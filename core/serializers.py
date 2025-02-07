from rest_framework import serializers
from .models import Student, Supervisor, Admin, FieldPlacement

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class FieldPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldPlacement
        fields = '__all__'
