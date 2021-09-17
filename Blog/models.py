from django.db import models

# Create your models here.

class Students(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    university = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.firstname

class Blog(models.Model):
    image = models.ImageField(upload_to="blog_pics")
    title = models.CharField(max_length=100)
    description = models.TextField()
    hashtag = models.TextField()
    date = models.DateField ( auto_now=True )



class Comment(models.Model):
    text = models.TextField(default="")
    date = models.DateTimeField(auto_now=True)
    blog= models.ForeignKey(Blog,on_delete=models.CASCADE)
