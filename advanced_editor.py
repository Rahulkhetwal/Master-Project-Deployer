# advanced_editor.py

import os
import tempfile
import shutil
import subprocess
import smtplib
import mimetypes
import requests
from email.message import EmailMessage
from pdfminer.high_level import extract_text
from PIL import Image
from tkinter import Tk, filedialog
from dotenv import load_dotenv

load_dotenv()

# Environment Variables
EMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
REPO_NAME = "Master-Project-Deployer"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}"

class AdvancedEditor:
    def __init__(self):
        self.code_snippets = []
        self.temp_dir = tempfile.mkdtemp()

    def write_code(self, code):
        self.code_snippets.append(code)
        suggestions = self.get_suggestions(code)
        print("\n💡 Smart Suggestion:", suggestions)

    def get_suggestions(self, code):
        return [s for s in self.code_snippets if s.startswith(code[:3])]

    def execute_code(self, code):
        try:
            exec(code, {})
        except Exception as e:
            print("\n❌ Error occurred:")
            print(f"{type(e).__name__}: {e}")
            print("\n🔍 Diagnosis:")
            print(f"Line:     {code}")
            print(f"Error: {e}")
            print("🛠️ Suggestion: Check syntax or variable names around the mentioned line.")

    def clear_temp(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
        print("🗑️ Temporary files cleared (Advanced Mode).")

    def push_to_github(self):
        print("\n🚀 Auto GitHub Push Starting...")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Advanced editor auto commit"])
        subprocess.run(["git", "push", "origin", "main"])
        print("✅ Code pushed to GitHub")

    def extract_skills_from_resume(self):
        Tk().withdraw()
        print("\n📄 Select your resume (PDF/Image)...")
        file_path = filedialog.askopenfilename(filetypes=[("PDF or Image", "*.pdf *.png *.jpg *.jpeg")])

        if not file_path:
            print("⚠️ No file selected.")
            return [], None

        ext = os.path.splitext(file_path)[1].lower()
        try:
            if ext == ".pdf":
                text = extract_text(file_path)
            else:
                text = pytesseract.image_to_string(Image.open(file_path))
        except Exception as e:
            print(f"❌ Failed to extract text: {e}")
            return [], None

        skills_keywords = ["python", "devops", "java", "cloud", "docker", "git"]
        skills = [s for s in skills_keywords if s.lower() in text.lower()]
        return list(set(skills)), file_path

    def simulate_recruiters(self, skills):
        recruiter_map = {
            "python": "hr.pythonjobs@example.com",
            "java": "java.hr@example.com",
            "cloud": "cloud.hiring@example.com",
            "git": "versioncontrol.jobs@example.com"
        }
        return {s: recruiter_map[s] for s in skills if s in recruiter_map}

    def compose_email(self, name, to_email, skill):
        subject = f"Application for {skill.capitalize()} Developer Role"
        body = (
            f"Dear Recruiter,\n\n"
            f"I am {name}, deeply passionate about {skill} and interested in relevant roles.\n"
            f"Please find my resume attached.\n\nRegards,\n{name}"
        )
        return subject, body

    def send_email(self, to_email, subject, body, attachment_path):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg.set_content(body)

        mime_type, _ = mimetypes.guess_type(attachment_path)
        if mime_type:
            maintype, subtype = mime_type.split("/")
            with open(attachment_path, 'rb') as ap:
                msg.add_attachment(ap.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(attachment_path))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print(f"✅ Email sent to {to_email}")
        except Exception as e:
            print(f"❌ Failed to send to {to_email}: {e}")

    def run(self):
        print("\n✨ Advanced Editor Activated")
        code = input("\n💻 Enter your Python code: ")
        self.write_code(code)
        self.execute_code(code)

        print("\n📤 Initiating GitHub Push and Resume Scanner...")
        self.push_to_github()

        skills, resume = self.extract_skills_from_resume()
        if not skills:
            print("❌ No valid skills extracted.")
            return

        print(f"\n🎯 Skills Detected: {', '.join(skills)}")
        matches = self.simulate_recruiters(skills)
        if not matches:
            print("❌ No recruiters found.")
            return

        print("\n📧 Emails will be sent to:")
        for s, e in matches.items():
            print(f" - {s.capitalize()}: {e}")

        name = input("\n👤 Enter your full name: ")
        for skill, email in matches.items():
            subject, body = self.compose_email(name, email, skill)
            self.send_email(email, subject, body, resume)

        self.clear_temp()

if __name__ == "__main__":
    AdvancedEditor().run()
