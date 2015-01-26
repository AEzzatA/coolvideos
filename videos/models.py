from django.db import models

class Video(models.Model):
	url = models.URLField()
	title = models.CharField(max_length=140)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('videos:video_detail', arge((self.id, )))
