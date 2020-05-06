# Generated by Django 2.2.4 on 2020-05-05 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Renter_Details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='Floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floor.floor'),
        ),
        migrations.AlterField(
            model_name='renter',
            name='Room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Room.room'),
        ),
    ]
