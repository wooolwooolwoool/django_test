from django.shortcuts import render
from django import forms
from book.models import *
from book.forms import *
import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView
import json

def add_post(request):
    # Bookshelfが50件以上登録されていたら、古いものを1件削除
    tmp = Bookshelf.objects.all()
    if len(tmp) > 50:
        Book.objects.filter(target__exact=tmp[0].pk).all().delete()
        tmp[0].delete()

    form = BookshelfForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        formset = BookFormset(request.POST, files=request.FILES, instance=post)
        if formset.is_valid():
            post.save()
            formset.save()
            print(post.pk)
            return redirect('book_detail', post.pk)
        else:
            context['formset'] = formset
    else:
        context['formset'] = BookFormset()
    return render(request, 'book/post_form.html', context)

def book_serch(request, key):
    url = "https://api.openbd.jp/v1/get?isbn=" + key
    html = requests.get(url)
    # 先頭と最後尾にカッコがついているので取って返却
    return HttpResponse(html.text[1:-1])

class BookList(ListView):
    model = Bookshelf
    template_name = 'book/post_list.html'

    def get_queryset(self):
        return Bookshelf.objects.all().order_by("-pk")

def book_detail(request, pk):
    bookshelf = Bookshelf.objects.get(pk=pk)
    books = Book.objects.filter(target__exact=pk).all()

    context = {'bookshelf': bookshelf,
               'books': books}
    return render(request, 'book/post_detail.html', context)

def top(request):
    return render(request, 'book/top.html', {})
