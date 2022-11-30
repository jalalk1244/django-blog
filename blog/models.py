from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

ALLERGY_ICONS = (
    ('0', 'none'),
    ('1', 'cereal'),
    ('2', 'gluten'),
    ('3', 'milk'),
    ('4', 'eggs'),
    ('5', 'peanuts'),
    ('6', 'nuts'),
    ('7', 'crustaceans'),
    ('8', 'mustard'),
    ('9', 'fish'),
    ('11', 'lupin'),
    ('12', 'sesame'),
    ('13', 'celery'),
    ('14', 'soya'),
    ('15', 'molluscs'),
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        f'Comment {self.body} by {self.name}'


class Dishes(models.Model):
    '''Model for the Dishes in the menu '''
    name = models.CharField(max_length=50, unique=True)
    dish_pic = CloudinaryField('image', default='placeholder')
    description = models.CharField(max_length=300)
    allergy_icon = models.CharField(max_length=12, choices=ALLERGY_ICONS, default='0')
    calorie_amount = models.CharField(max_length=6)
    protien_amount = models.CharField(max_length=6)
    carbs_amount = models.CharField(max_length=6)
    fat_amount = models.CharField(max_length=6)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
