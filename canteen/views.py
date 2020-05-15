from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render

def main_page(request):

    return render(request, 'canteen/base.html')
