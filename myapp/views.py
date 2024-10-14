from django.shortcuts import render
from myapp.models import Contact
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.serializers import ContactSerializer


# Create your views here.
@csrf_exempt
def contact_list(request):
    if request.method == "GET":
        Contacts = Contact.objects.all()
        serializer = ContactSerializer(Contacts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def contact_detail(request, pk):
    try:
        dvar = Contact.objects.get(pk=pk)
    except dvar.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = ContactSerializer(dvar)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ContactSerializer(dvar, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        Contact.delete()
        return HttpResponse(status=204)
