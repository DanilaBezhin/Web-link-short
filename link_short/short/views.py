from urllib import request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from .models import Link
from django.views.generic import ListView, CreateView
import pyshorteners


def home(request):
    return render(request, 'short/home.html')


class About(ListView):
    model = Link
    template_name = 'short/about.html'
    context_object_name = 'link'
    ordering = ['-id']

@method_decorator(login_required, 'dispatch')
class CreateLink(SuccessMessageMixin, CreateView):
    model = Link
    template_name = 'short/create.html'
    fields = ['title', 'start_link']
    success_message = "Ссылка успешно создана!"
    # messages.success(request, f'Ссылка успешно создана!')

    def shorten_url(self, url):
        sl = 'https://' + str(url)
        return sl.replace(" ", "")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.late_link = self.shorten_url(form.instance.title)
        return super().form_valid(form)

