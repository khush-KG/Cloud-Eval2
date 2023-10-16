from django.db import models

# Create your models here.
class Tables(models.Model):
    class Meta:
        unique_together = (('TableID','BookDateTime'),)
        constraints = [
            models.CheckConstraint(
                check=models.Q(TableID__gte=1) & models.Q(TableID__lt=20),
                name="A TableID value is valid between 1 and 20",
            )
        ]
    BookingID = models.AutoField(primary_key=True)
    TableID = models.IntegerField()
    BookDateTime = models.DateTimeField()
    # Duration_option = (
    #     ('2', '2 hours'),
    #     ('3', '3 hours'),
    #     ('4', '4 hours'),
    # )
    BookDuration = models.CharField(default="2 hours",max_length=255)
    DinerName = models.CharField(max_length=255,blank=True)
    DinerAge = models.IntegerField(default=20)
    DinerGender = models.CharField(max_length=255,blank=True)
    DinerEmail = models.EmailField(max_length=254,null=True)
    DinerPhone_num = models.IntegerField(null=True)
    DinerAddress = models.TextField(default="abc")
    Guests_num = models.IntegerField(default=0)
    Guest_list = models.TextField(blank=True)
    