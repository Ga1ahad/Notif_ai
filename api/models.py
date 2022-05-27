from django.db import models


class Message(models.Model):
    body = models.CharField(max_length=160, blank=False)
    views = models.PositiveIntegerField(default=0)

    def reset_views(self):
        self.views = 0
        self.save()

    def increment_views(self):
        self.views += 1
        self.save()
