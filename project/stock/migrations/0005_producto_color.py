# Generated by Django 5.0.4 on 2024-06-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_talle_remove_producto_contenido_producto_talle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='color',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
