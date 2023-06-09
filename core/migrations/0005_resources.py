# Generated by Django 4.2.1 on 2023-05-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_employee_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Creation')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modification')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('title', models.CharField(max_length=25, verbose_name='Title')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('icon', models.CharField(choices=[('lni-rocket', 'Bootstrap 4'), ('lni-laptop-phone', 'Responsividade'), ('lni-cog', 'HTML, CCS3 & SASS'), ('lni-leaf', 'Design moderno'), ('lni-layers', 'Multifuncionalidades'), ('lni-leaf', 'Trabalhos com dados')], max_length=16, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
    ]
