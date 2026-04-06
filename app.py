from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from config import email,senha

app = Flask(__name__)
app.secret_key = 'thicode'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['name'],
            request.form['email'],
            request.form['message']
            )
        
        msg = Message(
            subject = f'{formContato.name} te enviou uma mensagem no portfólio.',
            sender = app.config.get("MAIL_USERNAME"),
            recipients = ['orlandofilhodirect@gmail.com', app.config.get("MAIL_USERNAME")],
            body = f'''

            {formContato.name} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

            {formContato.message}

            '''
        )
        mail.send(msg)
        flash('Message sent successfully!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

