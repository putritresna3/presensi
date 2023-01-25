from django.contrib import admin
from Siswa.models import *


class AdminSiswa(admin.ModelAdmin):
    list_display = ['nama', 'kelas','tgl', 'jabatan', 'keterangan_id']
    search_fields = ['nama']
    list_filter = ['keterangan_id']
    list_per_page = 5

admin.site.register(Siswa,AdminSiswa)
admin.site.register(Keterangan)