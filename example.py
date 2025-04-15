from flask import Flask, render_template, url_for, request, flash, session,redirect

app = Flask(__name__)

app.config['SECRET_KEY']='vsvsvsfkbmdofbimsdobmsob'

menu=[{"name":'Установка', 'url':"install-flask"},{'name':"Первое приложение", 'url':"first-app"}, {'name':"Обратная связь", 'url':"contact"}]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

@app.route('/profile/<username>')
def profile(username):
    return f'Пользователь: {username}'

@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О сайте', menu=menu)

@app.route('/contact', methods=["POST","GET"])
def contact():
    if request.method=='POST':
        if len(request.form['username'])>2:
            flash('Сообщение отправлено',category='success')
        else:
            flash('Ошибка отправки',category='error')
    
    return render_template('contact.html',title='Обратная связь', menu=menu)

@app.route('/login', methods=["POST","GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile',username=session['userLogged']))
    elif request.method=='POST' and request.form['username']=='david'and request.form['psw']=='12345':
        session['userLogged']=request.form['username']
        return redirect(url_for('profile',username=session['userLogged']))  
    return render_template('login.html',title="Авторизация", menu=menu)

@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title='Your page not found', menu=menu),404


if __name__=="__main__":
    app.run(debug=True)