import strawberry
from app.schemas import UserType, PostType, CommentType
from .controller import CreateMutation, Queries
from typing import List


print('mutation', CreateMutation)

@strawberry.type
class Mutation:
    add_user: UserType = strawberry.mutation(resolver=CreateMutation.add_user)
    add_post: PostType = strawberry.mutation(resolver=CreateMutation.add_post)
    add_comment: CommentType = strawberry.mutation(resolver=CreateMutation.add_comment)

@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=Queries.get_all_users)