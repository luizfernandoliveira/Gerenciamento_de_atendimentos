# Generated by Django 4.0.1 on 2022-01-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concessionarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('contrato_suporte', models.BooleanField(default=False)),
                ('tipo_contrato', models.CharField(max_length=30)),
                ('data_final_contrato', models.DateField()),
                ('responsavel_manutencao', models.CharField(max_length=30)),
                ('telefone_responsavel', models.CharField(max_length=20)),
            ],
        ),
    ]