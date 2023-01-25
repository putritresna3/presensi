from django.contrib import admin
from django.urls import path
from Siswa.views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data, name='data'),
    path('tambah-siswa/', tambah_siswa, name='tambah_siswa'),
    path('data/ubah/<int:id_siswa>', ubah_siswa, name='ubah_siswa'),
    path('data/hapus/<int:id_siswa>', hapus_siswa, name='hapus_siswa'),
    path('masuk/', LoginView.as_view(), name='masuk'),
]
