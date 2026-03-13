# ShareJet

A Django-based file sharing web application with real-time transfer capabilities.

## Features

- User authentication (register/login)
- File upload and download
- Clipboard sharing
- Real-time file transfers using WebSockets
- Dashboard with transfer history

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Real-time**: Django Channels (WebSockets)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ShareJet.git
cd ShareJet
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

- `accounts/` - User authentication
- `files/` - File handling and downloads
- `transfers/` - Real-time transfer logic
- `core/` - Core application views
- `analytics/` - Transfer analytics
- `ShareJet/` - Django project settings
- `templates/` - HTML templates

## License

MIT
