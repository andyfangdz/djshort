from django.db import models


class Redirect(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    destination = models.URLField(max_length=255)

    count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.name

    def add_count(self):
        self.count += 1
        self.save()
