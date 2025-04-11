from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmailRequestSerializer, EmailRequest2Serializer

class ContactoGeneralView(APIView):
    def post(self, request):
        serializer = EmailRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            # Construir mensaje para el destinatario
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
                    'sistema_de_servicios@solucionesdsi.com',  # Cambiar por tu email de envío
                    [data['recipient']],
                    fail_silently=False,
                )
                return Response({"status": "Email de confirmación enviado"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InformacionStandView(APIView):
    def post(self, request):
        serializer = EmailRequest2Serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            # Construir mensaje para el destinatario
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
                    'sistema_de_servicios@solucionesdsi.com',  # Cambiar por tu email de envío
                    [data['recipient']],
                    fail_silently=False,
                )
                return Response({"status": "Email de confirmación enviado"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)