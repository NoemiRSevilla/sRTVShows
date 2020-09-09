from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors ={}
        if len(postData['title']) <2:
            errors["title"] = "<div class='ohno'>Title of TV Show should at least be 2 characters</div>"
        if len(postData['network'])<3:
            errors['network'] = "<div class='ohno'>Network name has to at least have 3 characters</div>"
        if len(postData['description'])>1 and len(postData['description'])<10:
            errors['description'] = "<div class='ohno'>Description optional but if present, must at least be 10 characters</div>"
        if postData['release'] == "":
            errors['release'] = "<div class='ohno'>Release date required</div>"
        if len(postData['release']) > 0:
            formtime = datetime.strptime(postData['release'], "%Y-%m-%d")
            present = datetime.now()
            if formtime.date() > present.date():
                errors['release'] = "<div class='ohno'>Release date has to be from the past</div>"
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release = models.DateField(auto_now=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ShowsManager()    # add this line!
                
    def __repr__(self):
        return f"Title: {self.title}, Network: {self.network}, Description: {self.description}"