# Generated by Django 2.0.3 on 2018-12-21 05:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staj', '0024_auto_20181218_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mulakat',
            name='duzen',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Düzen'),
        ),
        migrations.AlterField(
            model_name='mulakat',
            name='icerik',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='mulakat',
            name='mulakat_degerlendirmesi',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Mülakat'),
        ),
        migrations.AlterField(
            model_name='mulakat',
            name='proje',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Proje'),
        ),
        migrations.AlterField(
            model_name='mulakat',
            name='staj',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staj.Staj'),
        ),
        migrations.AlterField(
            model_name='mulakat',
            name='sunum',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Sunum'),
        ),
    ]
