from .model import Base
from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import String , BigInteger , Boolean , Enum , ForeignKey , Text , Integer , Numeric

class ReqProduct(BaseModel):
    id : Optional[str] = ''
    name : str
    price : Optional[float] = 0
    qty : Optional[int] = 0
    desc : Optional[str] = ''
    createdAt : Optional[int] = 0
    updatedAt : Optional[int] = 0

class Product(Base):
    __tablename__ = 'products'

    id:Mapped[str] = mapped_column(String(100) , primary_key=True)
    name:Mapped[str] = mapped_column(Text , name='name')
    price:Mapped[float] = mapped_column(Numeric , name='price')
    qty:Mapped[int] = mapped_column(Integer , name='qty')
    desc:Mapped[str] = mapped_column(Text , name='description')
    createdAt:Mapped[int] = mapped_column(Integer , name='created_at')
    updatedAt:Mapped[int] = mapped_column(Integer , name='updated_at')