# Generated by Django 2.0.3 on 2018-03-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trendingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsTag', models.CharField(max_length=15)),
                ('newsTagCode', models.CharField(max_length=10)),
                ('newsUrl', models.CharField(max_length=500)),
            ],
        ),
    ]