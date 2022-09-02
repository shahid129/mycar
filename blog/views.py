from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import PostAd
from .forms import PostForm


class PostAdList(generic.ListView):
    model = PostAd
    queryset = PostAd.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = PostAd.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
            }
        )


def post_your_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_your_add.html', {'form': form})
