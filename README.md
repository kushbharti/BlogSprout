<h1>📝 Multi-User Blog Platform (Django)</h1>

<h3>A responsive, full-stack blog web app built with Django that supports **multi-user authentication**, **blog post creation**, **editing**, and **deletion**, along with image uploads and dynamic post rendering.</h3>

<h1>🚀 Features</h1>

- 🔐 User registration and login
- ✍️ Create, update, delete blog posts
- 🖼️ Upload images to posts
- 🧑‍🤝‍🧑 User-specific post dashboard
- 📅 Auto-generated timestamps
- 📌 Slug-based unique URLs for SEO
- 🎨 Responsive Tailwind-styled UI


🔓 Login Page
![Screenshot 2025-07-06 180059](https://github.com/user-attachments/assets/de657eb8-c63f-4a97-bf07-f601c89b1fdc) <br>

🧾 Register Page
![Screenshot 2025-07-06 180115](https://github.com/user-attachments/assets/d05db98e-f6c1-490e-81a7-247542c38496)<br>


🏠 Home Page (All Posts)

![Screenshot 2025-07-06 180358](https://github.com/user-attachments/assets/6bcb8984-ae25-484a-8d63-322a4645aa08)<br>

👤 My Posts

![Screenshot 2025-07-06 180448](https://github.com/user-attachments/assets/a5585f2e-7577-4f22-97ac-6dc6d7e9b5ec)<br>

✍️ Create Blog Post

![Screenshot 2025-07-06 180305](https://github.com/user-attachments/assets/4f7fd813-6e46-497c-844e-3523ee644391)<br>

### 🛠️ Update Blog Post

![Screenshot 2025-07-06 180516](https://github.com/user-attachments/assets/4da10411-95ad-4e5a-8145-0a816ccb6979)<br>


📁 Project Structure

MultiUser_Blog_Page/
│
├── BlogApp/                       # Django app for blog logic
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # Django forms (BlogForm)
│   ├── models.py                 # Blogpost model
│   ├── tests.py
│   ├── urls.py                   # App-level routing
│   ├── views.py                  # View functions
│   └── templates/
│       └── BlogApp/
│           ├── create_blog.html
│           ├── blog_user_post.html
│           ├── update_post.html
│           └── home.html
│
├── media/                        # Uploaded blog images
│   └── pictures/
│
├── static/                       # Static files (CSS, JS)
│   └── styles/
│       ├── blog.css
│       ├── login.css
│       └── register.css
│
├── templates/                    # Global shared templates
│   ├── base.html
│   ├── login.html
│   └── register.html
│
├── MultiUser_Blog_Page/          # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py                   # Root URLs (includes BlogApp)
│   └── wsgi.py
│
├── db.sqlite3                    # SQLite database
├── manage.py                     # Django CLI entry
├── requirements.txt              # Python package list
└── README.md                     # Project documentation



🐍 Create & Activate Virtual Environment
python -m venv env
source env/bin/activate  # For macOS/Linux
.\env\Scripts\activate   # For Windows

📦 Install Dependencies
pip install -r requirements.txt

⚙️ Run Migrations
python manage.py makemigrations
python manage.py migrate

▶️ Run the Server
python manage.py runserver

👤 Create Superuser (Optional)
python manage.py createsuperuser


