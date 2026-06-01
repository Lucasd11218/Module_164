from pathlib import Path
from flask import redirect, request, session, url_for
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.clients.gestion_clients_wtf_forms import FormWTFAjouterClient, FormWTFDeleteClient, FormWTFUpdateClient


@app.route("/clients_afficher/<string:order_by>/<int:id_client_sel>", methods=['GET', 'POST'])
def clients_afficher(order_by, id_client_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_client_sel == 0:
                    mc_afficher.execute("SELECT * FROM t_client ORDER BY id_client ASC")
                elif order_by == "ASC":
                    mc_afficher.execute("SELECT * FROM t_client WHERE id_client = %(val)s", {"val": id_client_sel})
                else:
                    mc_afficher.execute("SELECT * FROM t_client ORDER BY id_client DESC")
                data_clients = mc_afficher.fetchall()
                if not data_clients and id_client_sel == 0:
                    flash("La table t_client est vide.", "warning")
                elif not data_clients and id_client_sel > 0:
                    flash("Le client demandé n'existe pas.", "warning")
                else:
                    flash("Données clients affichés !", "success")
        except Exception as e:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name} ; clients_afficher ; {e}")
    return render_template("clients/clients_afficher.html", data=data_clients)


@app.route("/clients_ajouter", methods=['GET', 'POST'])
def clients_ajouter_wtf():
    form = FormWTFAjouterClient()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                valeurs = {
                    "value_nom": form.nom_client_wtf.data,
                    "value_prenom": form.prenom_client_wtf.data,
                    "value_email": form.email_client_wtf.data,
                    "value_telephone": form.telephone_client_wtf.data,
                    "value_adresse": form.adresse_client_wtf.data
                }
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("""INSERT INTO t_client (id_client, nom, prenom, email, telephone, adresse)
                                        VALUES (NULL, %(value_nom)s, %(value_prenom)s,
                                        %(value_email)s, %(value_telephone)s, %(value_adresse)s)""", valeurs)
                flash("Client ajouté !", "success")
                return redirect(url_for('clients_afficher', order_by='DESC', id_client_sel=0))
        except Exception as e:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name} ; clients_ajouter_wtf ; {e}")
    return render_template("clients/clients_ajouter_wtf.html", form=form)


@app.route("/client_update", methods=['GET', 'POST'])
def client_update_wtf():
    id_client_update = request.values['id_client_btn_edit_html']
    form_update = FormWTFUpdateClient()
    try:
        if request.method == "POST" and form_update.submit.data:
            valeurs = {
                "value_id_client": id_client_update,
                "value_nom": form_update.nom_client_update_wtf.data,
                "value_prenom": form_update.prenom_client_update_wtf.data,
                "value_email": form_update.email_client_update_wtf.data,
                "value_telephone": form_update.telephone_client_update_wtf.data,
                "value_adresse": form_update.adresse_client_update_wtf.data
            }
            with DBconnection() as mconn_bd:
                mconn_bd.execute("""UPDATE t_client SET nom=%(value_nom)s, prenom=%(value_prenom)s,
                                    email=%(value_email)s, telephone=%(value_telephone)s,
                                    adresse=%(value_adresse)s
                                    WHERE id_client=%(value_id_client)s""", valeurs)
            flash("Client modifié !", "success")
            return redirect(url_for('clients_afficher', order_by="ASC", id_client_sel=id_client_update))
        elif request.method == "GET":
            with DBconnection() as mybd_conn:
                mybd_conn.execute("SELECT * FROM t_client WHERE id_client = %(val)s", {"val": id_client_update})
                data = mybd_conn.fetchone()
            form_update.nom_client_update_wtf.data = data["nom"]
            form_update.prenom_client_update_wtf.data = data["prenom"]
            form_update.email_client_update_wtf.data = data["email"]
            form_update.telephone_client_update_wtf.data = data["telephone"]
            form_update.adresse_client_update_wtf.data = data["adresse"]
    except Exception as e:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name} ; client_update_wtf ; {e}")
    return render_template("clients/client_update_wtf.html", form_update=form_update)


@app.route("/client_delete", methods=['GET', 'POST'])
def client_delete_wtf():
    btn_submit_del = None
    id_client_delete = request.values['id_client_btn_delete_html']
    form_delete = FormWTFDeleteClient()
    data_chiens = []
    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("clients_afficher", order_by="ASC", id_client_sel=0))
            if form_delete.submit_btn_conf_del.data:
                data_chiens = session['data_chiens_client']
                flash("Effacer le client de façon définitive !", "danger")
                btn_submit_del = True
                return render_template("clients/client_delete_wtf.html",
                                       form_delete=form_delete,
                                       btn_submit_del=btn_submit_del,
                                       data_chiens=data_chiens)
            if form_delete.submit_btn_del.data:
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("DELETE FROM t_client_chien WHERE FK_client = %(val)s", {"val": id_client_delete})
                    mconn_bd.execute("DELETE FROM t_client WHERE id_client = %(val)s", {"val": id_client_delete})
                flash("Client effacé !", "success")
                return redirect(url_for('clients_afficher', order_by="ASC", id_client_sel=0))
        if request.method == "GET":
            with DBconnection() as mydb_conn:
                mydb_conn.execute("""SELECT t_chien.nom
                                    FROM t_client_chien
                                    INNER JOIN t_chien ON t_client_chien.FK_chien = t_chien.id_chien
                                    WHERE t_client_chien.FK_client = %(val)s""", {"val": id_client_delete})
                data_chiens = mydb_conn.fetchall()
                session['data_chiens_client'] = data_chiens

                mydb_conn.execute("SELECT * FROM t_client WHERE id_client = %(val)s", {"val": id_client_delete})
                data = mydb_conn.fetchone()
            form_delete.nom_client_delete_wtf.data = data["nom"]
            btn_submit_del = False
    except Exception as e:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name} ; client_delete_wtf ; {e}")
    return render_template("clients/client_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_chiens=data_chiens)