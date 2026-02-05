import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_contact_email(name, email, message):
    content = f"""
    New Contact Form Message

    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    mail = Mail(
        from_email=os.getenv("DEFAULT_FROM_EMAIL"),
        to_emails=os.getenv("ADMIN_EMAIL"),
        subject="New Contact Form Message",
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        sg.send(mail)
        return True
    except Exception as e:
        print("SENDGRID ERROR:", e)
        return False
