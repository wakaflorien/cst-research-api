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
class Architecture_departments(models.Model):
    department_code = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(College_schools,  related_name='arcdepartments', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name

# Departments available in school of engineering
class engineering_departments(models.Model):
    department_code = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(College_schools,  related_name='engdepartments', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name

# Departments available in school of ICT
class ict_departments(models.Model):
    department_code = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(College_schools,  related_name='ictdepartments', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name

# Departments available in school of Science
class science_departments(models.Model):
    department_code = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(College_schools,  related_name='sciedepartments', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name

# Departments available in school of Mining and Geology
class mining_and_geology_departments(models.Model):
    department_code = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    school = models.ForeignKey(College_schools,  related_name='mindepartments', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.department_name


# ------------------------------------------------------------------------------------------------------
# Modules available in every Department of (School of Architecture)
# ------------------------------------------------------------------------------------------------------

class Construction_and_management_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(Architecture_departments, related_name='arcmodules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name
class Estate_management_and_valuation_models(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(Architecture_departments, related_name='arc2modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Geography_and_urban_planning_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(Architecture_departments, related_name='arc3modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Archtecture_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(Architecture_departments, related_name='arc4modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name



# ------------------------------------------------------------------------------------------------------
# Modules available in every Department of (School of Engineering)
# ------------------------------------------------------------------------------------------------------


class Electrical_and_Electronics_engineering_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(engineering_departments, related_name='engmodules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name
class MEE_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(engineering_departments, related_name='eng1modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Civil_environmental_and_geomatic_engineering_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(engineering_departments, related_name='eng2modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name



# ------------------------------------------------------------------------------------------------------
# Modules available in every Department of (School of ICT)
# ------------------------------------------------------------------------------------------------------

class Computer_and_software_engineering_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(ict_departments, related_name='ictmodules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name
class Information_Technology_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(ict_departments, related_name='ict1modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Information_systems_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(ict_departments, related_name='ict2modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Computer_sceince_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(ict_departments, related_name='ict3modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name



# ------------------------------------------------------------------------------------------------------
# Modules available in every Department of (School of Science)
# ------------------------------------------------------------------------------------------------------

class Biology_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(science_departments, related_name='sciemodules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name
class Chemistry_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(science_departments, related_name='scie1modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Mathematics_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(science_departments, related_name='scie2modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Physics_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(science_departments, related_name='scie3modules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

# ------------------------------------------------------------------------------------------------------
# Modules available in every Department of (School of Mining and Geology)
# ------------------------------------------------------------------------------------------------------

class Geology_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(mining_and_geology_departments, related_name='minmodules', on_delete=models.CASCADE)
    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name

class Mining_modules(models.Model):
    module_code = models.CharField(max_length=100)
    module_name = models.CharField(max_length=100)
    department = models.ForeignKey(mining_and_geology_departments, related_name='min1modules', on_delete=models.CASCADE)    # staff =  models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.module_name
