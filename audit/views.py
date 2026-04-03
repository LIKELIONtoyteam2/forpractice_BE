from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Hashtag

from .forms import PostForm

# Create your views here.

def home(request):
  posts = Post.objects.order_by('-created_at')
  return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
  post_detail=get_object_or_404(Post, pk=post_id)
  post_hashtag=post_detail.hashtag.all()
  return render(request, 'detail.html', {'post':post_detail, 'hashtag':post_hashtag})

def new(request):
  form=PostForm()
  return render(request, 'new.html', {'form':form})

def create(request):
  form=PostForm(request.POST, request.FILES)
  if form.is_valid():
    new_audit=form.save(commit=False)
    new_audit.expiration = request.POST['expiration']
    new_audit.open = request.POST['open']
    new_audit.save()

    hashtags=request.POST['hashtags']
    hashtag_list=hashtags.split(', ')

    for tag in hashtag_list:
      tag = tag.strip()
      new_hashtag=Hashtag.objects.get_or_create(hashtag=tag)
      new_audit.hashtag.add(new_hashtag[0])

    return redirect('audit:detail', new_audit.id)
  return redirect('audit:home')

def delete(request, post_id):
  delete_audit = get_object_or_404(Post, pk=post_id)
  delete_audit.delete()
  return redirect('audit:home')

def update_page(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  form = PostForm(instance=post)
  return render(request, 'update.html', {'form': form, 'post': post})

def update_post(request, post_id):
  post = get_object_or_404(Post, id=post_id)
  form = PostForm(request.POST, request.FILES, instance=post)
  if form.is_valid():
    update_audit = form.save(commit=False)
    update_audit.save()
    return redirect('audit:detail', update_audit.id)
  return redirect('audit:home')
