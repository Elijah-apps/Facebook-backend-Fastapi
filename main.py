from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data models
class User(BaseModel):
    id: str
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Post(BaseModel):
    id: str
    user_id: str
    content: str

class PostUpdate(BaseModel):
    content: Optional[str] = None

class Comment(BaseModel):
    id: str
    post_id: str
    user_id: str
    content: str

class CommentUpdate(BaseModel):
    content: Optional[str] = None

class Like(BaseModel):
    id: str
    post_id: str
    user_id: str

class FriendRequest(BaseModel):
    id: str
    from_user_id: str
    to_user_id: str
    status: str

class FriendRequestUpdate(BaseModel):
    status: Optional[str] = None

# Example data stores
users = []
posts = []
comments = []
likes = []
friend_requests = []

@app.post("/api/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/api/users/{user_id}", response_model=User)
def get_user(user_id: str = Path(..., title="The ID of the user to get")):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/users/{user_id}", response_model=User)
def update_user(user_id: str, user_update: UserUpdate):
    for user in users:
        if user.id == user_id:
            if user_update.name is not None:
                user.name = user_update.name
            if user_update.email is not None:
                user.email = user_update.email
            if user_update.password is not None:
                user.password = user_update.password
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/users/{user_id}")
def delete_user(user_id: str):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/api/posts", response_model=Post)
def create_post(post: Post):
    posts.append(post)
    return post

@app.get("/api/posts/{post_id}", response_model=Post)
def get_post(post_id: str = Path(..., title="The ID of the post to get")):
    for post in posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.put("/api/posts/{post_id}", response_model=Post)
def update_post(post_id: str, post_update: PostUpdate):
    for post in posts:
        if post.id == post_id:
            if post_update.content is not None:
                post.content = post_update.content
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/api/posts/{post_id}")
def delete_post(post_id: str):
    for post in posts:
        if post.id == post_id:
            posts.remove(post)
            return {"detail": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/api/comments", response_model=Comment)
def create_comment(comment: Comment):
    comments.append(comment)
    return comment

@app.get("/api/comments/{comment_id}", response_model=Comment)
def get_comment(comment_id: str = Path(..., title="The ID of the comment to get")):
    for comment in comments:
        if comment.id == comment_id:
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@app.put("/api/comments/{comment_id}", response_model=Comment)
def update_comment(comment_id: str, comment_update: CommentUpdate):
    for comment in comments:
        if comment.id == comment_id:
            if comment_update.content is not None:
                comment.content = comment_update.content
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@app.delete("/api/comments/{comment_id}")
def delete_comment(comment_id: str):
    for comment in comments:
        if comment.id == comment_id:
            comments.remove(comment)
            return {"detail": "Comment deleted"}
    raise HTTPException(status_code=404, detail="Comment not found")

@app.post("/api/likes", response_model=Like)
def create_like(like: Like):
    likes.append(like)
    return like

@app.delete("/api/likes/{like_id}")
def delete_like(like_id: str):
    for like in likes:
        if like.id == like_id:
            likes.remove(like)
            return {"detail": "Like deleted"}
    raise HTTPException(status_code=404, detail="Like not found")

@app.post("/api/friend_requests", response_model=FriendRequest)
def create_friend_request(friend_request: FriendRequest):
    friend_requests.append(friend_request)
    return friend_request

@app.get("/api/friend_requests/{request_id}", response_model=FriendRequest)
def get_friend_request(request_id: str = Path(..., title="The ID of the friend request to get")):
    for friend_request in friend_requests:
        if friend_request.id == request_id:
            return friend_request
    raise HTTPException(status_code=404, detail="Friend request not found")

@app.put("/api/friend_requests/{request_id}", response_model=FriendRequest)
def update_friend_request(request_id: str, friend_request_update: FriendRequestUpdate):
    for friend_request in friend_requests:
        if friend_request.id == request_id:
            if friend_request_update.status is not None:
                friend_request.status = friend_request_update.status
            return friend_request
    raise HTTPException(status_code=404, detail="Friend request not found")

@app.delete("/api/friend_requests/{request_id}")
def delete_friend_request(request_id: str):
    for friend_request in friend_requests:
        if friend_request.id == request_id:
            friend_requests.remove(friend_request)
            return {"detail": "Friend request deleted"}
    raise HTTPException(status_code=404, detail="Friend request not found")
