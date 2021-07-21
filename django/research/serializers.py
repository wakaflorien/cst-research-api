from rest_framework import serializers
from .models import *


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value




class ResearchSerializer(serializers.ModelSerializer):
    # chapters = ChapterBasedSerializer(many=True, read_only=True)
    # conferences = ConferenceSerializer(many=True, read_only=True)

    class Meta:
        model = Tbl_Research
        fields = '__all__'


class ConferenceSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = Tbl_conference

        fields = '__all__'


class ChapterBasedSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = Tbl_chap_based
        # fields = ['id', 'title', 'author', 'email']

        fields = '__all__'





class JournalTbSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = JournalTb
        fields = "__all__"      
    
class BookBasedSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = BookBased
        fields = "__all__"

class ColaboratorSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = Colaborator
        fields = "__all__"



class CommunityEngagementSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = CommunityEngagement
        fields = '__all__'

class MentorshipSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = MentorShip
        fields = '__all__'



class PeerReviewedInternationalSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = PeerReviewedInternational
        fields = '__all__'

class ResearchInnovationSerializer(serializers.ModelSerializer):
    research = ResearchSerializer(many=True, read_only=True)
    find = StringSerializer(many=False)
    class Meta:
        model = ResearchInnovation
        fields = '__all__'