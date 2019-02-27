from django.shortcuts import render, redirect, HttpResponse
from .models import User, Message, Comment
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, "wall/index.html")

def registration_process(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    else:
        hash_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create( name=request.POST['name'], 
                                        alias=request.POST['alias'], 
                                        email=request.POST['email'], 
                                        password=hash_password.decode())
        request.session["user_id"] = new_user.id
        request.session["username"] = new_user.alias
        return redirect("/wall")

def login_process(request):
    # if request.method=='post'

    errors =User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        logged_in_user = User.objects.get(email=request.POST["login_email"])
        request.session["user_id"] = logged_in_user.id
        request.session["username"] = logged_in_user.alias
        return redirect('/wall')

def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'logInInfo' : User.objects.get(id = request.session['user_id']),
        'messageList' : Message.objects.all(),
        'CommentList' : Comment.objects.all()
    }
    return render(request, 'wall/welcome.html', context)

def post_message(request):
    user= User.objects.get(id=request.session['user_id'])
    Message.objects.create( message=request.POST['message'], 
                            poster=user)
    return redirect('/wall')

def post_comment(request):
    user = User.objects.get(id= request.session['user_id'])
    message_id = request.POST['mesID']
    message=Message.objects.get(id=message_id)
    Comment.objects.create( opinions = request.POST['comment'], 
                            poster=user, 
                            message=message)
    return redirect('/wall')

def log_off(request):
    request.session.flush()
    return redirect('/')