import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .converter import convert_markdown_to_email_html

def send_email(
    markdown_path: str,
    subject: str,
    sender_email: str,
    recipient_email: str,
    smtp_server: str,
    smtp_port: int = 587,
    smtp_password: str = None,
    css_path: str = None
):
    """Converts a Markdown file to an HTML email and sends it via SMTP."""
    
    html_body = convert_markdown_to_email_html(markdown_path, css_path)
    
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email
    
    # Attach HTML content
    part = MIMEText(html_body, "html")
    msg.attach(part)
    
    # Send via SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        if smtp_password:
            server.login(sender_email, smtp_password)
        server.send_message(msg)
