from django.views import View
from django.shortcuts import render, redirect
from store.models import User
from store.form import UserForm


class UserBoard(View):
    contexts = {}
    def get(self, request):
        self.contexts['form'] = UserForm()
        self.contexts['users'] = User.objects.all()
        return render(request, 'users.html', {**self.contexts })
    def post(self,request):
        self.contexts['form'] = UserForm(request.POST)
        if self.contexts['form'].is_valid():
            self.contexts['form'].save()
            return redirect('users')
        else:
            print(self.contexts['form'].errors)
        return render(request, 'users.html', {**self.contexts })

