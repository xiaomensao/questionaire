# Generated by Django 2.2.5 on 2020-05-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questionaires', '0009_auto_20200502_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionaire',
            name='description',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
