from pathlib import Path

from dotenv import dotenv_values
from great_expectations.checkpoint.actions import EmailAction


# ---------------------------------------------------------------------
# Load configuration
# ---------------------------------------------------------------------

env_path = Path.cwd() / ".env"

if not env_path.exists():
    raise FileNotFoundError(
        ".env file not found. Create one from .env.example."
    )

config = dotenv_values(env_path)

email_user = config.get("EMAIL_USER")
email_password = config.get("EMAIL_PASSWORD")

if email_user is None:
    raise ValueError("EMAIL_USER is missing in .env")

if email_password is None:
    raise ValueError("EMAIL_PASSWORD is missing in .env")


# ---------------------------------------------------------------------
# Email Action
# ---------------------------------------------------------------------

email_action = EmailAction(
    name="email_notification",

    # Gmail SMTP
    smtp_address="smtp.gmail.com",
    smtp_port=587, # type: ignore

    # Sender
    sender_login=email_user,
    sender_password=email_password,
    sender_alias="Great Expectations",

    # Receiver
    receiver_emails=email_user,

    # Gmail settings
    use_tls=True,
    use_ssl=False,

    # Send notification for every validation (learning)
    notify_on="all",
)
