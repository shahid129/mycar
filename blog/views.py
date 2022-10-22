from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from .utils import account_activation_token
from .models import PostAd, Images
from .forms import PostForm, NewUserForm, CustomerCommentForm, ImagesForm


class PostAdList(generic.ListView):
    """
    Show all the post on the home page
    maximum post on a page is six
    """
    model = PostAd
    queryset = PostAd.objects.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """
    Renders post detail for every post
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Get all the queryset and renders on the post_detail page
        """
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
        """
        Post all the queryset objects on the post_detail template
        """
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
    # Add 3 more fields to add image
    ImageInlineFormSet = inlineformset_factory(PostAd, Images, fields=(
        'images',), extra=3, can_delete=False, form=ImagesForm)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        formset = ImageInlineFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()

        # loop through the image
            for form_image in formset:
                image = form_image.cleaned_data.get('images')
                photo = Images(images=image, name=new_form)
                photo.save()

            messages.info(request, 'Post added successfully.')
            return redirect('home')

    else:
        form = PostForm()
        formset = ImageInlineFormSet()

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'post_your_add.html', context)


def post_your_add_edit(request, post_id):
    """
    A function that lets user update their post
    """
    # Creat instance of post-item
    item = get_object_or_404(PostAd, id=post_id)

    # Create instance of formset
    # Add 3 more fields to add image
    ImageInlineFormSet = inlineformset_factory(PostAd, Images, fields=(
        'images',), max_num=3, can_delete=False, form=ImagesForm)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=item)
        formset = ImageInlineFormSet(
            request.POST, request.FILES, instance=item)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Updated successfully.')
            return redirect('home')
        else:
            messages.info(request, 'Invalid Information')

    form = PostForm(instance=item)
    formset = ImageInlineFormSet(instance=item)
    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'post_your_add_edit.html', context)


def post_your_add_delete(request, post_id):
    """
    User can delete their own post
    """
    item = get_object_or_404(PostAd, id=post_id)
    item.delete()
    messages.info(request, 'Deleted Succesfully')

    return redirect('home')


def register_request(request):
    """
    User can register for new accounts. This will enable them to create
    edit and update their posts.
    """
    if request.method == "POST":
        form = NewUserForm(request.POST)
        user = request.user
        user.is_active = False
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # Check if Email id exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use')
        # Check if passwords match
        elif password1 != password2:
            messages.error(request, 'Passwords does not match')
        # Check if Username  exists
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
        elif form.is_valid():
            # User to receive email on registraions

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={
                'uidb64': uidb64,
                'token': account_activation_token.make_token(user)
            })
            activate_url = 'https://' + domain + link

            subject = 'Account Registration'
            message = 'Hello ' + username + \
                ', please clink on the link to verify your account ' + \
                activate_url
            recipient = form.cleaned_data.get('email')
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [recipient], fail_silently=False)
            user = form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
    else:
        print('invalid')
    form = NewUserForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"form": form}
    )


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
    return render(
        request=request,
        template_name='registration/login.html',
        context={"form": form}
    )


class Verification(View):
    """
    Send verification email with a link
    When user clicks on the link, their account will
    be activated
    """

    def get(self, request, uidb64, token):
        """
        Verify if the sent link to user is correct
        """
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated succesfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')


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
    User can search for name of the car. The search engine looks for the
    title(name) of the car
    """
    if request.method == 'POST':
        searched = request.POST['searched']
        postads = PostAd.objects.filter(title__icontains=searched)

        return render(
            request,
            "search_car.html",
            {
                'searched': searched,
                'postads': postads
            }
        )
    else:
        return render(request, "search_car.html")


def about(request):
    """
    Render about page on request
    """

    return render(request, 'about.html')
