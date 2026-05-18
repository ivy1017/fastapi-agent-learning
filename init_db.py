from sqlalchemy.orm import Session

from app.database import engine
from app.models.order import DouplusOrder
from app.database import Base

Base.metadata.create_all(bind=engine)

db = Session(bind=engine)

""" 插入模拟 dou+ 数据 """
sample_orders = [
    DouplusOrder(
        user_id="1001",
        budget=500,
        roi=2.8,
        ctr=4.6,
        cpm=31
    ),
    DouplusOrder(
        user_id="1002",
        budget=1200,
        roi=1.9,
        ctr=2.7,
        cpm=45
    )
]

db.add_all(sample_orders)
db.commit()

print("数据库初始化完成")