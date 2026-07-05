from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Doctor

User = get_user_model()


class DoctorSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(write_only=True)

    password = serializers.CharField(
        write_only=True
    )

    class Meta:

        model = Doctor

        fields = [
            'id',
            'name',
            'email',
            'password',
            'specialization',
            'qualification',
            'experience',
            'phone',
            'department',
            'consultation_fee',
            'available'
        ]

    def create(self, validated_data):

        email = validated_data.pop('email')
        password = validated_data.pop('password')

        username = email.split("@")[0]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role="DOCTOR"
        )

        doctor = Doctor.objects.create(
            user=user,
            **validated_data
        )

        return doctor
    
    def update(self, instance, validated_data):

        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)

        user = instance.user

        if email:
            user.email = email

        if password:
            user.set_password(password)

        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance