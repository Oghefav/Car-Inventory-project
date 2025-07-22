from rest_framework import serializers
from user.models import CustomAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.settings import api_settings



class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta: 
        model = CustomAdminUser
        fields = ['id','username', 'last_name', 'first_name', 'email']


class AdminRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)


    class Meta:
        model = CustomAdminUser
        fields = ['username', 'last_name', 'first_name', 'email', 'password', 'confirm_password']
    
    def validate(self, data):
        if data['confirm_password'] != data['password']:
            raise serializers.ValidationError('passwords do not match')
        return data
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomAdminUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

        
class AdminLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
       data = super().validate(attrs)

       refresh = self.get_token(self.user)
       access = refresh.access_token

       data['user'] = UserSerializer(self.user).data
       data['access'] = str(access)
       data['refresh'] = str(refresh)

       if api_settings.UPDATE_LAST_LOGIN:
        update_last_login(None, self.user)
        return data
       
       return data