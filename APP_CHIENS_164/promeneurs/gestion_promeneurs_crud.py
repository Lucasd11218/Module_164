from pathlib import Path
from flask import redirect, request, session, url_for
from APP_CHIENS_164 import app
from APP_CHIENS_164.database.database_tools import DBconnection
from APP_CHIENS_164.erreurs.exceptions import *
from APP_CHIENS_164.promeneurs.gestion_promeneurs_wtf_forms import FormWTFAjouterPromeneur, FormWTFDeletePromeneur, FormWTFUpdatePromeneur


@app.route("/promeneurs_afficher/<string:order_by>/<int:id_promeneur_sel>", methods=['GET', 'POST'])
def promeneurs_afficher(order_by, id_promeneur_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_promeneur_sel == 0:
                    mc_afficher.execute("SELECT * FROM t_promeneur ORDER BY id_promeneur ASC")
                elif order_by == "ASC":
                    mc_afficher.execute("SELECT * FROM t_promeneur WHERE id_promeneur = %(val)s", {"val": id_promeneur_sel})
                else:
                    mc_afficher.execute("SELECT * FROM t_promeneur ORDER BY id_promeneur DESC")
                data_promeneurs = mc_afficher.fetchall()
                if not data_promeneurs and id_promeneur_sel == 0:
                    flash("La table t_promeneur est vide.", "warning")
                elif not data_promeneurs and id_promeneur_sel > 0:
                    flash("Le promeneur demandé n'existe pas.", "warning")
                else:
                    flash("Données promeneurs affichés !", "success")
        except Exception as e:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name} ; promeneurs_afficher ; {e}")
    return render_template("promeneurs/promeneurs_afficher.html", data=data_promeneurs)


@app.route("/promeneurs_ajouter", methods=['GET', 'POST'])
def promeneurs_ajouter_wtf():
    form = FormWTFAjouterPromeneur()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                valeurs = {
                    "value_nom": form.nom_promeneur_wtf.data,
                    "value_prenom": form.prenom_promeneur_wtf.data,
                    "value_email": form.email_promeneur_wtf.data,
                    "value_telephone": form.telephone_promeneur_wtf.data
                }
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("""INSERT INTO t_promeneur (id_promeneur, nom, prenom, email, telephone)
                                        VALUES (NULL, %(value_nom)s, %(value_prenom)s,
                                        %(value_email)s, %(value_telephone)s)""", valeurs)
                flash("Promeneur ajouté !", "success")
                return redirect(url_for('promeneurs_afficher', order_by='DESC', id_promeneur_sel=0))
        except Exception as e:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name} ; promeneurs_ajouter_wtf ; {e}")
    return render_template("promeneurs/promeneurs_ajouter_wtf.html", form=form)


@app.route("/promeneur_update", methods=['GET', 'POST'])
def promeneur_update_wtf():
    id_promeneur_update = request.values['id_promeneur_btn_edit_html']
    form_update = FormWTFUpdatePromeneur()
    try:
        if request.method == "POST" and form_update.submit.data:
            valeurs = {
                "value_id_promeneur": id_promeneur_update,
                "value_nom": form_update.nom_promeneur_update_wtf.data,
                "value_prenom": form_update.prenom_promeneur_update_wtf.data,
                "value_email": form_update.email_promeneur_update_wtf.data,
                "value_telephone": form_update.telephone_promeneur_update_wtf.data
            }
            with DBconnection() as mconn_bd:
                mconn_bd.execute("""UPDATE t_promeneur SET nom=%(value_nom)s, prenom=%(value_prenom)s,
                                    email=%(value_email)s, telephone=%(value_telephone)s
                                    WHERE id_promeneur=%(value_id_promeneur)s""", valeurs)
            flash("Promeneur modifié !", "success")
            return redirect(url_for('promeneurs_afficher', order_by="ASC", id_promeneur_sel=id_promeneur_update))
        elif request.method == "GET":
            with DBconnection() as mybd_conn:
                mybd_conn.execute("SELECT * FROM t_promeneur WHERE id_promeneur = %(val)s", {"val": id_promeneur_update})
                data = mybd_conn.fetchone()
            form_update.nom_promeneur_update_wtf.data = data["nom"]
            form_update.prenom_promeneur_update_wtf.data = data["prenom"]
            form_update.email_promeneur_update_wtf.data = data["email"]
            form_update.telephone_promeneur_update_wtf.data = data["telephone"]
    except Exception as e:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name} ; promeneur_update_wtf ; {e}")
    return render_template("promeneurs/promeneur_update_wtf.html", form_update=form_update)


@app.route("/promeneur_delete", methods=['GET', 'POST'])
def promeneur_delete_wtf():
    btn_submit_del = None
    id_promeneur_delete = request.values['id_promeneur_btn_delete_html']
    form_delete = FormWTFDeletePromeneur()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("promeneurs_afficher", order_by="ASC", id_promeneur_sel=0))
            if form_delete.submit_btn_conf_del.data:
                data_chiens = session['data_chiens_promeneur']
                flash("Effacer le promeneur de façon définitive !", "danger")
                btn_submit_del = True
            if form_delete.submit_btn_del.data:
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("DELETE FROM t_promeneur_chien_service WHERE FK_promeneur = %(val)s", {"val": id_promeneur_delete})
                    mconn_bd.execute("DELETE FROM t_promeneur WHERE id_promeneur = %(val)s", {"val": id_promeneur_delete})
                flash("Promeneur effacé !", "success")
                return redirect(url_for('promeneurs_afficher', order_by="ASC", id_promeneur_sel=0))
        if request.method == "GET":
            with DBconnection() as mydb_conn:
                mydb_conn.execute("""SELECT t_chien.nom
                                    FROM t_promeneur_chien_service
                                    INNER JOIN t_chien ON t_promeneur_chien_service.FK_chien = t_chien.id_chien
                                    WHERE FK_promeneur = %(val)s""", {"val": id_promeneur_delete})
                data_chiens = mydb_conn.fetchall()
                session['data_chiens_promeneur'] = data_chiens

                mydb_conn.execute("SELECT * FROM t_promeneur WHERE id_promeneur = %(val)s", {"val": id_promeneur_delete})
                data = mydb_conn.fetchone()
            form_delete.nom_promeneur_delete_wtf.data = data["nom"]
            btn_submit_del = False
    except Exception as e:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name} ; promeneur_delete_wtf ; {e}")
    return render_template("promeneurs/promeneur_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_chiens=data_chiens)