# Generated by Django 2.0.4 on 2018-05-18 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0003_auto_20180425_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrition',
            name='fat_monounsaturated',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='fat_polyunsaturated',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='fat_saturated',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nutrition',
            name='fiber',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='ingredient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Ingredient'),
        ),
    ]
