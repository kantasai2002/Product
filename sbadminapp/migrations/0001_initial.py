# Generated by Django 4.2.7 on 2023-11-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('uemail', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
            ],
        ),
    ]
