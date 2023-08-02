import strawberry
from .models.User import User
from .models.Post import Post
from .models.Comment import Comment
from .schemas import UserType, PostType
from typing import List

from .schemas import UserInput, PostsInput, CommentsInput

class CreateMutation:

    # def add_user(self, user_data: UserType):
    def add_user(self, user_data: UserInput):
        user = User.where("email", user_data.email).get()

        if user:
            raise Exception("User already exists")
        
        user = User()
        user.name = user_data.name
        user.address = user_data.address
        user.email = user_data.email
        user.phone_number = user_data.phone_number
        user.sex = user_data.sex
        user.save()

        return user
    
    def add_post(self, req_data: PostsInput):
        user = User.find(req_data.user_id)

        if not user:
            raise Exception("User not found")
        
        post = Post()
        post.title = req_data.title
        post.body = req_data.body
        post.user_id = req_data.user_id
        post.save()

        user.attach("posts", post)
        return post
    
    def add_comment(self, req_data: CommentsInput):
        post = Post.find(req_data.post_id)
        if not post:
            raise Exception("Post not found")
        
        user = User.find(req_data.user_id)
        if not user:
            raise Exception("User not found")
        
        comment = Comment()
        comment.body = req_data.body
        comment.post_id = req_data.post_id
        comment.user_id = req_data.user_id
        comment.save()

        user.attach("comments", comment)
        post.attach("comments", comment)

        return comment
    
class Queries:
     def get_all_users(self) -> List[UserType]:
        return User.all()