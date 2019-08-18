from django.db import models

class Words(models.Model):
	word = models.CharField(max_length=100)
	occurence_count = models.IntegerField(default=0)

	
	def __str__(self):
		return self.word

	
	
	
	