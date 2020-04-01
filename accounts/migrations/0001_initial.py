# Generated by Django 3.0.3 on 2020-04-01 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('citizenship', models.CharField(max_length=30)),
                ('passport_id', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('citizenship', models.CharField(max_length=30)),
                ('passport_id', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('street_address1', models.CharField(blank=True, max_length=50, null=True)),
                ('street_address2', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=40, null=True)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
