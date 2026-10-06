# md-mailer

A Python library that takes your standard Markdown files, converts them into beautifully styled HTML with inlined CSS (perfect for email clients), and sends them via SMTP—all in just a couple lines of code.

## Installation

```bash
pip install md-mailer
```

## Usage

Create a markdown file (`newsletter.md`):
```markdown
# Weekly Update
Hello! This is a **beautifully** formatted email sent directly from Python using `md-mailer`.

* Feature 1
* Feature 2
```

Send it using Python:

```python
from md_mailer import send_email

send_email(
    markdown_path="newsletter.md",
    subject="Your Weekly Update",
    sender_email="you@example.com",
    recipient_email="recipient@example.com",
    smtp_server="smtp.example.com",
    smtp_port=587,
    smtp_password="your_password"
)
```

## Author
Built by Mayuri.
