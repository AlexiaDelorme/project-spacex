# Generated by Django 3.0.3 on 2020-06-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingreference',
            name='order_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]