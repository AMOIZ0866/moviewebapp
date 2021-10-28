# Generated by Django 3.2.8 on 2021-10-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieweb', '0010_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=20, unique=True)),
                ('shortdesc', models.CharField(max_length=20, unique=True)),
                ('longdesc', models.CharField(max_length=250, unique=True)),
                ('review', models.CharField(max_length=250)),
                ('vurl', models.CharField(max_length=250)),
                ('imageurl', models.CharField(max_length=250)),
                ('mrating', models.FloatField(max_length=20)),
                ('creation_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
            ],
        ),
    ]