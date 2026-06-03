from pathlib import Path
from flask import redirect, request, session, url_for
from APP_CHIENS_164 import app
from APP_CHIENS_164.database.database_tools import DBconnection
from APP_CHIENS_164.erreurs.exceptions import *
from APP_CHIENS_164.reservations.gestion_reservations_wtf_forms import FormWTFAjouterReservation, FormWTFDeleteReservation, FormWTFUpdateReservation


@app.route("/reservations_afficher/<string:order_by>/<int:id_reservation_sel>", methods=['GET', 'POST'])
def reservations_afficher(order_by, id_reservation_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_reservation_sel == 0:
                    mc_afficher.execute("SELECT * FROM t_reservation ORDER BY id_reservation ASC")
                elif order_by == "ASC":
                    mc_afficher.execute("SELECT * FROM t_reservation WHERE id_reservation = %(val)s", {"val": id_reservation_sel})
                else:
                    mc_afficher.execute("SELECT * FROM t_reservation ORDER BY id_reservation DESC")
                data_reservations = mc_afficher.fetchall()
                if not data_reservations and id_reservation_sel == 0:
                    flash("La table t_reservation est vide.", "warning")
                elif not data_reservations and id_reservation_sel > 0:
                    flash("La réservation demandée n'existe pas.", "warning")
                else:
                    flash("Données réservations affichées !", "success")
        except Exception as e:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name} ; reservations_afficher ; {e}")
    return render_template("reservations/reservations_afficher.html", data=data_reservations)


@app.route("/reservations_ajouter", methods=['GET', 'POST'])
def reservations_ajouter_wtf():
    form = FormWTFAjouterReservation()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                valeurs = {
                    "value_date": form.date_reservation_wtf.data,
                    "value_heure_debut": form.heure_debut_reservation_wtf.data,
                    "value_heure_fin": form.heure_fin_reservation_wtf.data,
                    "value_statut": form.statut_reservation_wtf.data
                }
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("""INSERT INTO t_reservation (id_reservation, date, heure_debut, heure_fin, statut)
                                        VALUES (NULL, %(value_date)s, %(value_heure_debut)s,
                                        %(value_heure_fin)s, %(value_statut)s)""", valeurs)
                flash("Réservation ajoutée !", "success")
                return redirect(url_for('reservations_afficher', order_by='DESC', id_reservation_sel=0))
        except Exception as e:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name} ; reservations_ajouter_wtf ; {e}")
    return render_template("reservations/reservations_ajouter_wtf.html", form=form)


@app.route("/reservation_update", methods=['GET', 'POST'])
def reservation_update_wtf():
    id_reservation_update = request.values['id_reservation_btn_edit_html']
    form_update = FormWTFUpdateReservation()
    try:
        if request.method == "POST" and form_update.submit.data:
            valeurs = {
                "value_id_reservation": id_reservation_update,
                "value_date": form_update.date_reservation_update_wtf.data,
                "value_heure_debut": form_update.heure_debut_reservation_update_wtf.data,
                "value_heure_fin": form_update.heure_fin_reservation_update_wtf.data,
                "value_statut": form_update.statut_reservation_update_wtf.data
            }
            with DBconnection() as mconn_bd:
                mconn_bd.execute("""UPDATE t_reservation SET date=%(value_date)s, heure_debut=%(value_heure_debut)s,
                                    heure_fin=%(value_heure_fin)s, statut=%(value_statut)s
                                    WHERE id_reservation=%(value_id_reservation)s""", valeurs)
            flash("Réservation modifiée !", "success")
            return redirect(url_for('reservations_afficher', order_by="ASC", id_reservation_sel=id_reservation_update))
        elif request.method == "GET":
            with DBconnection() as mybd_conn:
                mybd_conn.execute("SELECT * FROM t_reservation WHERE id_reservation = %(val)s", {"val": id_reservation_update})
                data = mybd_conn.fetchone()
            form_update.date_reservation_update_wtf.data = data["date"]
            form_update.heure_debut_reservation_update_wtf.data = data["heure_debut"]
            form_update.heure_fin_reservation_update_wtf.data = data["heure_fin"]
            form_update.statut_reservation_update_wtf.data = data["statut"]
    except Exception as e:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name} ; reservation_update_wtf ; {e}")
    return render_template("reservations/reservation_update_wtf.html", form_update=form_update)


@app.route("/reservation_delete", methods=['GET', 'POST'])
def reservation_delete_wtf():
    btn_submit_del = None
    id_reservation_delete = request.values['id_reservation_btn_delete_html']
    form_delete = FormWTFDeleteReservation()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("reservations_afficher", order_by="ASC", id_reservation_sel=0))
            if form_delete.submit_btn_conf_del.data:
                flash("Effacer la réservation de façon définitive !", "danger")
                btn_submit_del = True
            if form_delete.submit_btn_del.data:
                with DBconnection() as mconn_bd:
                    mconn_bd.execute("DELETE FROM t_reservation WHERE id_reservation = %(val)s", {"val": id_reservation_delete})
                flash("Réservation effacée !", "success")
                return redirect(url_for('reservations_afficher', order_by="ASC", id_reservation_sel=0))
        if request.method == "GET":
            with DBconnection() as mydb_conn:
                mydb_conn.execute("SELECT * FROM t_reservation WHERE id_reservation = %(val)s", {"val": id_reservation_delete})
                data = mydb_conn.fetchone()
            form_delete.date_reservation_delete_wtf.data = data["date"]
            btn_submit_del = False
    except Exception as e:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name} ; reservation_delete_wtf ; {e}")
    return render_template("reservations/reservation_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del)