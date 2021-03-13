from django.db import models



class AudioBookFields(models.Model):
    ID = models.IntegerField(primary_key = True )
    Title = models.CharField(blank = False , null = False , max_length = 100)
    Author = models.CharField(blank = False , null = False , max_length = 100)
    audioFile = models.FileField(default = None)
    Narrator = models.CharField(blank = False , null = False , max_length = 100)
    DurationInNumberSeconds = models.PositiveIntegerField(blank = False , null = False)
    UploadedTime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Title


