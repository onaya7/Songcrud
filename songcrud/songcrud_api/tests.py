from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase,APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongSerializer


#tests for views

# class BaseViewTest(APITestCase):
#     client = APIClient()


