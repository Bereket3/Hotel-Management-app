# Hotel Booking and Review Web App

This project aims to digitalize the hotel booking and reviewing experience, making it easier for users to book rooms, review hotels, and request services.

## Description

The Hotel Booking and Review Web App is a full-featured solution designed to allow users to browse hotels, book rooms, review their experience, and request hotel services. Hotel administrators can register their hotels, staff, rooms, and services, streamlining operations and guest experiences.

### Features

1. Hotel Registration: Register hotels with room details, staff information, and available services.
2. User Authentication: Secure user login and registration system.
3. Room Booking System: Users can search for available rooms and book based on their preferences.
4. Review and Rating: Guests can leave reviews and rate their hotel experience.
5. Service Request: Users can request room service and other hotel services from the app.
6. Staff Management: Hotels can manage their staff profiles and assign roles.
7. Room and Service Management: Hotels can manage rooms and services offered to the guests.
8. Analytics and Reporting: Generate reports on bookings, reviews, and staff performance.

## Getting Started

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

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE.md file for details.
