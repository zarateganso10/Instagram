# Generated by Django 2.2.dev20181005132628 on 2018-11-19 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twistter', '0004_auto_20181119_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birthDate',
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=250),
        ),
    ]