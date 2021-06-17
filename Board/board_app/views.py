from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    boards = {'boards': sil_Board.objects.all()}
    return render(request, 'siljong_list.html', boards)

def sil_post(request):
    if request.method == "POST":
        title = request.POST['title']
        petimage = request.FILES['petimage']
        petname = request.POST['petname']
        petage = request.POST['petage']
        petkind = request.POST['petkind']
        pettype = request.POST['pettype']
        character = request.POST['character']
        whereCD = request.POST.get('h_area1')
        whereCGG = request.POST.get('h_area2')
        date = request.POST['date']
        money = request.POST['money']
        body = request.POST['content']
        user = request.user
        board = sil_Board(title=title, petimage=petimage, petname=petname, petage=petage, petkind=petkind, pettype=pettype, character=character, whereCD=whereCD, whereCGG=whereCGG,
                      date=date, money=money, body=body, user=user)
        board.save()
        HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'siljong_write.html')

def posting(request, pk):
    board = sil_Board.objects.get(pk=pk)
    #comments = Comment.objects.filter(cpost = pk)
   # if request.method == "POST":
       # comment = Comment()
       # comment.cpost = board
       # comment.cuser = request.user
       # comment.comment = request.POST['content']
       # comment.save()
    return render(request, 'detail.html', {'board':board})

@login_required
def comment_new(request, post_pk):
    cpost=get_object_or_404(sil_Board, pk = post_pk)
    if request.method =='POST':

        comment=request.POST.get('content')
        cuser = request.user
        comment=Comment(cpost=cpost, cuser=cuser, comment=comment)
        comment.save()

        #Comment.objects.create(cpost=cpost, cuser=cuser, comment=comment)
        return redirect('/post/'+str(cpost.pk))

def boardDelete(request, pk):
    board = sil_Board.objects.get(pk=pk)
    board.delete()
    return redirect('board')




# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        # password와 confirm에 입력된 값이 같다면
        if request.POST['password'] == request.POST['confirm']:
            # user 객체를 새로 생성
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')

# 로그인
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)

        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, 'login.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, 'login.html')