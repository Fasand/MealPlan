# Generated by Django 2.0.4 on 2018-04-24 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('unit_type', models.CharField(choices=[('g', 'g (weight)'), ('ml', 'ml (volume)')], default='g', max_length=2)),
                ('price', models.FloatField(blank=True, default=0.0)),
                ('description', models.TextField(blank=True, default='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mealplanner.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.FloatField(blank=True, null=True)),
                ('fat', models.FloatField(blank=True, null=True)),
                ('carbs', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('servings', models.PositiveSmallIntegerField()),
                ('prep_time', models.DurationField()),
                ('cook_time', models.DurationField()),
                ('directions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_type', models.CharField(choices=[('g', 'g (weight)'), ('ml', 'ml (volume)')], default='g', max_length=2)),
                ('value', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('shorthand', models.CharField(max_length=20)),
                ('belongs_to_ingredient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mealplanner.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mealplanner.Unit'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='mealplanner.RecipeIngredient', to='mealplanner.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='mealplanner.Tag'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='nutrition',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='mealplanner.Nutrition'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='preferred_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mealplanner.Unit'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='tags',
            field=models.ManyToManyField(to='mealplanner.Tag'),
        ),
    ]