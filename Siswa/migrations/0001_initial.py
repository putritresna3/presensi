# Generated by Django 3.2.15 on 2023-01-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('kelas', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=50)),
                ('tgl', models.DateTimeField(auto_now_add=True)),
                ('keterangan', models.TextField(max_length=50)),
            ],
        ),
    ]
