# Generated by Django 4.0.1 on 2022-01-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('test', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('track', models.CharField(max_length=20)),
            ],
        ),
    ]
