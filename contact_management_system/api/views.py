from rest_framework.response import Response
from rest_framework.decorators import api_view
from contacts.models import Contact
from .serializers import ContactSerializer
from django.contrib.auth.models import User
from rest_framework import status

@api_view(['GET'])
def get_data(request):
    # person = {'name':'srijon','age':25}
    user = User.objects.get(id=1)
    contacts_list = Contact.objects.all()
   
    serializer = ContactSerializer(contacts_list,many=True)
    return Response(serializer.data)
@api_view(['POST'])
def add_contact(request):
    data = request.data
    data['user'] = request.user.pk
    serializer = ContactSerializer(data=data)
    # if not serializer.is_valid():
    #     errors = serializer.errors
    #     print(errors)
    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def update_contact(request,pk):
    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
    data = request.data
    data['user'] = request.user.pk
    serializer = ContactSerializer(instance=contact,data=data)
    # serializer = ContactSerializer(instance=contact, data=request.data, partial=True) for partial update field
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def delete_contact(request,pk):
    try:
        contact = Contact.objects.get(id=pk)
        contact.delete()
        return Response({"message": "Contact deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Contact.DoesNotExist:
        return Response({"error": "Contact not found"}, status=status.HTTP_404_NOT_FOUND)
    