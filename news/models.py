from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
		
class News(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
	source = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title
	
	def summary(self):
		return self.body[:125]
	
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
