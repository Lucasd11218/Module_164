"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_service_regexp = ""
    nom_service_wtf = StringField("Service", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_service_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    duree_service_regexp=""
    duree_service_wtf = StringField("Durée", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(duree_service_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    prix_service_regexp = ""
    prix_service_wtf = StringField("prix", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                         Regexp(duree_service_regexp,
                                                                message="Pas de chiffres, de caractères "
                                                                        "spéciaux, "
                                                                        "d'espace à double, de double "
                                                                        "apostrophe, de double trait union")
                                                         ])
    submit = SubmitField("Enregistrer genre")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    type_service_update_regexp = ""
    type_service_update_wtf = StringField("nom_service", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(type_service_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    duree_service_update_regexp=""
    duree_service_update_wtf = StringField("Durée", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(duree_service_update_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    prix_service_update_regexp=""
    prix_service_update_wtf = StringField("Prix", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(prix_service_update_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])

    submit = SubmitField("Update genre")

class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer ce genre")
    submit_btn_del = SubmitField("Effacer genre")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
