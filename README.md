🧠 AI-Based Resume Generator
This is a full-stack portfolio web application that allows users to generate professional resumes using AI. Built with Django for the back end and styled with modern responsive front-end technologies, it provides a seamless experience for users to input their data and download a personalized CV.

🌐 Website Features
🔐 User authentication system (sign up, login, profile)

🧑‍💻 AI-based resume generation (dynamic CV output)

🖼️ Profile avatar upload and push notifications

📄 PDF resume download functionality

🌙 Dark/Light mode support

🌍 Fully responsive and mobile-friendly design

🛠️ Tech Stack
Back-End:
Python

Django

Django REST Framework

PostgreSQL

JWT Authentication

Front-End:
HTML5, CSS3

TailwindCSS / Bootstrap (choose one)

JavaScript

React.js or simple templating with Django (depending on your implementation)

AI Integration:
OpenAI API (or any AI text generator model)

🚀 Getting Started
1. Clone the project
bash
Копировать
Редактировать
git clone https://github.com/your-username/ai-resume-generator.git
cd ai-resume-generator
2. Set up virtual environment
bash
Копировать
Редактировать
python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows
3. Install dependencies
bash
Копировать
Редактировать
pip install -r requirements.txt
4. Set up .env file
Create a .env file and add your settings:

env
Копировать
Редактировать
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
OPENAI_API_KEY=your_openai_api_key
5. Apply migrations and run server
bash
Копировать
Редактировать
python manage.py migrate
python manage.py runserver
📸 Screenshots
Here is a preview of the website:


📁 Folder Structure
php
Копировать
Редактировать
├── accounts/               # Custom user model and authentication
├── resume/                 # Resume generation and AI integration
├── frontend/               # Front-end templates and static files
├── media/                  # Uploaded profile pictures
├── static/                 # CSS/JS files
├── Portfolio/              # Django project root
├── manage.py
├── requirements.txt
└── README.md
📌 Future Improvements
💬 Add multilingual support

📊 Resume analytics dashboard

📬 Email the resume directly to HR

🧑 Author
Muhammad Abdulloh Kozimjonov
📧 abdullohxkozimjonov42@gmail.com
🔗 GitHub

