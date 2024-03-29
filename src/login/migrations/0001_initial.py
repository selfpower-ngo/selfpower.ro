# Generated by Django 2.0 on 2019-03-21 16:58

import datetime
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
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPaymentStatusActive', models.BooleanField(default=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('membership_type', models.CharField(choices=[('Free', 'free'), ('VIP', 'vip')], default='Free', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Abonament (membership)',
                'verbose_name_plural': 'Abonamente (memberships)',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayingContactInfo', models.BooleanField(default=True)),
                ('phoneNo', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profil de utilizator (User Profiles)',
                'verbose_name_plural': 'Profile de utilizator (User Profiles)',
            },
        ),
    ]
