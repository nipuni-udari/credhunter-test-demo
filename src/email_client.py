import sendgrid
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "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"
FROM_EMAIL = "noreply@mycompany.com"
FROM_NAME = "My Company"


def send_welcome_email(to_email: str, username: str) -> bool:
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    message = Mail(
        from_email=(FROM_EMAIL, FROM_NAME),
        to_emails=to_email,
        subject="Welcome to My Company",
        plain_text_content=f"Hello {username}, welcome aboard!",
    )
    response = sg.send(message)
    return response.status_code == 202


def send_password_reset(to_email: str, reset_link: str) -> bool:
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    message = Mail(
        from_email=(FROM_EMAIL, FROM_NAME),
        to_emails=to_email,
        subject="Password Reset Request",
        plain_text_content=f"Reset your password here: {reset_link}",
    )
    response = sg.send(message)
    return response.status_code == 202


def send_invoice(to_email: str, invoice_id: str, amount: float) -> bool:
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    message = Mail(
        from_email=(FROM_EMAIL, FROM_NAME),
        to_emails=to_email,
        subject=f"Invoice #{invoice_id}",
        plain_text_content=f"Your invoice #{invoice_id} for ${amount:.2f} is ready.",
    )
    response = sg.send(message)
    return response.status_code == 202
