# Generated by Django 4.0.3 on 2022-03-09 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_alter_classdata_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdata',
            name='Section',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
