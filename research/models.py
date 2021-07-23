from django.db import models
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
import random
from django.utils import timezone
from isbn_field import ISBNField
from djmoney.models.fields import MoneyField



class Tbl_Research(models.Model):

        def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'PRJA'+str(counter)

        id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
        research_title = models.CharField(max_length=100)
        starting_date = models.DateTimeField(auto_now_add=True)
        ending_date = models.DateTimeField(auto_now_add=True)
        # amount = models.FloatField()
        amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
        status = models.CharField(max_length=20)
        # staff = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

        def __str__(self):
            return self.research_title


class Tbl_conference(models.Model):

    
    def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'PRJA'+str(counter)

    research = models.ForeignKey(Tbl_Research, on_delete=models.CASCADE)
    confer_id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    confer_name = models.CharField(max_length=100)
    author = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    no_of_pages = models.CharField(max_length=100)
    # ISBN = models.CharField(max_length=100)
    isbn = ISBNField(clean_isbn=False, null=True)
    research = models.ForeignKey(Tbl_Research, on_delete=models.CASCADE)

    def __str__(self):
        return self.confer_name

class Tbl_chap_based(models.Model):

    def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'RBB'+str(counter)

    research = models.ForeignKey(Tbl_Research, on_delete=models.CASCADE)
    chap_based_id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    chapter_title = models.CharField(max_length=100)
    author = models.EmailField(max_length=100)
    publication_year = models.DateTimeField(auto_now_add=True)
    book_title = models.CharField(max_length=100)
    chap_pages = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
    no_of_pages = models.CharField(max_length=100)
    # ISBN = models.CharField(max_length=100)
    ISBN = ISBNField(clean_isbn=False)
    research = models.ForeignKey(Tbl_Research, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_title


class BookBased(models.Model):
    # def validate_date(date):
    #  if date > models.timezone.now().date():
    #     raise ValidationError ("Research publication cannot be done in the future")

    def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'RBB'+str(counter)

    research = models.ForeignKey(Tbl_Research, on_delete=models.CASCADE)
    alphabetic = RegexValidator(r'[A-Za-z ]+', 'Only alphabetic characters are allowed.')
    bookbased_id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    title = models.CharField(max_length= 100,  validators = [alphabetic])
    author = models.CharField(max_length= 100, validators = [alphabetic])
    publication_year = models.DateField(null=False, blank=False)
    editor = models.CharField(max_length= 100)
    publisher = models.CharField(max_length= 100)
    place = models.CharField(max_length= 100)
    pages = models.PositiveSmallIntegerField()
    # isbn = models.CharField(max_length= 100)
    isbn = ISBNField(clean_isbn=False)


    def __str__(self):
        return self.title



class JournalTb(models.Model):
    # def validate_date(date):
    #  if date > models.timezone.now().date():
    #     raise ValidationError ("Research publication cannot be done in the future")

    def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'PRJA'+str(counter)

    # research = models.ForeignKey(Tbl_Research, on_delete=models.CASCADE)
    alphabetic = RegexValidator(r'[A-Za-z ]+', 'Only alphabetic characters are allowed.')
    journal_id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    title = models.CharField(max_length= 100, validators = [alphabetic])
    author = models.CharField(max_length= 100,  validators = [alphabetic])
    publication_year = models.DateField(null=False, blank=False)
    journal = models.CharField(max_length= 100)
    Volume = models.CharField(max_length= 100)
    series = models.CharField(max_length= 100)
    publisher = models.CharField(max_length= 100)
    pages = models.PositiveSmallIntegerField()
    issn= models.CharField(max_length= 100)
    impact_factor = models.TextField()

    def __str__(self):
        return self.title


class Colaborator(models.Model):

    def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'PRJA'+str(counter)

    colaborator_id = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    # staff = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    research = models.ManyToManyField(Tbl_Research)
    # name = models.CharField(max_length= 100, default= "your name")

    def __str__(self):
        return self.name



class CommunityEngagement(models.Model):

    def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'CA'+str(counter)

    engagementId = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    specializedArea = models.CharField(max_length=100)
    communityActivity = models.CharField(max_length=100)
    output = models.CharField(max_length=200)
    planEngagementUsed = models.CharField(max_length=200)
    # staff = models.ForeignKey(get_user_model(),
    #                             on_delete=models.CASCADE)

    def __str__(self):
        return self.output


class MentorShip(models.Model):

    def generate_pk():
            counter=0
            counter = Tbl_Research.objects.count()
            counter += 1
            return 'PGSM'+str(counter)

    mentorshipId = models.CharField(default=generate_pk, primary_key=True, max_length=255, unique=True)
    level = models.CharField(max_length=100)
    projectTitle = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    # staff = models.ForeignKey(get_user_model(),
    #                             on_delete=models.CASCADE)

    def __str__(self):
        return self.projectTitle



#---------------------------------------------------------------------------------


class Authors(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name 

class PeerReviewedInternational(models.Model):
    
    COLLEGE = {

    ('CST','COLLEGE OF SCIENCE AND TECHNOLOGY'),
    ('CBE','COLLEGE OF BUSINESS AND ECONOMY')

    }
    def sn():
        counter=0
        counter = PeerReviewedInternational.objects.count()
        counter +=1

        return "PRIRC"+ str(counter)

    serialNumber = models.CharField(default=sn, primary_key=True, max_length=200, unique=True)
    # staff = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    college = models.CharField(choices=COLLEGE, max_length=100)
    # authors = models.ManyToManyField(Authors)
    nameOfConference = models.CharField(max_length=100)
    organizer = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    datesOfPublication = models.DateField(default=timezone.now)
    place = models.CharField(max_length=100)
    editor = models.CharField(max_length=30)
    noOfPages = models.IntegerField(default=0)
    isbn = ISBNField(clean_isbn=False)

    def __str__(self):
        return self.serialNumber

class ResearchInnovation(models.Model):
    def sn():
        counter=0
        counter = ResearchInnovation.objects.count()
        counter +=1

        return "RPC"+ str(counter)

    serialNumber = models.CharField(default=sn, primary_key=True, max_length=200, unique=True)
    # staff = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    research = models.ForeignKey(Tbl_Research, on_delete=models.CASCADE)
    fundingResource = models.CharField(max_length=50)
    fundingAmount = MoneyField(max_digits=14, decimal_places=2, default_currency='RWF')
    collaborators = models.ManyToManyField(Colaborator)

    def __str__(self):
        return self.serialNumber





