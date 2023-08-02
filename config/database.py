from masoniteorm.connections import ConnectionResolver
from .settings import settings

DATABASES = {
  "default": "postgres",
  "mysql": {
    "host": "127.0.0.1",
    "driver": "mysql",
    "database": "masonite",
    "user": "root",
    "password": "",
    "port": 3306,
    "log_queries": False,
    "options": {
      #
    }
  },
  "postgres": {
    "driver": "postgres",
    "host": settings.database_host,
    "database": settings.database_name,
    "user": settings.database_user,
    "password": settings.database_password,
    "port": settings.database_port,
    # "host": "graphqlAlchem-db",
    # "driver": "postgres",
    # "database": "graphql01",
    # "user": "app_user",
    # "password": "app_pass",
    # "port": 5432,
    "log_queries": False,
    "options": {
      #
    }
  },
  "sqlite": {
    "driver": "sqlite",
    "database": "db.sqlite3",
  }
}

DB = ConnectionResolver().set_connection_details(DATABASES)