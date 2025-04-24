from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    id = models.AutoField(primary_key=True)
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    enabled = models.BooleanField()

    def __str__(self):
        return self.title
    
    class MPTTMeta:
        order_insertion_by = ['title']

class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    id_rubric = TreeForeignKey(Rubric,on_delete=models.PROTECT,null=True)
    text = models.TextField(null=True)
    author = models.CharField(max_length=100)
    create_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Author(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="authors",null=True,blank=True)

    def __str__(self):
        return str(self.id)+". "+self.title

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    category = TreeForeignKey(Category,on_delete=models.PROTECT,null=True)
    title = models.CharField(max_length=100)
    #id_author = models.IntegerField()
    id_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    price = models.IntegerField(null=True)
    content = models.TextField(null=True)
    data_pub = models.DateTimeField(default=timezone.now)
    enabled = models.BooleanField()
    reiting = models.PositiveSmallIntegerField(null=True)
    count_view = models.IntegerField(null=True)
    def __str__(self):
        return str(self.id)+". "+self.title

class New(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/news',null=True,blank=True)
    mini_content = models.TextField(null=True)
    content = models.TextField(null=True)
    cur_date = models.DateTimeField(default=timezone.now)
    enabled = models.BooleanField()
    def __str__(self):
        return str(self.id)+". "+self.name
    
    