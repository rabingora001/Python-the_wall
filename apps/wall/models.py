from django.db import models

# Create your models here.
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):

    def reg_validator(self, postData):
        errors={}
        #name errors
        if len(postData["name"]) < 1:
            errors["name_error"] = "Please enter name!"
        elif len(postData["name"]) < 2:
            errors["name_error"] ="please enter valid name!"
        elif not re.compile(r'^[a-zA-Z]{2,}$').match(postData["name"]):
            errors["name_error"] = "Name should have letters only (not numbers or special characters)!"

        #Alias errors
        if len(postData["alias"]) < 2:
            errors["alias_error"] = "please enter a valid alias"
        
        #email errors
        if len(postData["email"]) < 1:
            errors["email_error"] = "Email cannot be blank!"
        elif not re.compile(r'^[a-zA-Z0-9+-_]+@[a-zA-Z0-9+-_]+.[a-zA-Z0-9+-_]$').match(postData["email"]):
            errors["email_error"] = "Please enter vaild email form (eg. abc123@gmail.com)!"
        #email already exits errors
        elif len(User.objects.filter(email=postData["email"])) > 0:
            errors["dublicate_email"] = "Email already exits. Please use new email!"

        #password errors
        if len(postData["password"]) < 3:
            errors["password_error"] ="password needs to be more than 3 characters!"
        elif postData["password"] != postData["confirm_password"]:
            errors["password_error"] = "password did not match!"

        return errors
    
    def login_validator(self, postDATA):
        existing = User.objects.filter(email=postDATA["login_email"])
        errors={}
        #check if the email already exists
        if len(existing)==0:
            errors["one"]="Email is not register. Please register ar first!"
        #check if the password is correct
        elif not bcrypt.checkpw(postDATA["login_password"].encode(), existing[0].password.encode()):
            errors["two"] = "password is not correct!"
        
        return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at =models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now =True)
    #messages
    #comments
    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    poster = models.ForeignKey(User, related_name ='messages')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    #comments

class Comment(models.Model):
    opinions = models.TextField()
    poster = models.ForeignKey(User, related_name='comments')
    message = models.ForeignKey(Message, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


