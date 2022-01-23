from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .forms import PostForm
from .models import Post, Photo
from profiles.models import Profile

# Create your models here.
'''
class Profile(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars')
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of the user {self.user}"
'''
def post_list_and_create(request):
    form = PostForm(request.POST or None)
    qs = Post.objects.all()

    if request.is_ajax():
        if form.is_valid():
            author = Profile.objects.get(user=request.user)
            instance = form.save(commit=False)
            instance.author = author
            instance.save()
            return JsonResponse({
                'title': instance.title,
                'body': instance.body,
                'author': instance.author.user.username,
                'id': instance.id,
            })
    context = {
        'form': form,
    }
    return render(request, 'posts/main.html', context)

def load_post_data_view(request, **kwargs):
    if request.is_ajax():
        num_posts = kwargs.get('num_posts')
        visible = 3
        upper = num_posts
        lower = upper - visible
        size = Post.objects.count()

        qs = Post.objects.all()
        data = []
        for obj in qs:
            item = {
                'id': obj.id,
                'title': obj.title,
                'body': obj.body,
                'liked':True if request.user in obj.liked.all() else False,
                'conunt': obj.like_count,
                'author': obj.author.user.username
            }
            data.append(item)
    return JsonResponse({'data':data[lower:upper], 'size':size})

def like_unlike_post(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked':liked, 'count': obj.like_count})

def hello_wold_view(request):
    return JsonResponse({'text': 'Hey'})

def post_detaile(request, pk):
    obj = Post.objects.get(pk=pk)
    form = PostForm()

    context = {
        'obj': obj,
        'form': form,
    }

    return render(request, 'posts/detaile.html', context)

def post_detaile_data_view(request, pk):
    obj = Post.objects.get(pk=pk)
    data = {
        'id': obj.id,
        'title': obj.title,
        'body': obj.body,
        'author': obj.author.user.username,
        'logged_in': request.user.username,
    }

    return JsonResponse({'data':data})

def update_post(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.is_ajax():
        new_title = request.POST.get('title')
        new_body = request.POST.get('body')
        obj.title = new_title
        obj.body = new_body
        obj.save()
        return JsonResponse({
            'title': new_title,
            'body': new_body,
        })

def delete_post(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.is_ajax():
        obj.delete()
        return JsonResponse({})

def img_upload_view(request):
    print(request.FILES)
    if request.method == 'POST':
        img = request.FILES.get('file')
        new_post_id = request.POST.get('new_post_id')
        post = Post.objects.get(id=new_post_id)
        Photo.objects.create(image=img, post=post)
    return HttpResponse()
