import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    # Get variables from GitHub Secrets and Payload
    sender_email = os.getenv("GMAIL_USER")
    sender_password = os.getenv("GMAIL_PASS")
    video_url = os.getenv("VIDEO_URL")
    user_message = os.getenv("USER_MESSAGE")
    
    receiver_email = sender_email  # Sending it to yourself

    # Create the email content
    subject = "New Video Automation Entry"
    body = f"""
    Hello,

    You have sent a new request via mobile automation:

    Message: {user_message}
    Video Link: {video_url}

    Sent via GitHub Actions.
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail Server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_email()
