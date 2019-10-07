from django.shortcuts import render
from rest_framework import status,permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from Test.models import *
# Create your views here.

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def product_get_post(request):
    if request.method =='GET':
        res=AllProducts.objects.all().values()
        return Response({'result':res},status.HTTP_200_OK)
    elif request.method == 'POST':
        p_name=request.data['p_name']
        p_quantity=request.data['p_quantity']
        p_price=request.data['p_price']
        p_des=request.data['p_des']
        obj = AllProducts(product_name=p_name,product_quantity=p_quantity,product_price=p_price,product_description=p_des)
        obj.save()
        return Response({'msg':'Successfully Saved'},status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes((permissions.AllowAny,))
def product_edit_delete(request,id):
    if request.method == 'PUT':
        print(request.data)
        re = AllProducts.objects.get(id=id)
        re.product_name = request.data['p_name']
        re.product_quantity = request.data['p_quantity']
        re.product_price = request.data['p_price']
        re.product_description = request.data['p_des']
        re.save()
        return Response({'msg':'Successfully Updated'},status.HTTP_200_OK)
    elif request.method == 'DELETE':
        re = AllProducts.objects.get(id=id)
        re.delete()
        return Response({'msg':'Successfully Deleted'},status.HTTP_200_OK)
    return Response(status.HTTP_400_BAD_REQUEST)

