# Generated by Django 4.1.1 on 2022-10-18 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0028_remove_praia_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praia',
            name='reserva',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.reserva'),
        ),
    ]