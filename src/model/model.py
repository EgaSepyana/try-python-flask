from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column , relationship
from sqlalchemy import String , BigInteger , Boolean , Enum , ForeignKey , Text , Integer
from typing import List

class Base(DeclarativeBase):
    pass