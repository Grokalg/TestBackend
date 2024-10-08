# Generated by Django 4.2.10 on 2024-08-20 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Стоимость'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='courses.course'),
            preserve_default=False,
        ),
    ]
