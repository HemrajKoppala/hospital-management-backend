from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer



class DoctorListCreateView(generics.ListCreateAPIView):

    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer

    def perform_destroy(self, instance):

        user = instance.user

        instance.delete()

        user.delete()