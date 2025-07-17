import time
import requests
import random
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from celery.utils.log import get_task_logger

from .worker import celery_app

logger = get_task_logger(__name__)

# 🔧 1. Generic Python Job Task
@celery_app.task(name="run_python_job")
def run_python_job(job_name: str, duration: int = 5) -> str:
    logger.info(f"[{job_name}] Started, running for {duration}s")
    time.sleep(duration)
    result = f"[{job_name}] Completed after {duration}s"
    logger.info(result)
    return result

# 🌐 2. Scraping Task
@celery_app.task(name="scrape_url")
def scrape_url(url: str) -> str:
    """Fetch HTML content from a given URL."""
    try:
        logger.info(f"Scraping URL: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        error_msg = f"Scraping failed: {str(e)}"
        logger.error(error_msg)
        return error_msg

# 🧼 3. Parsing Task
@celery_app.task(name="parse_html")
def parse_html(html: str, tag: str = "p") -> list:
    """Extract text content from specific HTML tags."""
    try:
        logger.info(f"Parsing HTML for tag: <{tag}>")
        soup = BeautifulSoup(html, 'html.parser')
        content = [elem.get_text(strip=True) for elem in soup.find_all(tag)]
        return content
    except Exception as e:
        error_msg = f"Parsing failed: {str(e)}"
        logger.error(error_msg)
        return [error_msg]

# 🧠 4. Training Task (Mock)
@celery_app.task(name="train_model")
def train_model(data: list) -> str:
    """Fake training function to simulate model training."""
    try:
        logger.info(f"Training on {len(data)} samples...")
        time.sleep(5)
        return f"Training complete on {len(data)} samples"
    except Exception as e:
        error_msg = f"Training failed: {str(e)}"
        logger.error(error_msg)
        return error_msg

# 📧 5. Email Task
@celery_app.task(name="send_email")
def send_email(subject: str, body: str, to_email: str) -> str:
    """Send an email (requires valid SMTP config)."""
    try:
        from_email = "your_email@example.com"
        smtp_server = "smtp.example.com"
        smtp_port = 587
        password = "your_password"

        logger.info(f"Sending email to {to_email} with subject: {subject}")

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)

        return f"Email sent to {to_email}"
    except Exception as e:
        error_msg = f"Email failed: {str(e)}"
        logger.error(error_msg)
        return error_msg
