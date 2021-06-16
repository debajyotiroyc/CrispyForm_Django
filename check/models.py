from django.db import models
Gen=(
    ("male","MALE"),
    ("female","FEMALE"),
    ("others","OTHERS"),
)

# Create your models here.
class info(models.Model):
    name=models.TextField(max_length=50)
    gender=models.CharField(max_length=10,choices=Gen,null=True)
    standard=models.IntegerField()
    percentage=models.FloatField(max_length=4)
    email=models.CharField(max_length=20)
    password=models.TextField(max_length=10)

    def __str__(self):
        return self.name



