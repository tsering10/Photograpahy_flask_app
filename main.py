import os

from flask import Flask
from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail
from flask_mail import Message



mail = Mail()

app = Flask(__name__)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_SUPPRESS_SEND"]= False
app.config["MAIL_USERNAME"] = 'youremail'
app.config["MAIL_PASSWORD"] = 'passowrd'

mail.init_app(app)


app.secret_key = 'development key'

@app.route("/")

def home():
    return render_template('index.html')

@app.route("/about")

def about_me():
    return render_template('about.html')


@app.route("/photos")

def photos():
    return render_template('photos.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='xyz@email.com', recipients=['xyz@email.com'])
      msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)




