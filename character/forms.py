from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class CharacterForm(FlaskForm):
    id = IntegerField("Identificador", validators=[DataRequired()])
    name = StringField("Nome do Personagem", validators=[DataRequired()])
    level = IntegerField("Nível")
    exp = StringField("Experiência")
    classe = StringField("Classe")