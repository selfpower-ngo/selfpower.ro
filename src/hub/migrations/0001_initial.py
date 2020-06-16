# Generated by Django 2.0 on 2019-03-21 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'carte',
                'verbose_name_plural': 'carti',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='hubImages/')),
            ],
        ),
        migrations.CreateModel(
            name='Proiect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('slug', models.SlugField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Proiecte',
            },
        ),
        migrations.CreateModel(
            name='Resursa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('videoUrl', models.CharField(blank=True, max_length=300)),
                ('profile', models.FileField(upload_to='hubImages/')),
            ],
            options={
                'verbose_name_plural': 'resurse',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='proiect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hub.Proiect'),
        ),
        migrations.AddField(
            model_name='bookurl',
            name='resursa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hub.Resursa'),
        ),
    ]
