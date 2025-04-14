import os
import re
import smtplib
import mimetypes
import pytesseract
from email.message import EmailMessage
from dotenv import load_dotenv
from pdfminer.high_level import extract_text
from PIL import Image
from tkinter import Tk, filedialog

# Set Tesseract path (update yours if different)
pytesseract.pytesseract.tesseract_cmd = r"D:\Gamingfolder\Tesseract-OCR\tesseract.exe"

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"❌ Error extracting PDF: {e}")
        return ""

def extract_text_from_image(image_path):
    try:
        return pytesseract.image_to_string(Image.open(image_path))
    except Exception as e:
        print(f"❌ Error reading image: {e}")
        return ""

def extract_skills_and_fields(text):
    keywords = ["python", "java", "devops", "cloud", "docker", "kubernetes", "git", "linux", "machine learning"]
    return [word for word in keywords if word.lower() in text.lower()]

def simulate_recruiters(skills):
    recruiter_map = {
        "python": "hr.pythonjobs@example.com",
        "java": "java.hr@example.com",
        "devops": "devops.recruit@example.com",
        "cloud": "cloud.hiring@example.com",
    }
    return {skill: recruiter_map[skill] for skill in skills if skill in recruiter_map}

def browse_resume():
    Tk().withdraw()
    print("\n📄 Select your resume (PDF/Image)...")
    return filedialog.askopenfilename(filetypes=[("PDF or Image", "*.pdf *.png *.jpg *.jpeg")])

def compose_email(name, recruiter_email, skill):
    subject = f"Application for {skill.title()} Role"
    body = (
        f"Dear Recruiter,\n\n"
        f"I am {name}, writing to express my interest in roles related to {skill}.\n"
        f"Please find my resume attached for your review.\n\n"
        f"Regards,\n{name}"
    )
    return subject, body

def send_email(to_email, subject, body, resume_path):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach resume
    mime_type, _ = mimetypes.guess_type(resume_path)
    if mime_type:
        maintype, subtype = mime_type.split('/')
        with open(resume_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(resume_path))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")

def main():
    resume_path = browse_resume()
    if not resume_path:
        print("❌ No file selected.")
        return

    ext = os.path.splitext(resume_path)[1].lower()
    text = extract_text_from_pdf(resume_path) if ext == ".pdf" else extract_text_from_image(resume_path)

    if not text:
        print("❌ Failed to read resume content.")
        return

    skills = extract_skills_and_fields(text)
    if not skills:
        print("❌ No relevant skills found.")
        return

    print(f"\n🎯 Skills Detected: {', '.join(skills)}")
    recruiters = simulate_recruiters(skills)

    if not recruiters:
        print("❌ No recruiters matched your skills.")
        return

    print("\n📧 Emails will be sent to:")
    for skill, email in recruiters.items():
        print(f" - {skill.title()}: {email}")

    name = input("\n👤 Enter your full name: ").strip()

    for skill, email in recruiters.items():
        subject, body = compose_email(name, email, skill)
        send_email(email, subject, body, resume_path)

if __name__ == "__main__":
    main()
