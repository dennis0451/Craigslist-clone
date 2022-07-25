from unicodedata import category
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from . import views
from .models import Category, Post
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    all_categories = Category.objects.all()
    return render(request, 'craigslist_app/index.html',{'all_categories' : all_categories})

def all_cats(request):
    all_categories = Category.objects.all()
    # all_posts = Post.objects.all()
    return render(request, 'craigslist_app/allCategories.html',{'all_categories' : all_categories})


@csrf_exempt
def view_category(request, category_id):
    post = Post.objects.all().filter(category_id = category_id)
    category = Category.objects.all().get(id = category_id)
    print(post)
    print(category)
    data = {"post":post, "category":category}

    return render(request, 'craigslist_app/viewCategory.html', data)

@csrf_exempt
def create_category(request):
    all_categories = Category.objects.all()

    if request.method == 'POST':
        body = json.loads(request.body)
        newCategory = Category(name = body['category'])
        newCategory.save()
        HttpResponse({})

    return render(request, 'craigslist_app/newCategory.html', {'all_categories': all_categories})

@csrf_exempt
def edit_category(request):
    all_categories = Category.objects.all()

    if request.method == 'POST':
        body = json.loads(request.body)
        newCategory = Category(name = body['category'])
        newCategory.save()
        HttpResponse({})

    return render(request, 'craigslist_app/newCategory.html', {'all_categories': all_categories})

# @csrf_exempt
# def list_category(request, category_id):
#     print('here bruv')
#     return render(request, 'craigslist_app/categories.html')
# # def list_posts(request):
# #     all_posts = Post.objects.all()

def all_posts(request):
    all_posts = Post.objects.all()
    print('made it bruv')
    return render(request, 'craigslist_app/allPosts.html', {'all_posts':all_posts})


@csrf_exempt
def view_post(request,category_id, post_id):
    post = Post.objects.all().filter(id=post_id)
    category= Category.objects.all().get(id=category_id)
    print(post)
    print(category)
    data = {"post": post, "category":category}

    return render(request, 'craigslist_app/viewPost.html', data)

@csrf_exempt
def single_post(request,post_id):
    post = Post.objects.all().get(id=post_id)
    # category= Category.objects.all().get(id=category_id)
    print(post)
    # print(category)
    data = {"post": post}

    return render(request, 'craigslist_app/deletePost.html', data)


@csrf_exempt
def create_post(request, category_id):
    current_category = Category.objects.all().get(id=category_id)
    category =  current_category
    print(category)
    if request.method == 'POST':
        body = json.loads(request.body)
        newPost = Post(title=body['title'], price=body['price'], description=body['description'],  category=category)
        newPost.save()
        return JsonResponse({})

    return render(request, 'craigslist_app/newPost.html')

@csrf_exempt
def edit_post(request, category_id, post_id):
    category = Category.objects.all().get(id=category_id)
    post = Post.objects.all().get(id= post_id)
    # data
    print(category)
    print(post)
    data = {'post': post, 'category': category}    
    if request.method == 'PUT':
        body = json.loads(request.body)
        post = Post.objects.all().get(id = post_id)
        post.title = body['title']
        post.price = body['price']
        post.description = body['description']
        post.save()
        return JsonResponse({})

    return render(request, 'craigslist_app/editPost.html', data)


def page_not_found(request, exception):
    print('here')
    return render(request, 'craigslist_app/404.html', status=404)
