from django.contrib import admin

# Register your models here.
from emailsender.models import EmailRequest, EmailRequest2

admin.site.register(EmailRequest)

admin.site.register(EmailRequest2)

