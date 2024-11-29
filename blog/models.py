from django.db import models

# Create your models here.
class StaffModel(models.Model):

    GENDER_TYPE_CHOICES = (
        ("M" , "Male"),
        ("F", "Female")
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_TYPE_CHOICES)
    photo = models.ImageField(upload_to='staff_photos', default='avatar/userPhoto.jpg', blank=True)
    birth_day = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return f"{self.first_name} {self.last_name} "
    
    class Meta: 
        db_table = 'staff'
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'




