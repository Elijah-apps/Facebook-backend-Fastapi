# FastAPI Facebook Backend by Elijah Ekpen Mensah

## Overview

This FastAPI project provides a basic backend API for a Facebook-like service with support for managing users, posts, comments, likes, and friend requests.

## Setup

1. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Application**

    ```bash
    uvicorn main:app --reload
    ```

3. **Access the API**

    Visit `http://localhost:8000` to view the Swagger UI documentation.

## Endpoints

### Users

- `POST /api/users`: Create a new user
- `GET /api/users/{user_id}`: Get user details
- `PUT /api/users/{user_id}`: Update user details
- `DELETE /api/users/{user_id}`: Delete a user

### Posts

- `POST /api/posts`: Create a new post
- `GET /api/posts/{post_id}`: Get post details
- `PUT /api/posts/{post_id}`: Update post details
- `DELETE /api/posts/{post_id}`: Delete a post

### Comments

- `POST /api/comments`: Create a new comment
- `GET /api/comments/{comment_id}`: Get comment details
- `PUT /api/comments/{comment_id}`: Update comment details
- `DELETE /api/comments/{comment_id}`: Delete a comment

### Likes

- `POST /api/likes`: Like a post
- `DELETE /api/likes/{like_id}`: Remove a like

### Friend Requests

- `POST /api/friend_requests`: Send a friend request
- `GET /api/friend_requests/{request_id}`: Get friend request details
- `PUT /api/friend_requests/{request_id}`: Update friend request status
- `DELETE /api/friend_requests/{request_id}`: Cancel a friend request

Feel free to expand or modify these endpoints to suit your specific needs.
