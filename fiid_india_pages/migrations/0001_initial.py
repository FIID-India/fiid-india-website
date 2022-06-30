# Generated by Django 3.2 on 2022-06-30 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='images/carousel/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('file', models.FileField(upload_to='files/')),
                ('file_type', models.CharField(choices=[('Report', 'Report'), ('Newsletter', 'Newsletter'), ('Others', 'Others')], default='Newsletter', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/pages/')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiid_india_pages.page')),
            ],
        ),
    ]
