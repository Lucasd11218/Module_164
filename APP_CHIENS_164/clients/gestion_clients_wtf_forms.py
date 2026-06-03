from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Regexp

class FormWTFAjouterClient(FlaskForm):
    nom_client_regexp = ""
    nom_client_wtf = StringField("Nom", validators=[Length(min=2, max=70, message="min 2 max 70"),
                                                     Regexp(nom_client_regexp, message="Pas de caractères spéciaux")])
    prenom_client_regexp = ""
    prenom_client_wtf = StringField("Prénom", validators=[Length(min=2, max=70, message="min 2 max 70"),
                                                           Regexp(prenom_client_regexp, message="Pas de caractères spéciaux")])
    email_client_regexp = ""
    email_client_wtf = StringField("Email", validators=[Length(min=5, max=100, message="min 5 max 100"),
                                                         Regexp(email_client_regexp, message="Pas de caractères spéciaux")])
    telephone_client_regexp = ""
    telephone_client_wtf = StringField("Téléphone", validators=[Length(min=5, max=20, message="min 5 max 20"),
                                                                  Regexp(telephone_client_regexp, message="Pas de caractères spéciaux")])
    adresse_client_regexp = ""
    adresse_client_wtf = StringField("Adresse", validators=[Length(min=5, max=150, message="min 5 max 150"),
                                                              Regexp(adresse_client_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Enregistrer client")

class FormWTFUpdateClient(FlaskForm):
    nom_client_update_regexp = ""
    nom_client_update_wtf = StringField("Nom", validators=[Length(min=2, max=70, message="min 2 max 70"),
                                                            Regexp(nom_client_update_regexp, message="Pas de caractères spéciaux")])
    prenom_client_update_regexp = ""
    prenom_client_update_wtf = StringField("Prénom", validators=[Length(min=2, max=70, message="min 2 max 70"),
                                                                   Regexp(prenom_client_update_regexp, message="Pas de caractères spéciaux")])
    email_client_update_regexp = ""
    email_client_update_wtf = StringField("Email", validators=[Length(min=5, max=100, message="min 5 max 100"),
                                                                 Regexp(email_client_update_regexp, message="Pas de caractères spéciaux")])
    telephone_client_update_regexp = ""
    telephone_client_update_wtf = StringField("Téléphone", validators=[Length(min=5, max=20, message="min 5 max 20"),
                                                                         Regexp(telephone_client_update_regexp, message="Pas de caractères spéciaux")])
    adresse_client_update_regexp = ""
    adresse_client_update_wtf = StringField("Adresse", validators=[Length(min=5, max=150, message="min 5 max 150"),
                                                                     Regexp(adresse_client_update_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Update client")

class FormWTFDeleteClient(FlaskForm):
    nom_client_delete_wtf = StringField("Effacer ce client")
    submit_btn_del = SubmitField("Effacer client")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")