# Generated by Django 2.0.1 on 2018-02-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180223_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='start',
            field=models.DateField(null=True),
        ),
    ]
