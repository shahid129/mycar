from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from .models import PostAd, Images
from .forms import PostForm, NewUserForm, CustomerCommentForm, ImagesForm
# from django import forms
# from cloudinary.forms import cl_init_js_callbacks



class PostAdList(generic.ListView):
    model = PostAd
    queryset = PostAd.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    


class PostDetail(View):
    """
    Renders post detail for every post
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = PostAd.objects

        post = get_object_or_404(queryset, slug=slug)
        images = Images.objects.filter(name=post)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                'commented': False,
                "liked": liked,
                "comment_form": CustomerCommentForm(),
                'images': images
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = PostAd.objects
        post = get_object_or_404(queryset, slug=slug)
        images = Images.objects.filter(name=post)

        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        customer_comment_form = CustomerCommentForm(data=request.POST)

        if customer_comment_form.is_valid():
            customer_comment_form.instance.email = request.user.email
            customer_comment_form.instance.name = request.user.username
            comment = customer_comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            customer_comment_form = CustomerCommentForm()
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                'commented': True,
                "liked": liked,
                "comment_form": CustomerCommentForm(),
                'images': images
            },
        )


def post_your_add(request):
    """
    Users can post their add and add multiple images for the same post
    """

    # Formset for Image class
    ImageFormSet = formset_factory(ImagesForm, extra=3)  # Add 3 more fields to add image
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()

        # loop through the image
            for form_image in formset:
                image = form_image.cleaned_data.get('images')
                photo = Images(images=image, name=new_form)
                photo.save()

            print('formvalid: ', form.is_valid())  # Check if form is valid
            print('formsetvalid: ', formset.is_valid())  # Check if form is valid
            messages.info(request, 'Post added successfully.')
            return redirect('home')
        
    else:
        form = PostForm()
        formset = ImageFormSet()

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'post_your_add.html', context)


def post_your_add_edit(request, post_id):
    item = get_object_or_404(PostAd, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = PostForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'post_your_add_edit.html', context)


def post_your_add_delete(request, post_id):
    item = get_object_or_404(PostAd, id=post_id)
    item.delete()
    return redirect('home')


def register_request(request):
    """
    User can register for new accounts. This will enable them to create
    edit and update their posts.
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"form":form})


def login_request(request):
    """
    User can log in to the page and edit their items
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Your are logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request=request, template_name='registration/login.html', context={"form": form})


def logout_request(request):
    """
    User can log out
    """
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')


class PostAdLike(View):
    """
    User can like or unlike a post
    """
    def post(self, request, slug, *args, **kwargs):
        """
        User can like or unlike a post
        """
        post = get_object_or_404(PostAd, slug=slug)   

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def search_car(request):
    """
    User can search for name of the car. The search engine looks for the title(name)
    of the car
    """
    if request.method == 'POST':
        searched = request.POST['searched']
        postads = PostAd.objects.filter(title__icontains=searched)

        return render(request, "search_car.html", {'searched': searched, 'postads': postads})
    else:
        return render(request, "search_car.html")


