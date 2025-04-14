import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("EMAIL_SENDER")
SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")  # App password if Gmail

def generate_cold_email(name, job_title):
    return f"""
Hi,

My name is {name}, and I'm writing to express my interest in any potential {job_title} opportunities at your company. I have a strong background in automation, DevOps, and project deployment using AI tools.

I recently created a tool called "Master Project Deployer" that automates coding, GitHub integration, and even job applications.

I’d love to discuss how I can contribute to your team.

Looking forward to hearing from you!

Thanks & regards,  
{name}
"""

def send_email(recipient, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
            print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    name = input("👤 Your Name: ")
    recipient = input("📧 Recruiter Email: ")
    job_title = input("💼 Job Title you're targeting: ")
    
    email_body = generate_cold_email(name, job_title)
    print("\n📄 Generated Email:\n")
    print(email_body)

    send = input("\n🚀 Send this email? (y/n): ").lower()
    if send == 'y':
        send_email(recipient, f"Looking for {job_title} role", email_body)
