from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomStaffManager

# Create your models here.
# from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

from cst_data.models import College_schools,Departments

GENDER = {
    ('MALE','Male'),
    ('FEMALE','Female')
}

class Staff(AbstractUser):
    
    email = models.EmailField(_('email address'),  unique=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = CustomStaffManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=100)
    specializeArea = models.CharField("Area of specialisation + highest degree obtained", max_length=100)
    school = models.ForeignKey(College_schools, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    academicRank = models.IntegerField(default=0)
    appointmentDate = models.DateField()
    promotionDate = models.DateField()
    training = models.CharField("Plan for further training ( only applicable for TA, AL and Lecturers)-When will you register (Month/Year)", max_length=100)
    responsibilities = models.CharField("Administrative responsibilities (Director, Dean, HoD, Msc coordinator…)", max_length=100)
    teachingWorkload = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name