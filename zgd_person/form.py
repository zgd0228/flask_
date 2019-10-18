#!/user/bin/env python
# -*- conding:utf-8 -*-
# Author:zgd
from wtforms import Form,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Length,DataRequired
class LoginForm(Form):
    username = StringField('user',validators=[DataRequired(message='输入不能为空')])
    password = PasswordField('pwd',validators=[DataRequired(),Length(min=8)])
    remember = BooleanField("remember")
    login = SubmitField('login')
