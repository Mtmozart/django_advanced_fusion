# Generated by Django 4.2.1 on 2023-05-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foquete')], max_length=12, verbose_name='Icon'),
        ),
    ]