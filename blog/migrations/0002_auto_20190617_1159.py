# Generated by Django 2.2.2 on 2019-06-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='foto',
            field=models.FileField(upload_to='media/$Y/$m/$d/'),
        ),
    ]
