from rest_framework import serializers
from .models import Job, Requirement

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class RequirementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'