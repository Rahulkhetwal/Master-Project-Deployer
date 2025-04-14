# smart_email_dispatcher.py
import os
import fitz  # PyMuPDF
import requests
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import openai

load_dotenv()

# --- Constants ---
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


# --- Step 1: Extract text from uploaded PDF Resume ---
def extract_resume_text(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text.strip()


# --- Step 2: Use OpenAI to extract key skills and generate email text ---
def extract_skills_and_generate_email(resume_text):
    prompt = f"""
    You are an AI assistant. A user is applying for jobs and here is their resume:

    {resume_text}

    1. Extract the top 5 key skills from this resume.
    2. Generate a short, polite cold email for a recruiter introducing the candidate and requesting an opportunity.

    Respond in this format:
    SKILLS:
    - Skill 1
    - Skill 2
    ...

    EMAIL:
    Dear [Recruiter],
    ...
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']


# --- Step 3: Email Sender Function ---
def send_email(to_email, subject, content):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
        smtp.send_message(msg)
    print("✅ Email sent to", to_email)


# --- Sample Run ---
if __name__ == "__main__":
    resume_text = extract_resume_text("cvallpurpose1.pdf")  # already uploaded
    result = extract_skills_and_generate_email(resume_text)

    print("\n--- AI Generated Result ---\n")
    print(result)

    # Ask user for final input
    decision = input("\n❓ Do you want to send this email? (yes/edit/no): ").strip().lower()
    if decision == 'yes':
        recipient = input("Enter recruiter's email or your friend's email: ").strip()
        subject = "Application from Rahul Khetwal - Resume Attached"
        email_body = result.split("EMAIL:")[-1].strip()
        send_email(recipient, subject, email_body)
    elif decision == 'edit':
        print("✏️ Edit feature coming soon.")
    else:
        print("❌ Cancelled. Email not sent.")
