from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

def signupfunc(request):
    #htmlページでformに打ち込まれたデータ(POST)を受け取り、変数に代入
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Modelに登録  (引数にusername, emailaddress, password必要。emailは任意)
        #user = User.objects.create_user(username, '', password)
        
        #try:で行われた処理がerrorの場合（ユーザーがすでに重複していた場合）except:を実行する
        try:
            user = User.objects.create_user(username, '', password)
        except IntegrityError:
            return render(request, 'sns_app/signup.html', {'error': 'このユーザーはすでに登録されています'})
    return render(request, 'sns_app/list.html', )
    
def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticateで登録されているデータと合致するか確認する
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'sns_app/login.html', {'context': 'Not Logged In'})
    
    return render(request, 'sns_app/login.html', {'context': 'Get method'})

#If the user isn’t logged in, redirect to settings.LOGIN_URL
#@login_required
def listfunc(request):
    #BoardModelのデータを全て変数に入れる
    object_list = BoardModel.objects.all()
    return render(request, 'sns_app/list.html', {'object_list': object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'sns_app/detail.html', {'object':object})

def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')

def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    
    if username in object.readtext:
        return redirect('list')
    else:
        object.read += 1
        #readtext fieldsにusernameを登録する
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('list')
    
class BoardCreate(CreateView):
    template_name = 'sns_app/create.html'
    #作成したデータを保存するモデルの指定
    model = BoardModel
    #どのfieldsのデータを扱っていくかの指定
    fields = ('title', 'content', 'author', 'snsimages')
    #　= return redirect 
    success_url = reverse_lazy('list')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    