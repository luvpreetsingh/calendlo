# Generated by Django 2.2.10 on 2020-04-04 20:17

from django.db import migrations, models
import libs.validators


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabilityslot',
            name='end_time',
            field=models.TimeField(validators=[libs.validators.validate_absolute_hour]),
        ),
        migrations.AlterField(
            model_name='availabilityslot',
            name='start_time',
            field=models.TimeField(validators=[libs.validators.validate_absolute_hour]),
        ),
    ]