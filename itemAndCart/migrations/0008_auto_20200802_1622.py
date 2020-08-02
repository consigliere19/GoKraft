# Generated by Django 3.0.5 on 2020-08-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemAndCart', '0007_auto_20200802_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='saving',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='saving',
            field=models.FloatField(default=0),
        ),
    ]
