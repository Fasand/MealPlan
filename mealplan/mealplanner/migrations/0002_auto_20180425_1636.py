# Generated by Django 2.0.4 on 2018-04-25 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mealplanner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='nutrition',
        ),
        migrations.AddField(
            model_name='nutrition',
            name='ingredient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='preferred_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mealplanner.Unit'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mealplanner.Tag'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mealplanner.Tag'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='belongs_to_ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Ingredient'),
        ),
    ]