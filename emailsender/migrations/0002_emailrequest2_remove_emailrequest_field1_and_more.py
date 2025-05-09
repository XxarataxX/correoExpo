# Generated by Django 5.2 on 2025-04-11 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailsender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRequest2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(max_length=254)),
                ('nombre', models.TextField(blank=True, null=True)),
                ('telefono', models.TextField(blank=True, null=True)),
                ('empresa', models.TextField(blank=True, null=True)),
                ('stand', models.TextField(blank=True, null=True)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='emailrequest',
            name='field1',
        ),
        migrations.RemoveField(
            model_name='emailrequest',
            name='field2',
        ),
        migrations.RemoveField(
            model_name='emailrequest',
            name='field3',
        ),
        migrations.AddField(
            model_name='emailrequest',
            name='asunto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailrequest',
            name='mensaje',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailrequest',
            name='nombre',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='emailrequest',
            name='telefono',
            field=models.TextField(blank=True, null=True),
        ),
    ]
