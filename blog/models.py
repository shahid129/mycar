from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# STATUS = ((0, "Draft"), (1, "Published"))


class PostAd(models.Model):
    """
    A model that creates all the fields to post an add
    """
    title = models.CharField(max_length=200, unique=True)
    price = models.IntegerField(null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_PostAds")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500)
    image = models.ImageField()
    year = models.DateField(auto_now=False)
    tax = models.DateField(auto_now=False)
    nct = models.DateField(auto_now=False)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        Order the listing by recently created items first
        """
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Returns the total number of likes
        """
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class CustomerComment(models.Model):
    """
    A model that creates all the fields for a customer to add comment
    """
    post = models.ForeignKey(
        PostAd, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order the Comments by recently created items first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Images(models.Model):
    """
    Users can add more images along with their posts
    """
    name = models.ForeignKey(
        PostAd, on_delete=models.CASCADE, blank=True, null=True)
    images = models.ImageField()
