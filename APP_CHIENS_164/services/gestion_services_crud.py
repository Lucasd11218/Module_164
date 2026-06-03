from pathlib import Path
from flask import redirect, request, session, url_for
from APP_CHIENS_164 import app
from APP_CHIENS_164.database.database_tools import DBconnection
from APP_CHIENS_164.erreurs.exceptions import *
from APP_CHIENS_164.services.gestion_services_wtf_forms import FormWTFAjouterGenres, FormWTFDeleteGenre, FormWTFUpdateGenre


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    mc_afficher.execute("SELECT * FROM t_service ORDER BY id_service ASC")
                elif order_by == "ASC":
                    mc_afficher.execute("SELECT * FROM t_service WHERE id_service = %(val)s", {"val": id_genre_sel})
                else:
                    mc_afficher.execute("SELECT * FROM t_service ORDER BY id_service DESC")
                data_genres = mc_afficher.fetchall()
                if not data_genres and id_genre_sel == 0:
                    flash("La table t_service est vide.", "warning")
                elif not data_genres and id_genre_sel > 0:
                    flash("Le service demandé n'existe pas.", "warning")
                else:
                    flash("Données services affichés !", "success")
        except Exception as e:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name} ; genres_afficher ; {e}")
    return render_template("genres/genres_afficher.html", data=data_genres)


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                valeurs = {
                    "value_type_service": form.nom_service_wtf.data,
                    "value_duree": form.duree_service_wtf.data,
                    "value_prix": form.prix_service_wtf.data
                }
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("""INSERT INTO t_service (id_service, type_service, duree, prix)
                                        VALUES (NULL, %(value_type_service)s, %(value_duree)s, %(value_prix)s)""", valeurs)
                flash("Service ajouté !", "success")
                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))
        except Exception as e:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name} ; genres_ajouter_wtf ; {e}")
    return render_template("genres/genres_ajouter_wtf.html", form=form)


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    id_service_update = request.values['id_genre_btn_edit_html']
    form_update = FormWTFUpdateGenre()
    try:
        if request.method == "POST" and form_update.submit.data:
            valeurs = {
                "value_id_service": id_service_update,
                "value_type_service": form_update.type_service_update_wtf.data,
                "value_duree": form_update.duree_service_update_wtf.data,
                "value_prix": form_update.prix_service_update_wtf.data
            }
            with DBconnection() as mconn_bd:
                mconn_bd.execute("""UPDATE t_service SET type_service=%(value_type_service)s,
                                    duree=%(value_duree)s, prix=%(value_prix)s
                                    WHERE id_service=%(value_id_service)s""", valeurs)
            flash("Service modifié !", "success")
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_service_update))
        elif request.method == "GET":
            with DBconnection() as mybd_conn:
                mybd_conn.execute("SELECT * FROM t_service WHERE id_service = %(val)s", {"val": id_service_update})
                data = mybd_conn.fetchone()
            form_update.type_service_update_wtf.data = data["type_service"]
            form_update.duree_service_update_wtf.data = data["duree"]
            form_update.prix_service_update_wtf.data = data["prix"]
    except Exception as e:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name} ; genre_update_wtf ; {e}")
    return render_template("genres/genre_update_wtf.html", form_update=form_update)


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    btn_submit_del = None
    id_genre_delete = request.values['id_genre_btn_delete_html']
    form_delete = FormWTFDeleteGenre()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))
            if form_delete.submit_btn_conf_del.data:
                data_promenades = session['data_promenades_service']
                flash("Effacer le service de façon définitive !", "danger")
                btn_submit_del = True
            if form_delete.submit_btn_del.data:
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("DELETE FROM t_promeneur_chien_service WHERE FK_service = %(val)s", {"val": id_genre_delete})
                    mconn_bd.execute("DELETE FROM t_service WHERE id_service = %(val)s", {"val": id_genre_delete})
                flash("Service effacé !", "success")
                return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))
        if request.method == "GET":
            with DBconnection() as mydb_conn:
                mydb_conn.execute("""SELECT t_promeneur_chien_service.id_promeneur_chien_service,
                                    t_chien.nom
                                    FROM t_promeneur_chien_service
                                    INNER JOIN t_chien ON t_promeneur_chien_service.FK_chien = t_chien.id_chien
                                    WHERE FK_service = %(val)s""", {"val": id_genre_delete})
                data_promenades = mydb_conn.fetchall()
                session['data_promenades_service'] = data_promenades

                mydb_conn.execute("SELECT * FROM t_service WHERE id_service = %(val)s", {"val": id_genre_delete})
                data = mydb_conn.fetchone()
            form_delete.nom_genre_delete_wtf.data = data["type_service"]
            btn_submit_del = False
    except Exception as e:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name} ; genre_delete_wtf ; {e}")
    return render_template("genres/genre_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_promenades)