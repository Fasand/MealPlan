# Generated by Django 2.2.12 on 2020-05-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20200525_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipesection',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='sectiondirection',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='sectioningredient',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='recipesection',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectiondirection',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sectioningredient',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
    ]
