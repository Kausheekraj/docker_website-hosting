# docker_website-hosting
🚀 DevOps Task – EC2 Dockerized Flask Deployment
This repository documents my GUVI DevOps assignment where I built and deployed a Flask web application using Docker on an AWS EC2 instance. The project was developed locally in WSL Ubuntu and deployed to the cloud using Docker Compose.

📁 Project Structure
The project was organized with a clear folder structure for maintainability:
docker-project/
├── app/
│   ├── app.py
│   ├── requirements.txt
├── Dockerfile
├── docker-compose.yml



✅ Tasks Performed
- Created a Docker project folder with structured subdirectories and essential files.
- Wrote the Flask app (app.py) to serve a simple HTML page with personal and tech stack details.
- Defined dependencies in requirements.txt (Flask 2.3.2).
- Built a Dockerfile to containerize the app:
- Set working directory
- Installed dependencies
- Exposed port 5000
- Configured CMD to run the Flask app
- Created docker-compose.yml to manage container lifecycle and port mapping.
- Launched an EC2 Ubuntu instance and installed:
- Docker: sudo apt install docker.io
- Docker Compose: sudo apt install docker-compose
- Transferred project files from WSL to EC2 using scp:
scp -i credentials/docker.pem -r docker-project ubuntu@<ec2-ip>:~18.191.167.16
- SSH’ed into EC2 and verified Docker setup:
ssh -i credentials/docker.pem ubuntu@18.191.167.16
docker ps -a
- Built and ran the container using Docker Compose:
cd docker-project
sudo docker-compose up --build -d
- Configured EC2 security group to allow inbound traffic on ports 5000 and 80.
- Accessed the live app via browser:
http://18.191.167.16>



🖥️ Tech Stack
- AWS EC2 (Ubuntu 22.04 LTS)
- Docker & Docker Compose
- Flask (Python 3.10)
- WSL Ubuntu (Windows Subsystem for Linux)
- Git & GitHub

📚 References
- Docker Documentation — containerization and Compose setup
- GUVI DevOps course materials and assignment brief
- Personal notes and terminal logs from WSL Ubuntu
- Trial-and-error debugging across EC2, Docker, and Flask environments

📸 Screenshots
All terminal outputs, Docker logs, and browser screenshots confirming successful deployment are included in the repository.

📎 Submission
Submitted for GUVI DevOps EC2 + Docker Assignment. All required files, configuration scripts, and screenshots have been pushed to GitHub as per submission guidelines.
