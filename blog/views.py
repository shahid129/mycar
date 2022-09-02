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


# def feature(request):
#     return render(request, 'feature.html')

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'feature.html', {'form': form})


def product_list(request):
    filter_item = PostAd(request.GET, queryset=PostAd.objects.all())
    return render(request, 'index.html', {'filter': filter_item})