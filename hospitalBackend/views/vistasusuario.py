from django.conf import settings
from rest_framework import status,views,generics
from rest_framework.response import Response
"from rest_framework_simplejwt.serializers import TokenObtainPairSerializer"
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
from hospitalBackend.models.usuario import Usuario



class UsuarioListAPIView(generics.ListAPIview):

    #Concrete view for listing a queryset or creating a model instance.
    
    queryset=Usuario.objetos.all()
    serializer_class=UsuarioSerializer
    "permissions_classes=(IsAuthenticated)"

    def get(self, request):
        print('Get a todos los Usuario')
        queryset=self.get_queryset()
        serializer=UsuarioSerializer(queryset, many=True)
        return (serializer.data)

   
class UsuarioRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    #Concrete view for retrieving, updating or deleting a model instance.
    
    queryset=Usuario.objetos.all()
    serializer_class=UsuarioSerializer
    lookup_field="id" #Campo con el que se realiza la busqueda los objetos
    lookup_url_kwarg="pk" #Nombre dado en la URL al argumento
    permissions_classes=(IsAuthenticated)

    def get(self, request, *args, **kwargs):
        print("GET a Usuario")
        """if valid.data['usuario.id'] != kwargs['pk']:
            stringResponse={'deatil':'Unauthorized Request'}
            return Response(stringResponse,status=status.Unauthorized.HTTP_401_UNAUTHORIZED) """       
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Usuario")
        """if valid.data['usuario.id'] != kwargs['pk']:
            stringResponse={'deatil':'Unauthorized Request'}
            return Response(stringResponse,status=status.Unauthorized.HTTP_401_UNAUTHORIZED) """  
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PATCH a Usuario")
        """if valid.data['usuario.id'] != kwargs['pk']:
            stringResponse={'deatil':'Unauthorized Request'}
            return Response(stringResponse,status=status.Unauthorized.HTTP_401_UNAUTHORIZED) """  
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("DELETE a Usuario")
        """ if valid.data['usuario.id'] != kwargs['pk']:
            stringResponse={'deatil'=Unauthorized.HTTP_401_UNAUTHORIZED}
        """
        return super().delete(request, *args, **kwargs)

