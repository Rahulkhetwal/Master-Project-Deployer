import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load .env credentials
load_dotenv()
EMAIL = os.getenv("GMAIL_USER")
PASSWORD = os.getenv("GMAIL_PASS")

# Simulated recruiter emails (in real use, scrape or read from file/db)
recruiters = [
    "hr.techstartups@gmail.com",
    "recruiter.aiwave@outlook.com",
    "jobs@codehire.com",
    "hiring.devlaunchers@gmail.com",
    "talent@nextgen.tech"
]

# Read resume from resume.txt
with open("resume.txt", "r") as file:
    resume = file.read()

# Auto-generated cold email body (simulated AI generation)
email_body = f"""
Subject: Passionate DevOps Engineer | Available for Internships/Projects 🚀

Dear Recruiter,

I hope you're doing well! I'm Rahul, a DevOps enthusiast with hands-on experience in automating CI/CD pipelines, system backups, and real-world scripting using Python & MobaXterm.

Projects like "Master Project Deployer", "Interview Bot", and "Security Compliance Checker" reflect my passion for efficient, real-world tech solutions.

I'd love to contribute to your team or upcoming projects. Please find my resume below:
\n\n{resume}\n\n
Looking forward to hearing from you!

Best Regards,  
Rahul Khetwal  
GitHub: https://github.com/rahul-khetwal
"""

# Send emails
def send_emails():
    print("📤 Sending cold emails to recruiters...")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        for recipient in recruiters:
            msg = MIMEText(email_body)
            msg["Subject"] = "DevOps Internship | Rahul Khetwal"
            msg["From"] = EMAIL
            msg["To"] = recipient

            server.sendmail(EMAIL, recipient, msg.as_string())
            print(f"✅ Sent to {recipient}")

        server.quit()
        print("🎉 All cold emails sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send emails: {e}")

if __name__ == "__main__":
    send_emails()
