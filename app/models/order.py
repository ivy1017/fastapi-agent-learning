from sqlalchemy import Column, Integer, String, Float
from app.database import Base

""" Python 类 = 数据库表，类属性等价于表字段 """
class DouplusOrder(Base):
    __tablename__ = "douplus_orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    budget = Column(Float)
    roi = Column(Float)
    ctr = Column(Float)
    cpm = Column(Float)