# Generated by Django 4.1.4 on 2023-03-30 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_textbooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbooks',
            name='book',
            field=models.FileField(default=0, upload_to='pdf'),
            preserve_default=False,
        ),
    ]