# Generated by Django 4.1.7 on 2023-03-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizza', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='./img/'),
        ),
    ]