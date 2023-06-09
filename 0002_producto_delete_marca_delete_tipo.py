# Generated by Django 4.0.4 on 2023-05-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('id_categoria', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
    ]
