from django.shortcuts import render
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from restapi import models, serializers

# Create your views here.


class ExpenseListCreate(ListCreateAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()


class ExpenseRetrieveDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.Expense
    queryset = models.Expense.objects.all()
