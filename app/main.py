from fastapi import FastAPI, Depends
from app.config_ck.settings import settings
from starlette.middleware.cors import CORSMiddleware
import strawberry
# from strawbery import St
from strawberry.fastapi import GraphQLRouter
from app.core import Mutation, Query
import json

def create_app():
    app = FastAPI(title=settings.app_name, 
                    version=settings.app_version
                )
    
    # handle CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_credentials=True,
        allow_headers=["*"],
    )
    
    return app

# init app
app = create_app()
# app.include_router(consumer_router)

@app.get('/')
def app_index():
    return {"server": "I'm alive"}

@app.get('/ping')
def ping():
    return {"message": "pong"}

# @strawberry.type
# class Query:

#     @strawberry.field
#     def hello(self) -> str:
#         return "hello world"
  
schema = strawberry.Schema(
            query=Query, 
            mutation=Mutation,
            # config=StrawberryConfig(auto_camel_case=True)
        )
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix='/graphql')

# @app.on_event("startup")
# async def startup():
#     await get_db.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await get_db.disconnect()


