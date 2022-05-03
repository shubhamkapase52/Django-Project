# Generated by Django 4.0.2 on 2022-03-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('birth_year', models.IntegerField()),
                ('mobile_no', models.IntegerField()),
            ],
        ),
    ]
