# Generated by Django 4.2.5 on 2023-09-16 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo', models.CharField(blank=True, max_length=4, null=True)),
                ('active', models.BooleanField(default=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogos.pais')),
            ],
        ),
    ]
