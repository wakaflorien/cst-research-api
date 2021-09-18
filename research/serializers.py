from rest_framework import serializers
from .models import *


class ResearchSerializer(serializers.ModelSerializer):
    staff = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = Tbl_Research
        fields = '__all__'


class ConferenceSerializer(serializers.ModelSerializer):
    staff = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = Tbl_conference

        fields = '__all__'


class ChapterBasedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tbl_chap_based
        # fields = ['id', 'title', 'author', 'email']

        fields = '__all__'

class JournalTbSerializer(serializers.ModelSerializer):
    staff = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = JournalTb
        fields = "__all__"      
    
class BookBasedSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookBased
        fields = "__all__"

class ColaboratorSerializer(serializers.ModelSerializer):
    staff = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Colaborator
        fields = "__all__"



class CommunityEngagementSerializer(serializers.ModelSerializer):
    staff = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = CommunityEngagement
        fields = '__all__'

class MentorshipSerializer(serializers.ModelSerializer):
    staff = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = MentorShip
        fields = '__all__'



class PeerReviewedInternationalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PeerReviewedInternational
        fields = '__all__'

class ResearchInnovationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResearchInnovation
        fields = '__all__'

class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = '__all__'

class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityEngagement
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = MentorShip
        fields = '__all__'
        