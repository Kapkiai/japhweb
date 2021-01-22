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


class Transactions(models.Model):
    ReceiptNo = models.CharField(max_length=15, unique=True, null=True)
    CompletionTime = models.CharField(max_length=30, null=True)
    Details = models.CharField(max_length=100, null=True)
    PaidIn = models.CharField(max_length=10, null=True)
    Withdrawn = models.CharField(max_length=10, null=True)
    Balance = models.CharField(max_length=10, null=True)

    def __str__(self):
        return "%s" % self.ReceiptNo


