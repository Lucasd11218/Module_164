from pathlib import Path
from flask import redirect, request, session, url_for
from APP_CHIENS_164 import app
from APP_CHIENS_164.database.database_tools import DBconnection
from APP_CHIENS_164.erreurs.exceptions import *
from APP_CHIENS_164.chiens.gestion_chiens_wtf_forms import FormWTFAjouterChien, FormWTFDeleteChien, FormWTFUpdateChien


@app.route("/chiens_afficher/<string:order_by>/<int:id_chien_sel>", methods=['GET', 'POST'])
def chiens_afficher(order_by, id_chien_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_chien_sel == 0:
                    mc_afficher.execute("SELECT * FROM t_chien ORDER BY id_chien ASC")
                elif order_by == "ASC":
                    mc_afficher.execute("SELECT * FROM t_chien WHERE id_chien = %(val)s", {"val": id_chien_sel})
                else:
                    mc_afficher.execute("SELECT * FROM t_chien ORDER BY id_chien DESC")
                data_chiens = mc_afficher.fetchall()
                if not data_chiens and id_chien_sel == 0:
                    flash("La table t_chien est vide.", "warning")
                elif not data_chiens and id_chien_sel > 0:
                    flash("Le chien demandé n'existe pas.", "warning")
                else:
                    flash("Données chiens affichés !", "success")
        except Exception as e:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name} ; chiens_afficher ; {e}")
    return render_template("chiens/chiens_afficher.html", data=data_chiens)


@app.route("/chiens_ajouter", methods=['GET', 'POST'])
def chiens_ajouter_wtf():
    form = FormWTFAjouterChien()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                valeurs = {
                    "value_nom": form.nom_chien_wtf.data,
                    "value_race": form.race_chien_wtf.data,
                    "value_age": form.age_chien_wtf.data,
                    "value_taille": form.taille_chien_wtf.data,
                    "value_notes": form.notes_chien_wtf.data
                }
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("""INSERT INTO t_chien (id_chien, nom, race, age, taille, notes)
                                        VALUES (NULL, %(value_nom)s, %(value_race)s,
                                        %(value_age)s, %(value_taille)s, %(value_notes)s)""", valeurs)
                flash("Chien ajouté !", "success")
                return redirect(url_for('chiens_afficher', order_by='DESC', id_chien_sel=0))
        except Exception as e:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name} ; chiens_ajouter_wtf ; {e}")
    return render_template("chiens/chiens_ajouter_wtf.html", form=form)


@app.route("/chien_update", methods=['GET', 'POST'])
def chien_update_wtf():
    id_chien_update = request.values['id_chien_btn_edit_html']
    form_update = FormWTFUpdateChien()
    try:
        if request.method == "POST" and form_update.submit.data:
            valeurs = {
                "value_id_chien": id_chien_update,
                "value_nom": form_update.nom_chien_update_wtf.data,
                "value_race": form_update.race_chien_update_wtf.data,
                "value_age": form_update.age_chien_update_wtf.data,
                "value_taille": form_update.taille_chien_update_wtf.data,
                "value_notes": form_update.notes_chien_update_wtf.data
            }
            with DBconnection() as mconn_bd:
                mconn_bd.execute("""UPDATE t_chien SET nom=%(value_nom)s, race=%(value_race)s,
                                    age=%(value_age)s, taille=%(value_taille)s, notes=%(value_notes)s
                                    WHERE id_chien=%(value_id_chien)s""", valeurs)
            flash("Chien modifié !", "success")
            return redirect(url_for('chiens_afficher', order_by="ASC", id_chien_sel=id_chien_update))
        elif request.method == "GET":
            with DBconnection() as mybd_conn:
                mybd_conn.execute("SELECT * FROM t_chien WHERE id_chien = %(val)s", {"val": id_chien_update})
                data = mybd_conn.fetchone()
            form_update.nom_chien_update_wtf.data = data["nom"]
            form_update.race_chien_update_wtf.data = data["race"]
            form_update.age_chien_update_wtf.data = data["age"]
            form_update.taille_chien_update_wtf.data = data["taille"]
            form_update.notes_chien_update_wtf.data = data["notes"]
    except Exception as e:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name} ; chien_update_wtf ; {e}")
    return render_template("chiens/chien_update_wtf.html", form_update=form_update)


@app.route("/chien_delete", methods=['GET', 'POST'])
def chien_delete_wtf():
    btn_submit_del = None
    id_chien_delete = request.values['id_chien_btn_delete_html']
    form_delete = FormWTFDeleteChien()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("chiens_afficher", order_by="ASC", id_chien_sel=0))
            if form_delete.submit_btn_conf_del.data:
                data_promenades = session['data_promenades_chien']
                data_clients = session['data_clients_chien']
                flash("Effacer le chien de façon définitive !", "danger")
                btn_submit_del = True
            if form_delete.submit_btn_del.data:
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("DELETE FROM t_promeneur_chien_service WHERE FK_chien = %(val)s", {"val": id_chien_delete})
                    mconn_bd.execute("DELETE FROM t_client_chien WHERE FK_chien = %(val)s", {"val": id_chien_delete})
                    mconn_bd.execute("DELETE FROM t_chien WHERE id_chien = %(val)s", {"val": id_chien_delete})
                flash("Chien effacé !", "success")
                return redirect(url_for('chiens_afficher', order_by="ASC", id_chien_sel=0))
        if request.method == "GET":
            with DBconnection() as mydb_conn:
                mydb_conn.execute("""SELECT t_promeneur.nom, t_promeneur.prenom
                                    FROM t_promeneur_chien_service
                                    INNER JOIN t_promeneur ON t_promeneur_chien_service.FK_promeneur = t_promeneur.id_promeneur
                                    WHERE FK_chien = %(val)s""", {"val": id_chien_delete})
                data_promenades = mydb_conn.fetchall()
                session['data_promenades_chien'] = data_promenades

                mydb_conn.execute("""SELECT t_client.nom, t_client.prenom
                                    FROM t_client_chien
                                    INNER JOIN t_client ON t_client_chien.FK_client = t_client.id_client
                                    WHERE t_client_chien.FK_chien = %(val)s""", {"val": id_chien_delete})
                data_clients = mydb_conn.fetchall()
                session['data_clients_chien'] = data_clients

                mydb_conn.execute("SELECT * FROM t_chien WHERE id_chien = %(val)s", {"val": id_chien_delete})
                data = mydb_conn.fetchone()
            form_delete.nom_chien_delete_wtf.data = data["nom"]
            btn_submit_del = False
    except Exception as e:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name} ; chien_delete_wtf ; {e}")
    return render_template("chiens/chien_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_promenades=data_promenades,
                           data_clients=data_clients)