# Advanced FastAPI Blog Service

A feature-rich blog API service built with FastAPI, SQLAlchemy, and modern Python practices. This service can be run both locally and deployed to production environments.

## Features

- 🔐 JWT Authentication
- 👤 User Management
- 📝 Blog Posts with Comments
- 🏷️ Tag System
- 📊 User Profiles
- 🌐 Multi-environment Support (Local/Production)
- 📚 Comprehensive API Documentation
- 🔒 Role-based Access Control

## Prerequisites

- Python 3.8+
- PostgreSQL (for production) or SQLite (for local development)
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <your-repo-name>
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

4. Set up environment variables:
Create a `.env` file in the root directory with the following content:
```env
DATABASE_URL=sqlite:///./mydb.db  # For local development
# DATABASE_URL=postgresql://user:password@localhost/dbname  # For PostgreSQL
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

### Local Development
```bash
uvicorn main:app --reload
```

### Production
```bash
uvicorn main:app --host 0.0.0.0 --port 80
```

The API will be available at `http://localhost:8000` (development) or your production URL.

## API Documentation

Once the application is running, you can access:
- Interactive API documentation: `/docs`
- Alternative API documentation: `/redoc`

## API Endpoints

### Authentication
- POST `/auth/token` - Get access token
- POST `/auth/refresh` - Refresh access token

### Users
- POST `/users/` - Create new user
- GET `/users/me` - Get current user
- PUT `/users/me` - Update current user
- GET `/users/{user_id}` - Get user by ID

### Posts
- POST `/posts/` - Create new post
- GET `/posts/` - List all posts
- GET `/posts/{post_id}` - Get post by ID
- PUT `/posts/{post_id}` - Update post
- DELETE `/posts/{post_id}` - Delete post

### Comments
- POST `/posts/{post_id}/comments/` - Add comment
- GET `/posts/{post_id}/comments/` - List comments
- DELETE `/comments/{comment_id}` - Delete comment

### Tags
- POST `/tags/` - Create tag
- GET `/tags/` - List all tags
- GET `/posts/tag/{tag_name}` - Get posts by tag

## Database Schema

The application uses SQLAlchemy ORM with the following main models:
- User
- UserProfile
- Post
- Comment
- Tag
- PostTag (Association table)

## Security

- Password hashing using bcrypt
- JWT token authentication
- Role-based access control
- CORS middleware
- SQL injection protection through SQLAlchemy

## Deployment

### Docker
```dockerfile
# Dockerfile included in repository
docker build -t blog-api .
docker run -p 80:80 blog-api
```

### Traditional Deployment
1. Set up a PostgreSQL database
2. Configure environment variables
3. Install dependencies
4. Run with a production ASGI server (e.g., uvicorn, gunicorn)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.