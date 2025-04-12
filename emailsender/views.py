from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmailRequestSerializer, EmailRequest2Serializer
from .models import EmailRequest, EmailRequest2
class ContactoGeneralView(APIView):
    def post(self, request):
        serializer = EmailRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            # Guardar en la base de datos
            try:
                email_request = EmailRequest.objects.create(
                    recipient=data['recipient'],
                    nombre=data.get('nombre', ''),
                    telefono=data.get('telefono', ''),
                    asunto=data.get('asunto', ''),
                    mensaje=data.get('mensaje', '')
                )
            except Exception as db_error:
                return Response({"error": f"Error al guardar en BD: {str(db_error)}"}, 
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            # Construir y enviar email
            subject = "Confirmación de contacto"
            message = f"""
            Hola {data.get('nombre', '')},
            
            Gracias por contactarnos. Hemos recibido tu información y nos pondremos en contacto contigo a la brevedad.
            
            Atentamente,
            El equipo de soporte
            """
            
            try:
                send_mail(
                    subject,
                    message,
                    'sistema_de_servicios@solucionesdsi.com',
                    [data['recipient']],
                    fail_silently=False,
                )
                return Response({
                    "status": "Email de confirmación enviado",
                    "id_registro": email_request.id
                }, status=status.HTTP_200_OK)
            except Exception as email_error:
                # Si falla el email pero se guardó en BD, informamos igual
                return Response({
                    "status": "Registro guardado pero falló el envío de email",
                    "error": str(email_error),
                    "id_registro": email_request.id
                }, status=status.HTTP_207_MULTI_STATUS)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InformacionStandView(APIView):
    def post(self, request):
        serializer = EmailRequest2Serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            # Guardar en la base de datos
            try:
                email_request = EmailRequest2.objects.create(
                    recipient=data['recipient'],
                    nombre=data.get('nombre', ''),
                    telefono=data.get('telefono', ''),
                    empresa=data.get('empresa', ''),
                    stand=data.get('stand', ''),
                    mensaje=data.get('mensaje', '')
                )
            except Exception as db_error:
                return Response({"error": f"Error al guardar en BD: {str(db_error)}"}, 
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            # Construir y enviar email
            subject = "Confirmación - Información de Stand"
            message = f"""
            Hola {data.get('nombre', '')},
            
            Gracias por tu interés en nuestro stand. Hemos recibido tu solicitud y nos contactaremos contigo pronto.
            
            Atentamente,
            El equipo de stands
            """
            
            try:
                send_mail(
                    subject,
                    message,
                    'sistema_de_servicios@solucionesdsi.com',
                    [data['recipient']],
                    fail_silently=False,
                )
                return Response({
                    "status": "Email de confirmación enviado",
                    "id_registro": email_request.id
                }, status=status.HTTP_200_OK)
            except Exception as email_error:
                # Si falla el email pero se guardó en BD, informamos igual
                return Response({
                    "status": "Registro guardado pero falló el envío de email",
                    "error": str(email_error),
                    "id_registro": email_request.id
                }, status=status.HTTP_207_MULTI_STATUS)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)