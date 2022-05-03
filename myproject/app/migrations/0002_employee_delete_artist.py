# Generated by Django 4.0.4 on 2022-04-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('Email_id', models.CharField(max_length=250)),
                ('Role', models.CharField(max_length=250)),
                ('mobile_no', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
