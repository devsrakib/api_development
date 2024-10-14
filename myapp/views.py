from myapp.models import Contact
from myapp.serializers import ContactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET", "POST"])
def contact_list(request):
    if request.method == "GET":
        Mvar = Contact.objects.all()
        serializer = ContactSerializer(Mvar, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def contact_detail(request, pk):
    try:
        dvar = Contact.objects.get(pk=pk)
    except dvar.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = ContactSerializer(dvar)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ContactSerializer(dvar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        Contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
