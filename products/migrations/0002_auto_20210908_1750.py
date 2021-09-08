# Generated by Django 3.2.5 on 2021-09-08 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_product_id', models.SlugField(default='', max_length=100)),
                ('images', models.FileField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='image',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='images',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.imagemodel'),
        ),
    ]