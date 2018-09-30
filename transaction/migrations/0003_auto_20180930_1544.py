# Generated by Django 2.1.1 on 2018-09-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_pawntransaction_current_month_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pawntransaction',
            name='current_month_days',
            field=models.IntegerField(choices=[(31, '31'), (30, '31'), (29, '29'), (28, '28')], default=31),
        ),
    ]
