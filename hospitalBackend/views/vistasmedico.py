from urllib.request import Request
from django.conf import settings
from rest_framework import status,views,generics
from rest_framework.response import Response
"from rest_framework_simplejwt.serializers import TokenObtainPairSerializer"
from hospitalBackend.serializers.medicoSerializer import MedicoSerializer
from hospitalBackend.serializers.usuarioSerializer import UsuarioSerializer
#Empleamos el serilizador de la clase Usuario por que como vamos a manipular el modelo "Usuario"  para crear a travez de la URL del 
#medico usuarios ,por esa razon debemos tener en cuenta el serializador para usarlo mas adelante
from hospitalBackend.models.medico import Medico



class MedicoListCreateAPIView(generics.ListCreateAPIView):
   
    #Concrete view for listing a queryset or creating a model instance.
    
    queryset=Medico.objects.all()
    serializer_class=MedicoSerializer
    "permissions_classes=(IsAuthenticated)"

    def get(self, request):
        print('Get a Medico')
        queryset=self.get_queryset()
        serializer=MedicoSerializer(queryset, many=True)
        return (serializer.data)
    def post(self,request):
        print('POST a todos los Medico')
        print(Request.data)
        usuarioData=request.data.pop('usuario')
        serializerU=UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario=serializerU.save()
        enfData=request.data
        enfData.update({"usuario":usuario.id})
        serializerEnf=MedicoSerializer(data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)

        """tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)"""
   
class MedicoRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    queryset=Medico.objects.all()
    serializer_class=MedicoSerializer
    lookup_field="id" #Campo con el que se realiza la busqueda los objetos
    lookup_url_kwarg="pk" #Nombre dado en la URL al argumento
    """permissions_classes=(IsAuthenticated)"""

    def get(self, request, *args, **kwargs):
        print("GET a Medico")
        """if valid.data['usuario.id'] != kwargs['pk']:
            stringResponse={'deatil':'Unauthorized Request'}
            return Response(stringResponse,status=status.Unauthorized.HTTP_401_UNAUTHORIZED) """       
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Medico")
        """if valid.data['usuario.id'] != kwargs['pk']:
            stringResponse={'deatil':'Unauthorized Request'}
            return Response(stringResponse,status=status.Unauthorized.HTTP_401_UNAUTHORIZED) """  
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        print("PATCH a Medico")
        """if valid.data['usuario.id'] != kwargs['pk']:
            stringResponse={'deatil':'Unauthorized Request'}
            return Response(stringResponse,status=status.Unauthorized.HTTP_401_UNAUTHORIZED) """  
        return super().patch(request, *args, **kwargs)



