from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>Kausheek's DevOps Task</title></head>
        <body style='font-family:sans-serif; text-align:center; padding-top:50px;'>
            <h1>Hello from EC2!</h1>
            <p><strong>Name:</strong> Kausheek</p>
            <p><strong>Tech Stack:</strong> AWS EC2, Docker</p>
            <p><strong>Course:</strong> Online DevOps Training</p>
        </body>
    </html>
    """
