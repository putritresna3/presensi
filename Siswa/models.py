from django.db import models

class Keterangan(models.Model):
    keterangan = models.CharField(max_length=20)

    def __str__(self):
        return self.keterangan

class Siswa(models.Model):
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)
    tgl = models.DateTimeField(auto_now_add=True)
    keterangan_id = models.ForeignKey(Keterangan, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.nama
