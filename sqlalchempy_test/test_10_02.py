# 生成models
#
#
# 方法一： 自己根据SQLAlchemy的docs写model，比如一对多，多对一等复杂的表模型。(SQLAlchemy的文档非常详细，就跟天书一样，真心懒得看。还是flask-sqlalchemy的文档简洁明了，可以参考的)
# 方法二： 使用sqlacodegen从数据库逆向出models.py

# 对应的models.py



# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root:123456@localhost/webpy')

#比较好的习惯是现实销毁引擎，会有助于python的垃圾回收
engine.dispose()


# 创建对象的基类:
Base = declarative_base()
base=declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'userll'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 查询记录

#connect
connection = engine.connect()
result = connection.execute("select username from users")
for row in result:
    print("username:", row['username'])
connection.close()

# Session:

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
session.close()


#更改记录
# 基本思路是先filter到需要的行集合，再修改里面的值。这里有4种方式：

#
# 1) user.no_of_logins += 1
#    session.commit()
#
# 2) session.query().\
#        filter(User.username == form.username.data).\
#        update({"no_of_logins": (User.no_of_logins +1)})
#    session.commit()
#
# 3) conn = engine.connect()
#    stmt = User.update().\
#        values(User.no_of_logins = (User.no_of_logins + 1)).\
#        where(User.username == form.username.data)
#    conn.execute(stmt)
#
# 4) setattr(user, 'no_of_logins', user.no_of_logins+1)
#    session.commit()



