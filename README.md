# FastAPI Blog Service 🚀

A robust, feature-rich blog service built with FastAPI, offering a complete RESTful API with authentication, database integration, and Docker support. This project demonstrates modern Python web development practices with a focus on scalability and security.

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68.1-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.23-red.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- 🔐 JWT Authentication & Authorization
- 📝 Blog Post Management
- 💬 Comments System
- 🏷️ Tag Management
- � User Profiles
- 🔄 RESTful API
- 🐳 Docker Support
- 📊 SQLAlchemy ORM
- 📱 HTML Interface
- 🔧 Environment Configuration
- 🧪 API Client Library

## 📁 Project Structure

```
├── main.py              # FastAPI application entry point
├── db.py               # Database models and configuration
├── config.py           # Application configuration
├── client.py           # API client library
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── .env               # Environment variables (not in repo)
├── .gitignore        # Git ignore rules
├── static/           # Static files
│   └── favicon.ico   # Website favicon
└── templates/        # HTML templates
    └── index.html    # Main interface
```

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- Docker (for containerized deployment)
- Git (for version control)

### Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/YourUsername/FastAPI-Blog-Service.git
cd FastAPI-Blog-Service
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create the data directory for the database:
```bash
mkdir data
```

5. Run the application locally:
```bash
python main.py
```

### 🐳 Docker Setup

1. Create the data directory for persistent storage:
```powershell
mkdir -p data
```

2. Build the Docker image:
```powershell
docker build -t blog-api .
```

3. Run the container with volume mount for persistent data:
```powershell
docker run -p 8000:8000 -v ${PWD}/data:/app/data blog-api
```

4. Test the API using the provided client:
```powershell
# In a new terminal
python client.py
```

### 🔄 Database Management

The application uses SQLite by default with the following configuration:
- Database location: `./data/mydb.db`
- Auto-migration: Tables are automatically created on startup
- Persistent storage: Database file is stored in the mounted volume when using Docker

To reset the database:
1. Stop the running container/application
2. Delete the database file:
```powershell
Remove-Item -Path .\data\mydb.db -ErrorAction SilentlyContinue
```
3. Restart the application/container

### 💻 Using the Application

1. Web Interface:
   - Open http://localhost:8000 in your browser
   - Posts are automatically loaded and refreshed every 5 seconds
   - Use the interface to register, login, and create posts

2. API Client:
   - The `client.py` script demonstrates API usage
   - Creates a user with unique credentials
   - Posts are automatically created after successful login

Example client usage:
```python
from client import BlogAPIClient

client = BlogAPIClient("http://localhost:8000")
client.register_user(
    email="user@example.com",
    username="testuser",
    password="password123",
    full_name="Test User"
)
client.login("testuser", "password123")
client.create_post(
    title="Hello World",
    content="My first blog post!",
    tags=["hello", "first-post"]
)
```

## 📚 Component Details

### 1. `main.py`
The core application file that:
- Initializes the FastAPI application
- Defines API routes and endpoints
- Implements authentication logic
- Handles request/response models
- Sets up middleware and security

Key endpoints:
- `POST /token` - Authentication
- `POST /users/` - User registration
- `GET /users/me` - Current user profile
- `POST /posts/` - Create blog posts
- `GET /posts/` - List blog posts

### 2. `db.py`
Database configuration and models using SQLAlchemy:
- User model with authentication fields
- UserProfile for extended user information
- Post model for blog entries
- Comment model for post discussions
- Tag model for post categorization
- Association tables for relationships

Models include:
```python
class User:
    - id, email, username
    - hashed_password
    - is_active, is_superuser
    - created_at, updated_at

class Post:
    - title, content
    - author_id (User relationship)
    - comments, tags
    - created_at, updated_at
```

### 3. `config.py`
Configuration management using Pydantic:
- Environment variable handling
- Database configuration
- Security settings
- API settings
- CORS configuration

### 4. `client.py`
Python client library for API interaction:
```python
client = BlogAPIClient("http://localhost:8000")
client.login("username", "password")
client.create_post("Title", "Content", ["tag1"])
```

Features:
- User registration/authentication
- Post creation and retrieval
- Error handling
- Session management

### 5. `templates/index.html`
Interactive web interface:
- User registration and login forms
- Blog post creation interface
- Post listing and viewing
- Tag management
- Bootstrap-based responsive design

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

## 🚀 Getting Started

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/OliverDolle/Local_API.git
cd Local_API
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
DATABASE_URL=sqlite:///./mydb.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run the application:
```bash
uvicorn main:app --reload
```

### 🐳 Docker Deployment

1. Build the Docker image:
```powershell
docker build -t blog-api .
```

