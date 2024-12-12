from rest_framework import serializers
from .models import Category, Institution, User, Role

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Invalid email address")
        return value

    class Meta:
        model = User
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
