# Generated by Django 3.0.5 on 2020-04-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]