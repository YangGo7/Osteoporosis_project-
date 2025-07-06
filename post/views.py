from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Reply
from .forms import PostForm, ReplyForm
from django.contrib.auth.models import User
from django.db.models import Q  # 추가
from django.http import JsonResponse  # 추가


# 게시판 목록 (로그인하지 않은 사용자는 공개글만 볼 수 있음)
def board(request):
    query = request.GET.get('q', '')  # 검색어 받아오기

    if request.user.is_authenticated:
        # 로그인한 사용자: 전체 글 검색 가능
        posts = Post.objects.all()
    else:
        # 비회원: 비밀글 제외
        posts = Post.objects.filter(is_secret=False)

    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    posts = posts.order_by('-created_at')  # 정렬

    # 비밀글인 경우 제목을 '비밀글'로 변경
    for post in posts:
        if post.is_secret and request.user != post.author and not request.user.has_perm('post.view_secret_post'):
            post.title = "비밀글"  # 비밀글은 제목을 '비밀글'로 변경

    return render(request, 'post/board.html', {'posts': posts})

# 게시글 상세 조회
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 비밀글 접근 제한
    if post.is_secret and request.user != post.author and not request.user.is_staff:
        return redirect('board')  # 관리자 또는 작성자가 아니면 접근 불가

    replies = post.replies.all()
    can_reply = request.user == post.author or request.user.has_perm("post.can_reply")

    return render(request, 'post/post_detail.html', {
        'post': post,
        'replies': replies,
        'can_reply': can_reply
    })


# 게시글 작성성

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board')
    else:
        form = PostForm()

    return render(request, 'post/create_post.html', {'form': form})


# 답변 작성
@login_required
def create_reply(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 비밀글이면서 사용자가 답변 권한이 없으면 접근 불가
    if post.is_secret and not request.user.has_perm("post.can_reply"):
        return redirect('board')

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.post = post
            reply.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = ReplyForm()

    return render(request, 'post/create_answer.html', {'form': form, 'post': post})




# 게시글 수정 페이지
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('board')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form, 'post': post})

# 게시글 삭제 기능
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        return redirect('board')
    post.delete()
    return redirect('board')


# 좋아요 처리 뷰 만들기(post, reply) 추가
@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': post.likes.count()
    })
    
@login_required
def toggle_reply_like(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    user = request.user

    if user in reply.likes.all():
        reply.likes.remove(user)
        liked = False
    else:
        reply.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': reply.likes.count(),
    })