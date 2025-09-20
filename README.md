
# 🌊 PUDDLE

A modern **Django-based web application** built for modularity, scalability, and ease of use.  
PUDDLE provides the backbone for platforms featuring conversations, dashboards, item listings, and media uploads — all out of the box.

---

## 🚀 Features

- 🛠 **Modular Apps** – Core apps like `conversation`, `item`, `dashboard` are cleanly separated.
- 💾 **SQLite Database** – Quick start with zero setup, easily switchable to Postgres or MySQL.
- 🖼 **Media Management** – Built-in media handling for uploads.
- 🔐 **Django Admin Ready** – Full power of Django admin panel for management.
- ⚡ **Scalable Architecture** – Easy to extend with additional apps or APIs.

---

## 🗂 Project Structure

```bash
PUDDLE/
├── conversation/   # Messaging & chat between users
├── core/           # Core utilities and base templates
├── dashboard/      # Admin/user dashboards
├── item/           # Items or listings management
├── puddle/         # Django settings, URLs, WSGI, ASGI
├── media/          # Uploaded media files
├── db.sqlite3      # Default database
└── manage.py       # Django project manager
````

---

## ⚙️ Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/yourusername/PUDDLE.git
cd PUDDLE
python -m venv env
source env/bin/activate   # On Linux/Mac
env\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 📝 Configuration

You can configure environment variables by creating a `.env` file:

```env
DEBUG=True
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## 🤝 Contributing

Pull requests are welcome!
Please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---


