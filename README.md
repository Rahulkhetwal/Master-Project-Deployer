# Master Project Deployer 🚀

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-Web_App_Library-000000?logo=flask)](https://flask.palletsprojects.com)
[![GitHub](https://img.shields.io/badge/GitHub-Automation-black?logo=github)](https://github.com)
[![AI](https://img.shields.io/badge/AI-Enhanced-yellow?logo=openai)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A powerful all-in-one tool for developers and job seekers to streamline productivity, automate workflows, and manage GitHub projects—all through an intuitive command-line interface.

---

## ✨ Features

- 🔹 **Basic Mode**: Lightweight code editor with real-time suggestions and execution.
- 🔸 **Advanced Mode**: AI-enhanced code editor with smart suggestions, syntax diagnosis, and fixes.
- ✅ **Automated GitHub Project Creation**: Initialize, commit, push, and pull with one click.
- ✉️ **Cold Email Generator**: Create and send emails to recruiters or collaborators.
- 📄 **Notice & Resume Automation**: Upload resume (PDF/Image), extract skills, auto-detect recruiters, and generate applications.
- 🔧 **AI-generated Project Templates** *(Advanced Mode)*
- 🔐 **Secure Mode Selection**: Choose between modes with password-protected access.
- 🔈 **Upcoming**: Voice command-based interaction.
- 🐳 **Planned**: Docker container support, GUI dashboard.

---

## 📂 Folder Structure
```
Master-Project-Deployer/
├── basic_editor.py          # Basic code editor
├── advanced_editor.py       # Advanced AI code editor
├── mode_selector.py         # Mode launcher
├── deploy.py                # GitHub deployer
├── smart_recruiter_fetcher.py # Resume parser + recruiter matcher
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation
1. Install **Python 3.10+**
2. Clone the repository:
   ```powershell
   git clone https://github.com/yourusername/Master-Project-Deployer.git
   cd Master-Project-Deployer
   ```
3. Install required packages:
   ```powershell
   pip install -r requirements.txt
   ```

---

## 🚀 Usage
To launch the interactive selector:
```powershell
python mode_selector.py
```

Or run a specific mode directly:
```powershell
python basic_editor.py         # For basic suggestions and execution
python advanced_editor.py      # For AI-enhanced diagnostics
python smart_recruiter_fetcher.py  # For uploading resume & cold emailing recruiters
```

To deploy your project to GitHub:
```powershell
python deploy.py
```

---

## 📸 Demo
```
🎯 Welcome to Code Editor Launcher
1. Basic Mode
2. Advanced Mode
Select your mode (1/2): 2
🚀 Launching Advanced Editor...

💡 Smart Suggestion: ['for i in range(5): print(i)']
❌ Error occurred:
Traceback... (Syntax Error Diagnosed)
🛠️ Suggestion: Fix missing ':' at the end of 'for' loop
```

---

## 🔮 Future Enhancements
- Voice command support with `speech_recognition` and `gTTS`
- Docker container build
- Web-based GUI using Flask + HTML/CSS/JS
- AI resume scanner and recruiter auto-fetching
- Auto Gmail sender (OAuth2)
- Project deployment to Replit or GitHub Pages

---

## 👨‍💼 Author
**Rahul Khetwal**  
[![GitHub](https://img.shields.io/badge/GitHub-@Rahulkhetwal-black?logo=github)](https://github.com/Rahulkhetwal)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rahul-blue?logo=linkedin)](https://linkedin.com/in/rahulkhetwal)

---

## 🤾 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> 💬 *Feel free to fork, contribute, or raise issues. Let’s make something awesome together!*
