from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# STATUS = ((0, "Draft"), (1, "Published"))


class PostAd(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.IntegerField(null=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_PostAds")
    created_on = models.DateTimeField(auto_now=True)
    updtaed_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500)
    image = CloudinaryField('image', default='placeholder')
    year = models.DateField(auto_now=False)
    tax = models.DateField(auto_now=False)
    nct = models.DateField(auto_now=False)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    # Status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    def year_only(self):
        return self.year.strftime('%Y')


class CustomerComment(models.Model):
    post = models.ForeignKey(PostAd, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
