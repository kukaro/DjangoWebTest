from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import CustomUserCreationForm
from .forms import UserRegisterForm
from .forms import ArticleWriteForm
from .models import CustomUser, Article, Board


# Create your views here.
class Register(View):
    form_class = UserRegisterForm
    template_name = 'main/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                obj = CustomUser(
                    id=form.data['id'],
                    nick=form.data['nick'],
                    stud_no=form.data['stud_no'],
                    email=form.data['email'],
                    pw_hash=form.data['pw_hash'],
                    pnt=0,
                    password='1234'
                )
                obj.save()
            except Exception:
                return HttpResponse('exception')

            return HttpResponse('success')
        return HttpResponse('fail')


class Write(View):
    form_class = ArticleWriteForm
    template_name = 'main/write.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                obj = Article(
                    board=Board.objects.get(pk=kwargs['bid']),
                    title=form.data['title'],
                    content=form.data['content'],
                    author=CustomUser.objects.get(pk=form.data['author']),
                )
                obj.save()
            except Exception as e:
                print(e)
                return HttpResponse('exception')

            return HttpResponse('success')
        return HttpResponse('fail')
