import markdown
from premailer import transform
import os

def convert_markdown_to_email_html(md_path: str, css_path: str = None) -> str:
    """Reads a markdown file and converts it to HTML with inlined CSS."""
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"Markdown file not found: {md_path}")
        
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    # Convert MD to HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['extra', 'codehilite', 'tables']
    )
    
    # Load CSS
    if css_path is None:
        css_path = os.path.join(os.path.dirname(__file__), "templates", "default.css")
        
    if not os.path.exists(css_path):
        raise FileNotFoundError(f"CSS file not found: {css_path}")
        
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
        
    # Wrap in HTML document structure
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        {css_content}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Inline the CSS
    inlined_html = transform(full_html)
    return inlined_html
