# Generated by Django 4.1.2 on 2022-12-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ename', models.CharField(max_length=20)),
                ('EmpId', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
