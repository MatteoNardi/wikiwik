from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Publication date', auto_now_add=True)
    slug = models.SlugField()
    author = models.ForeignKey('auth.User', related_name='pages')
    content = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]

class Picture(models.Model):
	title = models.CharField(max_length=200)
	picture = models.ImageField(upload_to='img')
		