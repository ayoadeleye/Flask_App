from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9a716eae4129c7b4a79e69ae1bb5d7dc'

posts = [
    {
        'author':'Ayooluwa Adeleye',
        'title':'Blog Post 1',
        'content':'First Post',
        'date_posted':'Feb 17, 2005'
    },
    {
        'author': 'Ayomikun Adeleye',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'Oct 16, 2009'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title='Registration', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
