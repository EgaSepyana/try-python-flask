from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column , relationship
from sqlalchemy import String , BigInteger , Boolean , Enum , ForeignKey , Text , Integer
from typing import List
from pydantic import BaseModel
from typing import Optional

class Base(DeclarativeBase):
    pass

class Request(BaseModel):
    page : Optional[int] = 1
    size : Optional[int] = 10
    order : Optional[str] = 'asc'
    order : Optional[str] = 'createdAt'