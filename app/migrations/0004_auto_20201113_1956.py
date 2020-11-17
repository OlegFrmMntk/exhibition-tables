# Generated by Django 3.1.2 on 2020-11-13 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201028_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibition',
            name='artist',
        ),
        migrations.AddField(
            model_name='exhibition',
            name='artwork',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.artwork'),
        ),
    ]