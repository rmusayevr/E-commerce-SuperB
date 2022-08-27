from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Authors(models.Model):
    author = models.CharField(max_length=100, default="John Doe")
    author_slug = models.SlugField(max_length=150, allow_unicode=True, null=True, blank=True)
    author_image = models.ImageField(upload_to = "user_images")

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('author_blogs', kwargs={'slug':self.author_slug})

    def save(self, *args, **kwargs):
        self.author_slug = slugify(self.author)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to = "blog_images")
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    short_desc = models.TextField()
    desc = models.TextField()
    read_count = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug':self.slug})
        
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

class Comments(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True)
    comment = models.TextField(default="Blog is awesome!")
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='blog')

    def __str__(self):
        return f"{self.name}'s comment"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

