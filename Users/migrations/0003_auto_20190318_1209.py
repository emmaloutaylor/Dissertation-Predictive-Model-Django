# Generated by Django 2.1.3 on 2019-03-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20190310_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programme',
            name='notes',
        ),
        migrations.AddField(
            model_name='sets',
            name='notes',
            field=models.CharField(default='notes', max_length=1000),
        ),
    ]