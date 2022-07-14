from distutils.core import setup

setup(name="ch_message", # 包名
      version="1.0", # 版本
      description="itheima's 发送和接收消息模块", # 描述信息
      long_description="完整的发送和接收消息模块", # 完整描述信息
      author="昌韵", # 作者
      author_email="7671@protonmail.com", # 作者邮箱
      url="db.httpscn.cn", # 主页
      py_modules=["ch_message.send_message",
                  "ch_message.receive_message"])