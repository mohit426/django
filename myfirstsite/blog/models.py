from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
		author = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
		title = models.CharField(max_length=200)
		text = models.TextField()
		created_date = models.DateTimeField(default=timezone.now)
		published_date = models.DateTimeField(blank=True, null=True)
		Email = models.EmailField(max_length=254,blank=False,null=False)
		age = models.PositiveSmallIntegerField(blank=False,null=False)
		GENDER_CHOICE = (('m','Male'),('F', 'Female'))
		gender = models.CharField(max_length=1, choices=GENDER_CHOICE,default='M')

		def published(self):
			self.published_date = timezone.now()
			self.save()

		def __str__(self):
			return self.title
