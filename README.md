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


<h3>🔓 Login Page</h3>

![Screenshot 2025-07-06 180059](https://github.com/user-attachments/assets/6263d707-e992-4994-b6e2-e43af08257ad) <br>

<h3>🧾 Register Page</h3>

![Screenshot 2025-07-06 180115](https://github.com/user-attachments/assets/e5b6de38-491c-415d-ae44-c4109f7d4a7f)<br>

<h3>🏠 Home Page (All Posts)</h3>

![Screenshot 2025-07-06 180358](https://github.com/user-attachments/assets/a323ed52-d5b6-43c6-9930-e5d1d2f19b8c)<br>

<h3>👤 My Posts</h3>

![Screenshot 2025-07-06 180530](https://github.com/user-attachments/assets/1da6f51b-baf6-4c54-b55f-3854127ca2ef)<br>

<h3>✍️ Create Blog Post</h3>

![Screenshot 2025-07-06 180305](https://github.com/user-attachments/assets/acd9a4ea-d39f-4879-a6a5-b6e37ce49ae1)<br>

<h3>🛠️ Update Blog Post</h3>

![Screenshot 2025-07-06 180516](https://github.com/user-attachments/assets/37c2197a-e233-49f0-b96a-a44b4084ac95)<br>

<h1>📁 Project Structure</h1>

MultiUser_Blog_Page/          <br>
│                            <br>                
├── BlogApp/                       # Django app for blog logic   <br>
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



<h3>🐍 Create & Activate Virtual Environment</h3>
python -m venv env  <br>
source env/bin/activate  # For macOS/Linux <br>
.\env\Scripts\activate   # For Windows    <br>

<h3>📦 Install Dependencies </h3>
pip install -r requirements.txt

<h3>⚙️ Run Migrations</h3>
python manage.py makemigrations
python manage.py migrate

<h3>▶️ Run the Server</h3>
python manage.py runserver

<h3>👤 Create Superuser (Optional)</h3>
python manage.py createsuperuser


