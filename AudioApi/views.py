from rest_framework import generics
from .serializers import AudioBookSerializers 
from .models import AudioBookFields
from rest_framework.response import Response
from rest_framework import status



class AudioBookList(generics.ListAPIView):
    queryset =  AudioBookFields.objects.all()
    serializer_class = AudioBookSerializers 
    if queryset is True:
         Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
         Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        

   

class AudioBookCreate(generics.CreateAPIView):
    queryset =  AudioBookFields.objects.all()
    serializer_class = AudioBookSerializers 
    if queryset is True:
         Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
         Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class AudioBookRetrieve(generics.RetrieveAPIView):
    queryset =  AudioBookFields.objects.all()
    serializer_class = AudioBookSerializers 
    if queryset is True:
         Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
         Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


class AudioBookDelete(generics.RetrieveDestroyAPIView):
    queryset =  AudioBookFields.objects.all()
    serializer_class = AudioBookSerializers 
    if queryset is True:
         Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
         Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)



class AudioBookUpdate(generics.RetrieveUpdateAPIView):
    queryset =  AudioBookFields.objects.all()
    serializer_class = AudioBookSerializers 
    if queryset is True:
         Response(serializer_class.data, status=status.HTTP_200_OK)
    else:
         Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


    

