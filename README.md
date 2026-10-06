<div align="center">
  <h1>✉️ md-mailer</h1>
  <p><b>Beautiful HTML emails from Markdown, sent instantly.</b></p>
  
  [![Python Versions](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

<hr/>

`md-mailer` is a lightweight Python library that bridges the gap between writing in Markdown and sending beautiful, email-client-safe HTML emails. 

Writing HTML emails by hand is notoriously difficult because email clients (Gmail, Outlook, Apple Mail) strip out `<style>` tags. `md-mailer` solves this by automatically parsing your Markdown, applying a beautiful GitHub-inspired theme, and safely inlining all CSS directly into the HTML elements using `premailer` before sending it out via SMTP.

## ✨ Key Features
- **Markdown Support:** Write your newsletters, alerts, or reports in standard Markdown (including tables, code blocks, and lists).
- **Auto-Inlining:** Automatically injects CSS styles into HTML tags to ensure cross-client compatibility.
- **Sleek Default Theme:** Comes with a beautiful, responsive, GitHub-inspired typography theme out-of-the-box.
- **Customizable:** Easily pass your own CSS file to override the default styles.
- **Simple API:** Send an email with just a single function call.

## 📦 Installation

Install via pip:

```bash
pip install md-mailer
```

## 🚀 Quick Start

1. Create a simple markdown file, e.g., `newsletter.md`:

```markdown
# Weekly Update
Hello! This is a **beautifully** formatted email sent directly from Python using `md-mailer`.

* 🚀 Fast
* 🎨 Beautiful
* ✉️ Reliable

### Data Summary
| Metric | Value |
|--------|-------|
| Users  | 1,024 |
| Uptime | 99.9% |
```

2. Send the email from your Python script:

```python
from md_mailer import send_email

send_email(
    markdown_path="newsletter.md",
    subject="Your Weekly Update",
    sender_email="you@example.com",
    recipient_email="recipient@example.com",
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    smtp_password="your_app_password"  # Use environment variables in production!
)
```

## 🛠️ Advanced Usage

### Using Custom CSS
If you want your emails to match your brand's styling, simply pass the path to your own CSS file. `md-mailer` will automatically parse and inline it for you.

```python
send_email(
    markdown_path="newsletter.md",
    subject="Branded Update",
    sender_email="you@example.com",
    recipient_email="recipient@example.com",
    smtp_server="smtp.gmail.com",
    smtp_password="your_app_password",
    css_path="path/to/your/custom_styles.css"  # <-- Inject custom CSS here
)
```

### Accessing the Raw HTML
If you just want the generated HTML (to use with an API like SendGrid or AWS SES) instead of sending it via SMTP directly:

```python
from md_mailer import convert_markdown_to_email_html

html_content = convert_markdown_to_email_html("newsletter.md")
print(html_content)
```

## 📚 API Reference

### `send_email(...)`
Sends an email natively using Python's `smtplib`.
* `markdown_path (str)`: Path to the source `.md` file.
* `subject (str)`: Email subject line.
* `sender_email (str)`: The 'From' address.
* `recipient_email (str)`: The 'To' address.
* `smtp_server (str)`: Your SMTP server (e.g. `smtp.gmail.com`).
* `smtp_port (int)`: SMTP port (defaults to `587`).
* `smtp_password (str)`: Authentication password.
* `css_path (str, optional)`: Path to a custom CSS file to apply.

### `convert_markdown_to_email_html(...)`
Returns the raw HTML string with inlined CSS.
* `md_path (str)`: Path to the source `.md` file.
* `css_path (str, optional)`: Path to a custom CSS file.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
This project is licensed under the MIT License.

## 👤 Author
Built with ❤️ by **Mayuri**.