2. Run the container (PowerShell):
```powershell
# Basic run
docker run -p 8000:8000 blog-api

# With environment variables
docker run -p 8000:8000 -e "DATABASE_URL=sqlite:///./mydb.db" -e "SECRET_KEY=your-secret-key" blog-api

# With all configuration options (using PowerShell line continuation)
docker run -p 8000:8000 `
    -e "DATABASE_URL=sqlite:///./mydb.db" `
    -e "SECRET_KEY=your-secret-key" `
    -e "ALGORITHM=HS256" `
    -e "ACCESS_TOKEN_EXPIRE_MINUTES=30" `
    blog-api
```

3. Using the PowerShell script template:
```powershell
# Copy the template
Copy-Item run-docker.ps1.template run-docker.ps1

# Edit run-docker.ps1 with your configuration
# (Update DATABASE_URL, SECRET_KEY, etc.)

# Run the script
.\run-docker.ps1
```

The template provides a starting point for your Docker configuration. For security:
1. Never commit the actual `run-docker.ps1` to version control
2. Always use unique and secure values for SECRET_KEY
3. Update DATABASE_URL according to your environment
4. The template file is safe to share as it contains no sensitive data

### 🛠️ Docker Management Commands

```powershell
# List running containers
docker ps

# Stop a container
docker stop <container-id>

# Remove a container
docker rm <container-id>

# View container logs
docker logs <container-id>

# Interactive shell in container
docker exec -it <container-id> /bin/bash

# Stop all running containers
docker stop $(docker ps -q)

# Remove all stopped containers
docker container prune
```

### 🌐 Network Access

- Local access: http://localhost:8000
- Network access: http://<your-ip>:8000
- API Documentation: http://localhost:8000/docs
- Alternative Documentation: http://localhost:8000/redoc

## 🔧 API Usage

### Using the Python Client

```python
from client import BlogAPIClient

# Initialize client
client = BlogAPIClient("http://localhost:8000")

# Register user
client.register_user(
    email="user@example.com",
    username="user1",
    password="secure_password"
)

# Login
client.login("user1", "secure_password")

# Create post
client.create_post(
    title="Hello World",
    content="My first blog post!",
    tags=["introduction", "blog"]
)
```

### Using cURL

```bash
# Login
curl -X POST http://localhost:8000/token \
  -d "username=user1&password=secure_password"

# Create post (requires token)
curl -X POST http://localhost:8000/posts/ \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  -d '{"title":"Hello","content":"World","tags":[]}'
```

## 🔒 Security Features

- JWT token authentication
- Password hashing with bcrypt
- Role-based access control
- CORS middleware
- Environment variable configuration
- Secure password storage
- SQL injection protection

## 📚 API Documentation

When the server is running, access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testing

Run the client tests:
```bash
python client.py
```

This will:
1. Register a test user
2. Authenticate
3. Create a blog post
4. Retrieve posts

## 🔄 Environment Configuration

### Environment Variables

Required variables in `.env`:
- `DATABASE_URL`: Database connection string
- `SECRET_KEY`: JWT signing key
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiry

### Database URLs

```plaintext
# SQLite (local development)
DATABASE_URL=sqlite:///./mydb.db

# PostgreSQL (production)
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

### Configuration Methods

1. Using `.env` file (local development):
```plaintext
DATABASE_URL=sqlite:///./mydb.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

2. Using PowerShell environment variables:
```powershell
$env:DATABASE_URL = "sqlite:///./mydb.db"
$env:SECRET_KEY = "your-secret-key"
$env:ALGORITHM = "HS256"
$env:ACCESS_TOKEN_EXPIRE_MINUTES = "30"
```

3. Using Docker environment variables:
```powershell
docker run -p 8000:8000 `
    -e "DATABASE_URL=sqlite:///./mydb.db" `
    -e "SECRET_KEY=your-secret-key" `
    -e "ALGORITHM=HS256" `
    -e "ACCESS_TOKEN_EXPIRE_MINUTES=30" `
    blog-api
```

### Security Considerations

- Never commit `.env` files to version control
- Use strong, unique SECRET_KEY values in production
- Use PostgreSQL in production for better scalability
- Keep environment variables secure and separate for different environments (dev/staging/prod)

## 📦 Dependencies

Core dependencies:
- FastAPI: Web framework
- SQLAlchemy: ORM
- PyJWT: Authentication
- bcrypt: Password hashing
- Pydantic: Data validation
- uvicorn: ASGI server

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI documentation
- SQLAlchemy documentation
- Python community
- Open source contributors

## 📞 Contact

- GitHub: [@OliverDolle](https://github.com/OliverDolle)