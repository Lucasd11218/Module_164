from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Regexp

class FormWTFAjouterReservation(FlaskForm):
    date_reservation_regexp = ""
    date_reservation_wtf = StringField("Date", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                            Regexp(date_reservation_regexp, message="Pas de caractères spéciaux")])
    heure_debut_reservation_regexp = ""
    heure_debut_reservation_wtf = StringField("Heure début", validators=[Length(min=2, max=10, message="min 2 max 10"),
                                                                           Regexp(heure_debut_reservation_regexp, message="Pas de caractères spéciaux")])
    heure_fin_reservation_regexp = ""
    heure_fin_reservation_wtf = StringField("Heure fin", validators=[Length(min=2, max=10, message="min 2 max 10"),
                                                                       Regexp(heure_fin_reservation_regexp, message="Pas de caractères spéciaux")])
    statut_reservation_regexp = ""
    statut_reservation_wtf = StringField("Statut", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                Regexp(statut_reservation_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Enregistrer réservation")

class FormWTFUpdateReservation(FlaskForm):
    date_reservation_update_regexp = ""
    date_reservation_update_wtf = StringField("Date", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                    Regexp(date_reservation_update_regexp, message="Pas de caractères spéciaux")])
    heure_debut_reservation_update_regexp = ""
    heure_debut_reservation_update_wtf = StringField("Heure début", validators=[Length(min=2, max=10, message="min 2 max 10"),
                                                                                  Regexp(heure_debut_reservation_update_regexp, message="Pas de caractères spéciaux")])
    heure_fin_reservation_update_regexp = ""
    heure_fin_reservation_update_wtf = StringField("Heure fin", validators=[Length(min=2, max=10, message="min 2 max 10"),
                                                                              Regexp(heure_fin_reservation_update_regexp, message="Pas de caractères spéciaux")])
    statut_reservation_update_regexp = ""
    statut_reservation_update_wtf = StringField("Statut", validators=[Length(min=2, max=50, message="min 2 max 50"),
                                                                       Regexp(statut_reservation_update_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Update réservation")

class FormWTFDeleteReservation(FlaskForm):
    date_reservation_delete_wtf = StringField("Effacer cette réservation")
    submit_btn_del = SubmitField("Effacer réservation")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")