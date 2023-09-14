from django.views import View
from django.shortcuts import render
from store.models import User


class UserBoard(View):
    def get(self, request):
        return render(request, 'users.html', {'users': User.objects.all() })

