from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Regexp

class FormWTFAjouterPromeneur(FlaskForm):
    nom_promeneur_regexp = ""
    nom_promeneur_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                        Regexp(nom_promeneur_regexp, message="Pas de caractères spéciaux")])
    prenom_promeneur_regexp = ""
    prenom_promeneur_wtf = StringField("Prénom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                              Regexp(prenom_promeneur_regexp, message="Pas de caractères spéciaux")])
    email_promeneur_regexp = ""
    email_promeneur_wtf = StringField("Email", validators=[Length(min=5, max=50, message="min 5 max 50"),
                                                            Regexp(email_promeneur_regexp, message="Pas de caractères spéciaux")])
    telephone_promeneur_regexp = ""
    telephone_promeneur_wtf = StringField("Téléphone", validators=[Length(min=5, max=20, message="min 5 max 20"),
                                                                    Regexp(telephone_promeneur_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Enregistrer promeneur")

class FormWTFUpdatePromeneur(FlaskForm):
    nom_promeneur_update_regexp = ""
    nom_promeneur_update_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                               Regexp(nom_promeneur_update_regexp, message="Pas de caractères spéciaux")])
    prenom_promeneur_update_regexp = ""
    prenom_promeneur_update_wtf = StringField("Prénom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                     Regexp(prenom_promeneur_update_regexp, message="Pas de caractères spéciaux")])
    email_promeneur_update_regexp = ""
    email_promeneur_update_wtf = StringField("Email", validators=[Length(min=5, max=50, message="min 5 max 50"),
                                                                   Regexp(email_promeneur_update_regexp, message="Pas de caractères spéciaux")])
    telephone_promeneur_update_regexp = ""
    telephone_promeneur_update_wtf = StringField("Téléphone", validators=[Length(min=5, max=20, message="min 5 max 20"),
                                                                           Regexp(telephone_promeneur_update_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Update promeneur")

class FormWTFDeletePromeneur(FlaskForm):
    nom_promeneur_delete_wtf = StringField("Effacer ce promeneur")
    submit_btn_del = SubmitField("Effacer promeneur")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")