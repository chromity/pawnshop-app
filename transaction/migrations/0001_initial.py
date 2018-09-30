# Generated by Django 2.1.1 on 2018-09-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PawnTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('middle_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=128)),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=1)),
                ('nationality', models.CharField(max_length=256)),
                ('contact_number', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=512)),
                ('date_time', models.DateTimeField()),
                ('code', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(max_length=2048)),
                ('karat', models.IntegerField(null=True)),
                ('grams', models.IntegerField(null=True)),
                ('percentage', models.FloatField(choices=[(0.04, '4%'), (0.05, '5%'), (0.06, '6%')])),
                ('price_value', models.FloatField()),
                ('number_of_days', models.FloatField()),
                ('a_value', models.FloatField()),
            ],
        ),
    ]
