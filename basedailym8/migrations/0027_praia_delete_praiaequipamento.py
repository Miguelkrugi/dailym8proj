# Generated by Django 4.1.1 on 2022-10-18 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0026_remove_praiaequipamento_stock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Praia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('NumeroEquipamentos', models.IntegerField(default='', null=True)),
                ('reserva', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='basedailym8.reserva')),
            ],
        ),
        migrations.DeleteModel(
            name='PraiaEquipamento',
        ),
    ]