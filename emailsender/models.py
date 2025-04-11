from django.db import models

class EmailRequest(models.Model):
    recipient = models.EmailField()  # Obligatorio (por defecto)
    nombre = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    asunto = models.TextField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EmailRequest to {self.recipient}"

class EmailRequest2(models.Model):
    recipient = models.EmailField()  # Obligatorio (por defecto)
    nombre = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    empresa = models.TextField(blank=True, null=True)
    stand = models.TextField(blank=True, null=True)
    mensaje = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EmailRequest2 to {self.recipient}"