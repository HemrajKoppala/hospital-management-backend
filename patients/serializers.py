from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Patient

User = get_user_model()


class PatientSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(source="user.email")

    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:

        model = Patient

        fields = [
            "id",
            "name",
            "email",
            "password",
            "date_of_birth",
            "gender",
            "phone",
            "address",
            "blood_group"
        ]

    def create(self, validated_data):

        user_data = validated_data.pop("user")

        email = user_data["email"]

        password = validated_data.pop("password")

        username = email.split("@")[0]

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password,

            role="PATIENT"

        )

        patient = Patient.objects.create(

            user=user,

            **validated_data

        )

        return patient