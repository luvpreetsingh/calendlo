# Generated by Django 2.2.10 on 2020-04-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200402_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendlouser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='calendlouser',
            name='first_name',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='calendlouser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='calendlouser',
            name='last_name',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
