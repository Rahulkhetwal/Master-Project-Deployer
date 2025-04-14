import os
import smtplib
import time
from dotenv import load_dotenv
from email.message import EmailMessage
from datetime import datetime

# Load environment variables
load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

recruiters = ["recruiter1@example.com", "recruiter2@example.com"]
friends = ["friend1@example.com", "friend2@example.com"]

def get_resume_text():
    try:
        with open("resume.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("❌ resume.txt not found!")
        exit()

def generate_email(resume_text):
    return f"""
Subject: Application for DevOps/AI Role – Based on My Resume

Dear Sir/Madam,

I am writing to express my keen interest in a DevOps or AI Engineering position. With strong technical expertise and real-world projects like "Master Project Deployer", I’d love to collaborate or contribute to your company.

Summary from my resume:
{resume_text[:300]}...

Looking forward to your response!

Warm regards,  
Rahul Khetwal  
GitHub: https://github.com/Rahulkhetwal
"""

def send_email(recipient, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = "DevOps/AI Job Application"
    msg["From"] = EMAIL_SENDER
    msg["To"] = recipient

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ Email sent to {recipient}")
        log_status(recipient, "SUCCESS")
    except Exception as e:
        print(f"❌ Failed to send to {recipient}: {e}")
        log_status(recipient, f"FAILED: {e}")

def log_status(recipient, status):
    with open("email_log.txt", "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] To: {recipient} - {status}\n")

def choose_recipient_group():
    print("\n🎯 Choose Recipient Group:")
    print("1. Send to Recruiters")
    print("2. Send to Friends")
    print("3. Send to Myself (Test Email)")

    choice = input("👉 Enter choice (1/2/3): ").strip()
    if choice == '1':
        return recruiters
    elif choice == '2':
        return friends
    elif choice == '3':
        return [EMAIL_SENDER]
    else:
        print("❌ Invalid choice. Defaulting to test email.")
        return [EMAIL_SENDER]

def save_draft(content):
    with open("draft_email.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("📄 Draft saved to 'draft_email.txt'")

def schedule_email():
    answer = input("⏰ Do you want to schedule this email? (yes/no): ").strip().lower()
    if answer == "yes":
        delay = input("⏳ Enter delay in seconds: ").strip()
        if delay.isdigit():
            print(f"🕒 Waiting for {delay} seconds before sending...")
            time.sleep(int(delay))
        else:
            print("❌ Invalid input. Skipping delay.")
    else:
        print("📤 Sending immediately...")

# Main
if __name__ == "__main__":
    resume = get_resume_text()
    content = generate_email(resume)
    
    save_draft(content)
    print("\n📧 Email Preview:\n")
    print(content)

    group = choose_recipient_group()
    confirm = input("\n✅ Ready to send? (yes/no): ").strip().lower()
    if confirm == "yes":
        schedule_email()
        for recipient in group:
            send_email(recipient, content)
    else:
        print("🚫 Email not sent. You can review draft_email.txt")
