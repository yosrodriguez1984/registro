# Generated by Django 3.1.5 on 2021-01-19 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210119_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('dias_clase', models.CharField(max_length=25)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sede')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
    ]
