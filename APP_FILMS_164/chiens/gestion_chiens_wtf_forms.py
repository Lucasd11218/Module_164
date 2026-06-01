from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Regexp

class FormWTFAjouterChien(FlaskForm):
    nom_chien_regexp = ""
    nom_chien_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                    Regexp(nom_chien_regexp, message="Pas de caractères spéciaux")])
    race_chien_regexp = ""
    race_chien_wtf = StringField("Race", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                      Regexp(race_chien_regexp, message="Pas de caractères spéciaux")])
    age_chien_regexp = ""
    age_chien_wtf = StringField("Age", validators=[Length(min=1, max=3, message="min 1 max 3"),
                                                    Regexp(age_chien_regexp, message="Pas de caractères spéciaux")])
    taille_chien_regexp = ""
    taille_chien_wtf = StringField("Taille", validators=[Length(min=1, max=10, message="min 1 max 10"),
                                                          Regexp(taille_chien_regexp, message="Pas de caractères spéciaux")])
    notes_chien_regexp = ""
    notes_chien_wtf = StringField("Notes", validators=[Length(min=0, max=100, message="max 100"),
                                                        Regexp(notes_chien_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Enregistrer chien")

class FormWTFUpdateChien(FlaskForm):
    nom_chien_update_regexp = ""
    nom_chien_update_wtf = StringField("Nom", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                           Regexp(nom_chien_update_regexp, message="Pas de caractères spéciaux")])
    race_chien_update_regexp = ""
    race_chien_update_wtf = StringField("Race", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                             Regexp(race_chien_update_regexp, message="Pas de caractères spéciaux")])
    age_chien_update_regexp = ""
    age_chien_update_wtf = StringField("Age", validators=[Length(min=1, max=3, message="min 1 max 3"),
                                                           Regexp(age_chien_update_regexp, message="Pas de caractères spéciaux")])
    taille_chien_update_regexp = ""
    taille_chien_update_wtf = StringField("Taille", validators=[Length(min=1, max=10, message="min 1 max 10"),
                                                                  Regexp(taille_chien_update_regexp, message="Pas de caractères spéciaux")])
    notes_chien_update_regexp = ""
    notes_chien_update_wtf = StringField("Notes", validators=[Length(min=0, max=100, message="max 100"),
                                                               Regexp(notes_chien_update_regexp, message="Pas de caractères spéciaux")])
    submit = SubmitField("Update chien")

class FormWTFDeleteChien(FlaskForm):
    nom_chien_delete_wtf = StringField("Effacer ce chien")
    submit_btn_del = SubmitField("Effacer chien")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")