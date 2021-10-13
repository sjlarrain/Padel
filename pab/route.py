
from flask import render_template, url_for, flash, redirect
from pab import app, db
from pab.registro import Registro, Confirm
from pab.database import User 

@app.route('/')
def entrada():
    return redirect('home')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/tournaments')
def tournaments():
    return render_template('tournaments.html') 

@app.route('/inscripciones', methods=['GET','POST'])
def inscripciones():
    form = Registro()
    if form.validate_on_submit():
        user = User(nombre1=form.nombre1.data, nombre2=form.nombre2.data, tel1=form.tel1.data, tel2=form.tel2.data, email=form.email.data, cat=form.categoria.data)
        conf=Confirm()
        if  conf.validate_on_submit() and form.confirmacion.data:
            db.session.add(user)
            db.session.commit()
            return redirect('inscripciones2')      
    return render_template('inscripciones.html', form=form )
    
@app.route('/inscripciones2')
def inscripciones2():
    return render_template('inscripciones2.html')


    

