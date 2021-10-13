from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email ,InputRequired

style1={'style':'margin:3px; border-color:grey'}
style2={'style':'margin:3px; border-color:grey; margin-left:12px'}
style3={'style':'margin:3px; border-color:grey;margin-left:20px'}

class Registro(FlaskForm):
    nombre1=StringField('Nombre',
    validators=[DataRequired(),Length(min=2)],render_kw=style1)
    tel1=StringField('Celular ', 
    validators=[DataRequired(),Length(min=9)],render_kw=style2)
    email=StringField('Email  ',validators=[DataRequired(), Email() ],render_kw=style3)
    nombre2=StringField('Nombre',
    validators=[DataRequired(),Length(min=2)],render_kw=style1)
    tel2=StringField('Celular ', 
    validators=[DataRequired(),Length(min=9)],render_kw=style2)
    categoria=SelectField(choices=[("V-A",'Varones-A'),("V-B",'Varones-B'),("M-M",'Mixto-Mujeres')], coerce=str,validators=[DataRequired()])
    confirmacion=BooleanField('SI',validators=[DataRequired()])
    submit=SubmitField('Inscribirse')

class Confirm(FlaskForm):
    submited=SubmitField('Confirmar')
