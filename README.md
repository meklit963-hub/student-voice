# Student Voice

Student Voice is a mobile-first feedback system for students, departments, and student affairs teams. The app lets students submit academic, facility, and service feedback, including optional anonymous reports and image attachments, while staff users can review and update feedback status.

## Features

- Student feedback submission with category and routing fields.
- Optional anonymous feedback handling.
- Image attachment support from the mobile app.
- Role-aware dashboards for students, departments, student affairs, and admins.
- Notification and feedback APIs served by the Django backend.

## Tech Stack

- Mobile: Expo, React Native, React Navigation
- Backend: Django, Django REST Framework
- Database: SQLite for local development
- API configuration: `EXPO_PUBLIC_API_BASE_URL` for mobile-to-backend routing

## Repository Structure

```text
backend/
  apps/
    accounts/        # Custom user model, auth views, serializers
    departments/     # Department-related backend API code
    feedback/        # Feedback model, serializers, views, services
    notifications/   # Notification model, serializers, views, services
  config/            # Django project settings and URL routing
  manage.py

mobile/
  src/
    api/             # Shared API client helpers
    components/      # Reusable mobile layout components
    navigation/      # Main app navigation
    screens/         # Role-specific screens and dashboards
    utils/           # Collaboration and review matrices
```

## Local Development

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
python manage.py migrate
python manage.py runserver
```

The backend serves API routes under `/api/`.

### Mobile

```bash
cd mobile
npm install
npm start
```

By default, the mobile API client points Android emulators to `http://10.0.2.2:8000/api` and iOS/web to `http://localhost:8000/api`. Override this when testing on a physical device:

```bash
set EXPO_PUBLIC_API_BASE_URL=http://YOUR-LAN-IP:8000/api
npm start
```

## Notes For Contributors

- Keep backend role logic close to serializers, permissions, and viewsets so access rules are easy to audit.
- Prefer service helpers for reusable database workflows that should stay outside view classes.
- Keep mobile API behavior centralized in `mobile/src/api/api.js` instead of duplicating fetch logic in screens.
- Avoid behavior-changing pull requests unless the affected role workflow has been tested end to end.
