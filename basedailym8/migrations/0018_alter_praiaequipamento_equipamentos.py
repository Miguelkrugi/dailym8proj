# Generated by Django 4.1.1 on 2022-10-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedailym8', '0017_praiaequipamento_equipamentos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praiaequipamento',
            name='equipamentos',
            field=models.IntegerField(default=300),
        ),
    ]
