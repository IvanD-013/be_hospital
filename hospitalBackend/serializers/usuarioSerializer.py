
from hospitalBackend.models.usuario import Usuario
from rest_framework import serializers
class UsuarioSerializer(serializers.ModelSerializer):
 class Meta:
     model = Usuario
     fields = ['id', 'rol','nombre','apellido','celular','email','direccion','username','password']