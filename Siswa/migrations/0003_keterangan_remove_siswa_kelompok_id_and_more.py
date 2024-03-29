# Generated by Django 4.1.5 on 2023-01-24 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Siswa', '0002_auto_20230123_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keterangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='siswa',
            name='kelompok_id',
        ),
        migrations.RemoveField(
            model_name='siswa',
            name='keterangan',
        ),
        migrations.DeleteModel(
            name='kelompok',
        ),
        migrations.AddField(
            model_name='siswa',
            name='keterangan_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Siswa.keterangan'),
        ),
    ]
