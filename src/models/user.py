from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from src.config.db import meta, engine

users = Table("users", meta, Column("id", String(255), primary_key=True), 
              Column("name", String(255)), Column("email", String(255)))

meta.create_all(engine)