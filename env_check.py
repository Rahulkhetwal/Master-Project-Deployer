import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

# Check if values are loading correctly
print("📧 GMAIL_ADDRESS =", os.getenv("GMAIL_ADDRESS"))
print("🔐 GMAIL_PASSWORD length =", len(os.getenv("GMAIL_PASSWORD") or ""))
print("🔑 GITHUB_TOKEN =", os.getenv("GITHUB_TOKEN"))
print("👤 GITHUB_USERNAME =", os.getenv("GITHUB_USERNAME"))
print("🧠 OPENAI_API_KEY length =", len(os.getenv("OPENAI_API_KEY") or ""))
