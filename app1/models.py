from django.db import models

class Question(models.Model):
	Q = models.TextField()
	A1 = models.TextField()
	A2 = models.TextField()
	A3 = models.TextField()
	A4 = models.TextField()
	A5 = models.TextField()
	A6 = models.TextField()
	QType = models.TextField()
	RightAnswer = models.CharField(max_length = 6)
	Source = models.URLField()
	Comment = models.TextField()
