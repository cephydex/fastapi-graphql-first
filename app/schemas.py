import strawberry
from typing import List, Optional

@strawberry.type
class CommentType:
    id: int
    user_id: int
    post_id: int
    body: str

@strawberry.type
class PostType:
    id: int
    user_id: int
    title: str
    body: str
    comments: Optional[List[CommentType]]

@strawberry.type
class UserType:
    id: int
    name: str
    email: str
    address: str
    phone_number: str
    sex: str
    posts: Optional[List[PostType]]
    comments: Optional[List[CommentType]]


@strawberry.input
class UserInput:
    name: str
    email: str
    address: str
    phone_number: str
    sex: str

@strawberry.input
class PostsInput:
    user_id: int
    title: str
    body: str

@strawberry.input
class CommentsInput:
    user_id: int
    post_id: int
    body: str
