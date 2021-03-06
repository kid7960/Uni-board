from django.shortcuts           import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls                import reverse
from .models                    import User_Post, User_Comment
from django.http                import HttpResponseRedirect
from django.db.models           import Q
from main.apps.leaderboard.models import Leaderboard
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Main Message Board Page
class Message_Board(ListView):
    model               = User_Post
    ordering            = ['-post_date']                   # Orders to most recent date
    context_object_name = 'user_posts'
    template_name       = 'message_board/message_board.html'
    paginate_by = 4
    
class Post_Detail(DetailView):
    model = User_Post
    template_name   = "message_board/post_detail.html"

class Create_Post(LoginRequiredMixin, CreateView):
    model           = User_Post
    fields          = ['post_subject', 'post_content', 'post_tags']
    template_name   = "message_board/create_post.html"
    post_id = None

    # Validate user is logged in
    def form_valid(self, form):
        form.instance.post_user = self.request.user
        post            =   form.save()
        self.post_id    =   post.post_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.post_id})

class Update_Post(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model           = User_Post
    fields          = ['post_subject', 'post_content', 'post_tags']
    template_name   = "message_board/update_post.html"
    post_id = None

    # Validate user is logged in
    def form_valid(self, form):
        form.instance.post_user = self.request.user
        post            =   form.save()
        self.post_id    =   post.post_id
        return super().form_valid(form)

    # Validate user owns post or is a staff member
    def test_func(self):
        isPostOwnerOrStaff = False
        post_detail = self.get_object()
        if self.request.user == post_detail.post_user or self.request.user.is_staff == True:
            isPostOwnerOrStaff = True
        return isPostOwnerOrStaff

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.post_id})

class Delete_Post(DeleteView):
    model = User_Post
    template_name   = "message_board/delete_post_confirm.html"

    # Validate user owns post or is a staff member
    def test_func(self):
        isPostOwnerOrStaff = False
        post_detail = self.get_object()
        if self.request.user == post_detail.post_user or self.request.user.is_staff == True:
            isPostOwnerOrStaff = True
        return isPostOwnerOrStaff

    def get_success_url(self):
        return reverse('my_posts')

class My_Posts(LoginRequiredMixin, ListView):
    model               = User_Post
    ordering            = ['-post_date']                   # Orders to most recent date
    context_object_name = 'user_posts'
    template_name       = 'message_board/my_posts.html'
    paginate_by = 4

# Search Posts
class Search_Posts(ListView):
    model               = User_Post
    ordering            = ['-post_date']                   # Orders to most recent date
    context_object_name = 'user_posts'
    template_name       = 'message_board/message_board.html'

    def get_queryset(self):
        
        search_query = self.request.GET.get('search-text')
        return User_Post.objects.filter(Q(post_tags__icontains=search_query) | Q(post_subject__icontains=search_query)).order_by('-post_date')

# Comment system

class Add_Comment(LoginRequiredMixin, CreateView):
    model           = User_Comment
    fields          = ['comment']
    #form_class      = Add_Comment_Form
    template_name   = "message_board/add_comment.html"
    cmnt_id = None
    post_id = None

    # Validate user is logged in
    def form_valid(self, form):
        form.instance.post_id   = self.kwargs['pk']
        form.instance.cmnt_user = self.request.user
        comment         =   form.save()
        self.cmnt_id    =   comment.cmnt_id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})

class Delete_Comment(DeleteView):
    model           = User_Comment
    template_name   = "message_board/delete_comment_confirm.html"

    # Validate user owns post or is a staff member
    def test_func(self):
        isPostOwnerOrStaff = False
        post_detail = self.get_object()
        if self.request.user == post_detail.post_user or self.request.user.is_staff == True:
            isPostOwnerOrStaff = True
        return isPostOwnerOrStaff

    def get_success_url(self):
        return reverse('message_board')

# Like Posts
def like_post(request, pk, current_url):

    try: 
        post = get_object_or_404(User_Post, post_id=request.POST.get('post_id'))

        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
            losePoint(post)
        else:
            post.likes.add(request.user)
            liked = True
            addPoint(post)
        return HttpResponseRedirect(current_url)
    except:
        return HttpResponseRedirect('/account/login')

def addPoint(post):
    leaderboard = Leaderboard()

    obj, created = Leaderboard.objects.get_or_create(user=post.post_user)

    if created == True:
        obj.points = 1
    else:
        obj.points = obj.points + 1

    obj.save()

def losePoint(post):
    leaderboard = Leaderboard()

    obj, created = Leaderboard.objects.get_or_create(user=post.post_user)

    if created == True:
        obj.points = 0
    else:
        obj.points = obj.points - 1

    obj.save() 