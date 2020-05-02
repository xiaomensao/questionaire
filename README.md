# questionaire
# test

install restframework by running: 
`pip install djangorestframework`

To create a super admin for models:
`python manage.py createsuperuser`

install mysqlclient
`pip install mysqlclient`

Everytime you make change to models(database table),run following commands:
`python manage.py makemigrations`
`python manage.py migrate`

create database and make mysql work with utf-8
`CREATE SCHEMA `questionaire` DEFAULT CHARACTER SET utf8 ;`

QuestionType:
1 - 文本
2 - 单选
3 - 多选
4 - 多选选项

questionaire status:
1 - 编辑
2 - 发布
3 - 关闭
