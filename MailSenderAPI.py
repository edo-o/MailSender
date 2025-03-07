from flask import Flask, request, render_template
from flask_mail import Mail, Message
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

SENDGRID_API_KEY = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        receiver_email = request.form["email"]
        message_body = request.form["message"]

        message = Mail(
            from_email="eduardo@sagenedata.no",
            to_emails=receiver_email,
            subject="Ny Mail Fra IKT",
            plain_text_content=message_body,
        )

        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            reponse = sg.send(message)
            return f"Mail Sendt! Status: {reponse.status_code}"
        except Exception as e:
            return f"ERROR: {str(e)}"
    
    return '''
        <form method="POST">
            <label>Email to send message to:</label><br>
            <input type="email" name="email" required><br><br>
            <label>Message:</label><br>
            <textarea name="message" required></textarea><br><br>
            <button type="submit">Send Email</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)