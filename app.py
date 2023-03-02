from flask import *
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='lgekrhqmh01.lge.com',
    MAIL_PORT=25,
    MAIL_DEFAULT_SENDER=('CostReview', 'eunbi1.yoon@lge.com'),

)

mail = Mail(app)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/send_mail", methods=['POST'])
def send_mail():
    email = request.form['email'].strip()
    subject = 'Hello'
    message = 'This is test email'
    msg = Message(
        subject=subject,
        recipients=[email],
        html=message
    )
    # msg.body 
    with app.open_resource("static/images/image.jpg") as fp:
        msg.attach("image.jpg", "image/jpg", fp.read())
    mail.send(msg)

    # return 
    return render_template("thank.html")

if __name__ == '__main__':
    app.run()
