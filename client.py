import requests
import json
from typing import Optional, List, Dict
from datetime import datetime

class BlogAPIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.token: Optional[str] = None

    def register_user(self, email: str, username: str, password: str, full_name: Optional[str] = None) -> Dict:
        """Register a new user"""
        endpoint = f"{self.base_url}/users/"
        data = {
            "email": email,
            "username": username,
            "password": password,
            "full_name": full_name
        }
        response = requests.post(endpoint, json=data)
        return self._handle_response(response)

    def login(self, username: str, password: str) -> bool:
        """Login and get access token"""
        endpoint = f"{self.base_url}/token"
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(endpoint, data=data)  # Note: using form data, not JSON
        if response.status_code == 200:
            self.token = response.json()["access_token"]
            return True
        return False

    def create_post(self, title: str, content: str, tags: List[str] = None) -> Dict:
        """Create a new blog post"""
        if not self.token:
            raise ValueError("You must login first")

        endpoint = f"{self.base_url}/posts/"
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {
            "title": title,
            "content": content,
            "tags": tags or []
        }
        response = requests.post(endpoint, json=data, headers=headers)
        return self._handle_response(response)

    def get_posts(self) -> List[Dict]:
        """Get all posts"""
        if not self.token:
            raise ValueError("You must login first")

        endpoint = f"{self.base_url}/posts/"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(endpoint, headers=headers)
        return self._handle_response(response)

    def get_user_profile(self) -> Dict:
        """Get current user's profile"""
        if not self.token:
            raise ValueError("You must login first")

        endpoint = f"{self.base_url}/users/me"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(endpoint, headers=headers)
        return self._handle_response(response)

    def _handle_response(self, response: requests.Response) -> Dict:
        """Handle API response and errors"""
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            print(f"Response: {response.text}")
            raise
        except json.JSONDecodeError:
            print(f"Invalid JSON response: {response.text}")
            raise

def main():
    # Create API client
    client = BlogAPIClient("http://localhost:8000")

    try:
        # Register a new user
        print("Registering new user...")
        user = client.register_user(
            email="test@example.com",
            username="testuser",
            password="testpassword123",
            full_name="Test User"
        )
        print(f"Registered user: {user}")

        # Login
        print("\nLogging in...")
        if client.login("testuser", "testpassword123"):
            print("Login successful!")
        else:
            print("Login failed!")
            return

        # Get user profile
        print("\nGetting user profile...")
        profile = client.get_user_profile()
        print(f"User profile: {profile}")

        # Create a post
        print("\nCreating a blog post...")
        post = client.create_post(
            title="My First Blog Post",
            content="This is a test post created via the API client!",
            tags=["test", "first-post"]
        )
        print(f"Created post: {post}")

        # Get all posts
        print("\nGetting all posts...")
        posts = client.get_posts()
        print(f"Found {len(posts)} posts:")
        for post in posts:
            print(f"- {post['title']}")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()