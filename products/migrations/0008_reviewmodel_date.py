# Generated by Django 3.2.7 on 2021-09-16 21:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_reviewmodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]