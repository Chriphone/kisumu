# Generated by Django 3.0.5 on 2022-08-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_studentextra_academic_year_studentextra_id_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('desscription', models.CharField(max_length=120, verbose_name='desscription')),
            ],
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('ICT', 'ICT'), ('HD', 'HD'), ('TD', 'TD'), ('FB', 'FB')], default='one', max_length=10),
        ),
    ]
