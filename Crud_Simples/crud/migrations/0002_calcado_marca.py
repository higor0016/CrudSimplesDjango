# Generated by Django 5.0.4 on 2024-05-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcado',
            name='marca',
            field=models.TextField(default=str, max_length=100, verbose_name='Marca'),
            preserve_default=False,
        ),
    ]