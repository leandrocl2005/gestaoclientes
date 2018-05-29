from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField()
	salary = models.DecimalField(max_digits=12, decimal_places=2)
	bio = models.TextField(default='professor')
	email = models.EmailField(max_length=80)
	photo = models.ImageField(upload_to='clients_photos',null=True,blank=True)

	def __str__(self):
		return self.first_name + "_" + self.last_name
