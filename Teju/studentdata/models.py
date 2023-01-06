from django.db import models

# Create your models here.

class classtable(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=20)
	house_teacher = models.CharField(max_length=35)
	student_count=models.IntegerField()

	def __str__(self):
		return self.first_name


class student(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=40)
	classtable = models.ForeignKey(classtable,on_delete=models.CASCADE)
	student_id = models.IntegerField()
	age = models.IntegerField()
	email = models.EmailField(max_length=50)

	def __str__(self):
		return self.first_name
