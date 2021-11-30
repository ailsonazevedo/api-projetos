# Generated by Django 3.2.9 on 2021-11-30 01:06

from django.db import migrations, models
import projetos.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetos',
            name='id',
        ),
        migrations.AddField(
            model_name='projetos',
            name='id_projeto',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='projetos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=projetos.models.upload_imagem_projeto),
        ),
    ]
