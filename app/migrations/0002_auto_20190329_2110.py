# Generated by Django 2.1.7 on 2019-03-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('year', models.CharField(max_length=100, null=True)),
                ('rating', models.CharField(max_length=100, null=True)),
                ('img_url', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('year', models.CharField(max_length=100, null=True)),
                ('rating', models.CharField(max_length=100, null=True)),
                ('img_url', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='moviesandtv',
        ),
    ]
