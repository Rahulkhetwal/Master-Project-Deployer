from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import subprocess

app = Flask(__name__)
app.secret_key = "super_secret_key"

OWNER_PASSWORD = "masterrahul9731@#"
BASE_PATH = "D:/Master_Project_Deployer/guest_projects/"

def create_project(project_name):
    """Creates a new project directory with a sample file."""
    project_path = os.path.join(BASE_PATH, project_name)
    os.makedirs(project_path, exist_ok=True)
    with open(os.path.join(project_path, "main.py"), "w") as f:
        f.write('print("Hello, this is your automated project!")')
    return project_path

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/owner", methods=["POST"])
def owner_login():
    """Handles owner login authentication."""
    password = request.form.get("password")
    if password == OWNER_PASSWORD:
        session["owner"] = True
        return redirect(url_for("dashboard"))
    else:
        flash("Incorrect password! Access Denied.", "danger")
        return redirect(url_for("home"))

@app.route("/guest", methods=["POST"])
def guest_mode():
    """Handles guest project creation."""
    project_name = request.form.get("project_name")
    if not project_name:
        flash("Project name cannot be empty!", "warning")
        return redirect(url_for("home"))

    project_path = create_project(project_name)
    session["guest_project"] = project_name

    flash("Project created successfully!", "success")
    return redirect(url_for("preview"))

@app.route("/preview")
def preview():
    """Displays the generated project files for review."""
    project_name = session.get("guest_project", "")
    project_path = os.path.join(BASE_PATH, project_name)

    if not os.path.exists(project_path):
        flash("Project not found!", "danger")
        return redirect(url_for("home"))

    files = os.listdir(project_path)
    file_contents = {}
    for file in files:
        with open(os.path.join(project_path, file), "r") as f:
            file_contents[file] = f.read()

    return render_template("preview.html", project_name=project_name, file_contents=file_contents)

@app.route("/approve", methods=["POST"])
def approve_project():
    """Handles project approval and pushes to GitHub."""
    project_name = session.get("guest_project", "")
    github_url = request.form.get("github_url")

    if not github_url:
        flash("GitHub URL is required!", "danger")
        return redirect(url_for("preview"))

    project_path = os.path.join(BASE_PATH, project_name)

    # GitHub push commands
    os.system(f'cd "{project_path}" && git init')
    os.system(f'cd "{project_path}" && git add .')
    os.system(f'cd "{project_path}" && git commit -m "Initial Commit"')
    os.system(f'cd "{project_path}" && git branch -M main')
    os.system(f'cd "{project_path}" && git remote add origin {github_url}')
    os.system(f'cd "{project_path}" && git push -u origin main')

    flash("Project successfully pushed to GitHub!", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
