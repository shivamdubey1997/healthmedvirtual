from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    members = models.ManyToManyField(User,related_name="followers",blank=True)
    membership = models.ManyToManyField(User,related_name="followings",blank=True)
    profile_picture = models.ImageField( upload_to='profilepics')

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posts")
    likes = models.ManyToManyField(User,related_name='likes',blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

class Shorts(models.Model):
    shorts = models.FileField(upload_to='shorts',null=True,default='shorts/video.mp4')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='shortslikes', blank=True)

class VlogPost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vlog = models.FileField(upload_to='vlogpost')
    likes = models.ManyToManyField(User, related_name='likess', blank=True)
    member = models.ManyToManyField(User, related_name='family', blank=True)
    mediastram = models.CharField(max_length=50)
    description = models.TextField()
    #profile = models.ForeignKey(Profile,on_delete=models.CASCADE)



class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    vlogpost = models.ForeignKey(VlogPost,on_delete=models.CASCADE)

class Uploadworkoutvideo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='workoutpost')
    titleofvideo = models.TextField()
    dietdescription = models.TextField()
    country = models.CharField(max_length=100)
    day = models.CharField(max_length=250)
    muscle = models.CharField(max_length=100)
    myworkoutfollowers = models.ManyToManyField(User, related_name='myworkoutfollowers', blank=True)

class Commentworkout(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    workoutpost = models.ForeignKey(Uploadworkoutvideo,on_delete=models.CASCADE)

class Healthymeals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    resturantname = models.TextField()
    whatsappno = models.IntegerField()
    resturantmenu = models.ImageField(upload_to='resturantmenu')


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titleofvideo = models.TextField()
    blogtext = models.TextField()
    reads = models.ManyToManyField(User, related_name='reads', blank=True)
    blogimage = models.ImageField(upload_to='blogimage')

