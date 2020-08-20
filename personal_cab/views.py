from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializer import *


# Create your views here.

class Exp_view(APIView):

    def get(self, request):
        expenses = Expenses.objects.all()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response({"expenses": serializer.data})

    def post(self,request):
        expenses = request.data.get('expenses')

        serializer = ExpensesSerializer(data=expenses)
        if serializer.is_valid(raise_exception=True):
            expense_saved = serializer.save()

        return Response({"success": "Expenses '{}' were created successfully".format(expense_saved.exp_title)})


    def put(self, request, pk):
        saved_exp = get_object_or_404(Expenses.objects.all(), pk=pk)
        data = request.data.get('expenses')
        serializer = ExpensesSerializer(instance=saved_exp, data=data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            saved_exp = serializer.save()
        
        return Response({"Success": "Expenses '{}' updated successfully".format(saved_exp.exp_title)})

    def delete(self, request, pk):
        #Get object with this pk
        expenses = get_object_or_404(Expenses.objects.all(), pk=pk)
        expenses.delete()
        return Response({"Success": "Expenses '{}' has been deleted".format(pk)}, status=204)


# Косяк, надо исправить! 
@csrf_exempt
def expense_detail(request,pk):
    try:
        expense = Expenses.objects.get(pk=pk)
    except Expenses.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ExpensesSerializer(expense)
        return JsonResponse(serializer.data)


    
class ODRView(APIView):

    def get(self, request):
        odrs = ODR.object.all()
        serializer = ODRSerializer(odrs, many=True)
        return Response({"odrs": serializer.data})


    def post(self, request):
        expenses = request.data.get('expenses')

        serializer = ExpensesSerializer(data=expenses)
        serializer = ExpensesSerializer(data=expenses)

        return print(serializer)