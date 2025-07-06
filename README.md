<h1>📝 Multi-User Blog Platform (Django)</h1>

<h4>A responsive, full-stack blog web app built with Django that supports **multi-user authentication**, **blog post creation**, **editing**, and **deletion**, along with image uploads and dynamic post rendering.</h4>

<h1>🚀 Features</h1>

- 🔐 User registration and login
- ✍️ Create, update, delete blog posts
- 🖼️ Upload images to posts
- 🧑‍🤝‍🧑 User-specific post dashboard
- 📅 Auto-generated timestamps
- 📌 Slug-based unique URLs for SEO
- 🎨 Responsive Tailwind-styled UI


#🔓 Login Page
![Screenshot 2025-07-06 180059](https://github.com/user-attachments/assets/6263d707-e992-4994-b6e2-e43af08257ad) <br>

#🧾 Register Page
![Screenshot 2025-07-06 180115](https://github.com/user-attachments/assets/e5b6de38-491c-415d-ae44-c4109f7d4a7f)<br>

#🏠 Home Page (All Posts)
![Screenshot 2025-07-06 180358](https://github.com/user-attachments/assets/a323ed52-d5b6-43c6-9930-e5d1d2f19b8c)<br>

#👤 My Posts
![Screenshot 2025-07-06 180530](https://github.com/user-attachments/assets/1da6f51b-baf6-4c54-b55f-3854127ca2ef)<br>

#✍️ Create Blog Post
![Screenshot 2025-07-06 180305](https://github.com/user-attachments/assets/acd9a4ea-d39f-4879-a6a5-b6e37ce49ae1)<br>

#🛠️ Update Blog Post
![Screenshot 2025-07-06 180516](https://github.com/user-attachments/assets/37c2197a-e233-49f0-b96a-a44b4084ac95)<br>

<h1>📁 Project Structure</h1>

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



<h1>🐍 Create & Activate Virtual Environment</h1>
python -m venv env
source env/bin/activate  # For macOS/Linux
.\env\Scripts\activate   # For Windows

<h1>📦 Install Dependencies </h1>
pip install -r requirements.txt

<h1>⚙️ Run Migrations</h1>
python manage.py makemigrations
python manage.py migrate

<h1>▶️ Run the Server</h1>
python manage.py runserver

<h1>👤 Create Superuser (Optional)</h1>
python manage.py createsuperuser


