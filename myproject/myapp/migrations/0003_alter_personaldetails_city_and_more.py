# Generated by Django 4.1.4 on 2023-03-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_personaldetails_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails',
            name='city',
            field=models.CharField(default='city', max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='date_of_birth',
            field=models.CharField(default='00/00/0000', max_length=50),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='gender',
            field=models.CharField(default='gender', max_length=10),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='phone_number',
            field=models.CharField(default='phone_number', max_length=20),
        ),
    ]
