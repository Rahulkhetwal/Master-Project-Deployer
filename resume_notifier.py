import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage

load_dotenv()

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def extract_text_from_image(file_path):
    image = Image.open(file_path)
    return pytesseract.image_to_string(image)

def generate_notice(text):
    # Simple mock-up for now
    return f"""
To Whom It May Concern,

I am writing to express my interest in job opportunities suitable to my qualifications. 

Below is a summary extracted from my resume:
{text[:500]}...

Thank you for your consideration.

Sincerely,
The Applicant
"""

def send_email(recipient, notice):
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg['Subject'] = 'Job Application Notice'
    msg['From'] = EMAIL
    msg['To'] = recipient
    msg.set_content(notice)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
    print("📤 Email sent successfully!")

def main():
    print("📤 Resume Automation System")
    file_path = input("📁 Enter the path to your resume (PDF/Image): ").strip()

    if not os.path.exists(file_path):
        print("❌ File not found. Please check the path.")
        return

    if file_path.lower().endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith((".jpg", ".png")):
        resume_text = extract_text_from_image(file_path)
    else:
        print("❌ Unsupported file type. Please upload a PDF or Image.")
        return

    notice = generate_notice(resume_text)
    with open("notice.txt", "w") as f:
        f.write(notice)
    print("✅ Notice generated and saved to notice.txt")

    choice = input("✉️ Do you want to send this to (1) Recruiters, (2) Friends, or (3) Yourself? ").strip()
    if choice == '1':
        recipient = os.getenv("RECRUITER_EMAIL")
    elif choice == '2':
        recipient = os.getenv("FRIEND_EMAIL")
    elif choice == '3':
        recipient = os.getenv("EMAIL")
    else:
        print("❌ Invalid choice. Email not sent.")
        return

    send_email(recipient, notice)

if __name__ == "__main__":
    main()
