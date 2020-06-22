# Generated by Django 3.0 on 2020-06-22 18:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('designation', models.CharField(choices=[('prt', 'PRT')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('section', models.CharField(max_length=3)),
                ('subject', models.CharField(max_length=20)),
                ('no_students', models.IntegerField(default=0)),
                ('platform', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Report.Teacher')),
            ],
        ),
    ]
