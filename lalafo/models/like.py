from django.db import models
from.comment import Comment
from.elan import Elan

class Like(models.Model):
    elan = models.ForeignKey(Elan, null=True, blank=True, related_name="elan_likes", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, related_name="comment_likes", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comment)
    
