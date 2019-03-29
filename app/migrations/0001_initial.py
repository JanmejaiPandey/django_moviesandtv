# Generated by Django 2.1.7 on 2019-03-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviesandtv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('year', models.DecimalField(decimal_places=0, max_digits=4, null=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('img_url', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]