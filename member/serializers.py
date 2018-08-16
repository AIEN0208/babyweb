from rest_framework import serializers
import member.models as models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = ('UserId', 'UserName', 'UserEmail', 'UserPassword')
