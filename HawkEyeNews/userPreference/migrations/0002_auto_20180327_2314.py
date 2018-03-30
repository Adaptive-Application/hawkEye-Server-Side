# Generated by Django 2.0.3 on 2018-03-27 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userPreference', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=20)),
                ('categoryCode', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategoryName', models.CharField(max_length=20)),
                ('subcategoryCode', models.IntegerField(default=None)),
                ('category_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userPreference.category')),
            ],
        ),
        migrations.RemoveField(
            model_name='userpreference',
            name='preferenceName',
        ),
        migrations.AddField(
            model_name='userpreference',
            name='preferenceCode',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='userpreference',
            name='userId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
