# Generated by Django 2.0.7 on 2018-10-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectCentricMail', '0003_auto_20181008_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('projectname', models.CharField(max_length=32)),
            ],
        ),
    ]
