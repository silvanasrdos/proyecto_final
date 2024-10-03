import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify
import os

class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True, blank=True)
    content= models.TextField(max_length=10000)
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date= models.DateTimeField(default=timezone.now)
    modification_date= models.DateTimeField(auto_now=True)
    allow_comments= models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    @property
    def amount_comments(self):
        return self.comments.count() #TODO: DEFINIR COMMENTS 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)
        #TODO: definir imagenes portada
    
    def generate_unique_slug(self):
        #tenemos este titulo
        #tenemos-este-titulo
        slug= slugify(self.title)
        unique_slug = slug
        num = 1

        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}--{num}'
            num += 1

        return unique_slug
    
class Comment(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content= models.TextField(max_length=500)
    creation_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content 

# Create your models here.
def get_image_filename(instance, filename):
    post_id = instance.post.id
    images_count = instance.post.images.count()
    base_filename, file_extension = os.path.splitext(filename) # esto se llama unpacking (desempaquetado)
    new_filename = f"post_{post_id}_cover_{images_count + 1}{file_extension}"
    return os.path.join('post/cover/', new_filename)

class PostImage(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_filename,
    default='post/default/post_default.png')
    active = models.BooleanField(default=True)

def __str__(self):
    return f"PostImage {self.id}"

def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = self.generate_unique_slug()
    super().save(*args, **kwargs)

    if not self.images.exists():
        PostImage.objects.create(post=self,
    image='post/default/post_default.jpg')

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name