## How To Run The Back end

### Dependencies

- Python interpreter (v3.x)
- Django (v4.x or higher)
- Database (SQLite, PostgreSQL, etc.)
- Any modern web browser

### Installing

1. Clone the project with:
```
git clone https://github.com/your-username/hotel-booking-app.git
```
2. Navigate to the project directory:
```
cd Hotel-Management-App
```
3. Create and activate a virtual environment:
```
# on cmd
python -m venv venv && venv\Scripts\activate.bat 
# on powershell
python -m venv venv && venv\Scripts\Activate.ps1
# on bash
python -m venv venv && .venv\Scripts\activate
```
4. Install dependencies:
```
pip Install -r requirements.txt
```
5. Apply database migrations:
```
python manage.py migrate
```
6. Run the development server:
```
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000` in your browser to view the app.

