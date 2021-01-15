from django.db import models


class Upload(models.Model):
    upload_file = models.FileField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # randomNum = random.randint(10000, 90000)
        new_name = "data" + ".docx"
        self.upload_file.name = new_name
        super(Upload, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.upload_file
