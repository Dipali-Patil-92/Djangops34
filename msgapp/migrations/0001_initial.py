# Generated by Django 5.0.6 on 2024-06-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mob', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('msg', models.CharField(max_length=300)),
            ],
        ),
    ]
