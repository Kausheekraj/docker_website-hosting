# docker_website-hosting
☁️ DevOps Task – EC2 Docker Deployment
This repository documents my GUVI DevOps assignment focused on deploying a Flask web application using Docker on an AWS EC2 instance. The project was developed locally using WSL Ubuntu and successfully deployed to the cloud.

✅ Tasks Performed
- Created a Flask app (app.py) that displays personal and tech stack details.
- Wrote a Dockerfile to containerize the app:
- Installed Flask via requirements.txt
- Set working directory and exposed port 5000
- Configured CMD to run the app
- Defined a docker-compose.yml to manage container lifecycle and port mapping.
- Transferred project files to EC2 using SCP and GitHub.
- Deployed the container using Docker Compose and verified the app via browser.
- Configured EC2 security group to allow HTTP and custom TCP traffic.

🖥️ Tech Stack
- AWS EC2 (Ubuntu 22.04 LTS)
- Docker & Docker Compose
- Flask (Python 3.10)
- WSL Ubuntu (Windows Subsystem for Linux)
- Git & GitHub

📚 References
- Docker Documentation — for containerization and Compose setup
- Personal notes and terminal logs from WSL Ubuntu
- GUVI DevOps course instructions and assignment brief
- Trial-and-error debugging across EC2, Docker, and Flask environments

📸 Screenshots
All terminal outputs, Docker logs, and browser screenshots confirming successful deployment are included in the repository.

📎 Submission
Submitted for GUVI DevOps EC2 + Docker Assignment. All required files, configuration scripts, and screenshots have been pushed to GitHub as per submission guidelines.
