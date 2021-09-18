from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# from staff.models import Staff
#Teaching in higher learning institution certificate (THLIC)
class THLIC_Certificate(models.Model):

    """
    Staff Name
    Staff Gender
    Area of specialisation
    Department
    School/ Centre
    Certificate obtained (Yes or No)

    
    """
    def generate_pk():
            counter=0
            counter = THLIC_Certificate.objects.count()
            counter += 1
            return 'THLIC'+str(counter)

    certificate_id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    certificate_name = models.CharField(max_length=100)
    certificate_obtained_Yes_Or_No = models.BooleanField(default=False)
    date = models.DateField()
    staff = models.ForeignKey(get_user_model(), default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.certificate_name


# Teaching portofolio  (TP)

class Teaching_portofolio(models.Model):

    """
    Staff Name
    Staff Gender
    Area of specialisation
    Department
    School/ Centre
    TP Developed (Yes or No)
    """

    def generate_pk():
            counter=0
            counter = Teaching_portofolio.objects.count()
            counter += 1
            return 'TP'+str(counter)

    certificate_id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    TP_name = models.CharField(max_length=100)
    TP_Developed = models.BooleanField(default=False)
    date = models.DateField()
    staff = models.ForeignKey(get_user_model(), default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.TP_name 