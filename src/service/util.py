from uuid import uuid4
import decimal, datetime
from sqlalchemy.engine.result import Result 

def generate_uuid() -> str:
    return str(uuid4()).replace("-" , "")

def fetch_result(result:Result):
    columns = result.keys()
    return [dict(zip(columns, row)) for row in result.fetchall()]