# 绑定多个数据库


# 示例配置¶
# 下面的配置声明了三个数据库连接。特殊的默认值和另外两个分别名为 users`
# （用于用户）和 `appmeta 连接到一个提供只读访问应用内部数据的 sqlite 数据库）:
#
# SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
# SQLALCHEMY_BINDS = {
#     'users':        'mysqldb://localhost/users',
#     'appmeta':      'sqlite:////path/to/appmeta.db'
# }


# 创建和删除表
# create_all() 和 drop_all() 方法默认作用于所有声明的绑定(bind)，包括默认的。
# 这个行为可以通过提供 bind 参数来定制。它可以是单个绑定(bind)名, '__all__'
# 指向所有绑定(binds)或一个绑定(bind)名的列表。默认的绑定(bind)(SQLALCHEMY_DATABASE_URI) 名为 None:
#
# >>> db.create_all()
# >>> db.create_all(bind=['users'])
# >>> db.create_all(bind='appmeta')
# >>> db.drop_all(bind=None)


# 引用绑定(Binds)¶
# 当您声明模型时，您可以用 __bind_key__ 属性指定绑定(bind):
#
# class User(db.Model):
#     __bind_key__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
# bind key 存储在表中的 info 字典中作为 'bind_key' 键值。了解这个很重要，
# 因为当您想要直接创建一个表对象时，您会需要把它放在那:
#
# user_favorites = db.Table('user_favorites',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('message_id', db.Integer, db.ForeignKey('message.id')),
#     info={'bind_key': 'users'}
# )
# 如果您在模型上指定了 __bind_key__ ，您可以用它们准确地做您想要的。模型会自行连 接到指定的数据库连接。


# 信号支持

存在以下两个信号:

# models_committed
# 这个信号在修改的模型提交到数据库时发出。发送者是发送修改的应用，
# 模型和操作描述符以 (model, operation) 形式作为元组，这样的元组列表传递给接受者的 changes 参数。
#
# 该模型是发送到数据库的模型实例，当一个模型已经插入，操作是 'insert' ，
# 而已删除是 'delete' ，如果更新了任何列，会是 'update' 。
#
# before_models_committed
# 工作机制和 models_committed 完全一样，但是在提交之前发送。