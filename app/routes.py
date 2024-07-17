from flask import Flask, render_template, request, redirect, url_for
from app import app

# Хранение введенных данных
users = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        users.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
        return redirect(url_for('index'))
    return render_template('blog.html', users=users)