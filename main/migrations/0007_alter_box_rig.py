# Generated by Django 4.2.11 on 2024-04-24 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_package_reserved_box_reserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='rig',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='box_rigs', to='main.rig'),
        ),
    ]
