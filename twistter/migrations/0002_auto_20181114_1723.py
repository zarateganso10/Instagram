# Generated by Django 2.2.dev20181005132628 on 2018-11-14 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twistter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('Conta', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('dataNascimento', models.DateField()),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]