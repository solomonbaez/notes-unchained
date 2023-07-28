from django.db import models

class Note(models.note):
    title = models.CharFileld(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title