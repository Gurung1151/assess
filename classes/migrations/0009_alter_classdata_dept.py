# Generated by Django 4.0.3 on 2022-03-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_assessmentmarks_is_approved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdata',
            name='dept',
            field=models.CharField(blank=True, choices=[('BCT', 'BCT'), ('BEL', 'BEL'), ('BEX', 'BEX'), ('BEI', 'BEI')], max_length=200),
        ),
    ]