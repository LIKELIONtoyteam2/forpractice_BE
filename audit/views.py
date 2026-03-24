from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Inventory

from .forms import PostForm

# Create your views here.

def home(request):
  posts = Post.objects.order_by('-created_at')
  return render(request, 'home.html', {'posts': posts})

def detail(request, post_id):
  post_detail=get_object_or_404(Post, pk=post_id)
  return render(request, 'detail.html', {'post':post_detail})

def new(request):
  form=PostForm()
  return render(request, 'new.html', {'form':form})

def create(request):
  form=PostForm(request.POST, request.FILES)
  if form.is_valid():
    new_audit=form.save(commit=False)
    new_audit.save()
    return redirect('audit:detail', new_audit.id)
  return redirect('audit:home')

def delete(request, post_id):
  delete_audit = get_object_or_404(Post, pk=post_id)
  delete_audit.delete()
  return redirect('audit:home')

def update_page(request, post_id):
  update_audit = get_object_or_404(Post, pk=post_id)
  return render(request, 'update.html', {'update_audit': update_audit})

def update_post(request, post_id):
  update_audit = get_object_or_404(Post, pk=post_id)
  update_audit.name = request.POST['name']
  update_audit.expiration = request.POST['expiration']
  update_audit.open = request.POST['open']
  update_audit.save()
  return redirect('audit:home')

def inventory_list(request):
    # DB에 있는 모든 재고(Inventory) 데이터를 가져와서 items라는 상자에 담습니다.
    items = Inventory.objects.all().order_by('expiration_date') # 유통기한이 임박한 순서대로 정렬!
    # inventory_list.html 파일에 items 상자를 전달해 줍니다.
    return render(request, 'inventory_list.html', {'items': items})