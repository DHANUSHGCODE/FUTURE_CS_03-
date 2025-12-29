File Share – Secure File Sharing System

## Internship Information
- **Organization:** Future Interns  
- **Domain:** Cyber Security  
- **Task:** 03 – Secure File Sharing System  
- **Intern Name:** Dhanush G  

---

## Project Overview
**File Share** is a secure web-based file sharing application designed to demonstrate
core cybersecurity principles such as **data confidentiality**, **secure file handling**,
and **encryption at rest**.  
The application encrypts uploaded files using **AES symmetric encryption** before
storing them on the server, ensuring that sensitive data remains protected from
unauthorized access.

---

## Objectives
- To understand and implement **AES encryption**
- To securely handle file uploads in a web application
- To demonstrate secure storage of files at rest
- To gain hands-on experience with **Flask-based web security**

---

## Technologies & Tools
- **Programming Language:** Python  
- **Web Framework:** Flask  
- **Encryption Algorithm:** AES (PyCryptodome)  
- **Frontend:** HTML, CSS  
- **Development Environment:** Windows  

---

## Key Features
- Secure file upload mechanism  
- AES-based encryption for files before storage  
- Encrypted files are unreadable without the encryption key  
- Clean, interactive, and user-friendly interface  
- Beginner-friendly yet security-focused implementation  

---

## Project Structure
FUTURE_CS_03/
├── app.py
├── requirements.txt
├── README.md
├── Security_Overview.docx
├── templates/
│ └── upload.html
├── screenshots/
│ └── *.png

yaml
Copy code

---

## How the Application Works
1. The user selects a file through the web interface.
2. The file is uploaded to the Flask server.
3. Before storage, the file is encrypted using AES encryption.
4. The encrypted file is securely stored on the server.
5. The original file content remains protected and unreadable.

---

## How to Run the Project
1. Install Python on your system  
2. Install required dependencies:
pip install flask pycryptodome

markdown
Copy code
3. Run the application:
python app.py

css
Copy code
4. Open a browser and visit:
http://127.0.0.1:5000

yaml
Copy code

---

## Security Considerations
- Files are encrypted before being stored on disk.
- Encryption keys are managed server-side.
- This project is intended for **educational and demonstration purposes**.

---

## Learning Outcomes
- Practical understanding of AES encryption
- Secure file handling in web applications
- Basics of Flask application development
- Introduction to real-world cybersecurity concepts

---

## Disclaimer
This project is developed as part of an internship task and is intended
for learning and demonstration purposes only. It is not designed for
production use.
