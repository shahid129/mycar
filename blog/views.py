from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import PostAd


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