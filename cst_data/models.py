from django.db import models
# from .models import User,

# -------------------------------------Schools-----------------------------------------
# Schools available in CST college
class College_schools(models.Model):
    school_code = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)


    def __str__(self):
        return self.school_name
# -------------------------------------Departments from different schools-----------------------------------------
# Departments available in school of architecture
class Departments(models.Model):
    department_code = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(College_schools,  related_name='College_schools', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name

# Departments available in school of engineering
class Modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    school = models.ForeignKey(Departments,  related_name='Departments', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name
