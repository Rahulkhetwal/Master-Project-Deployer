import smtplib

EMAIL = "itzrahul9548437@gmail.com"
PASSWORD = "slzoheqyaacttuux"

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        print("✅ Login successful!")
except Exception as e:
    print(f"❌ Login failed: {e}")
