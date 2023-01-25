from django.shortcuts import render, redirect
from Siswa.forms import FormSiswa
from Siswa.models import *
from django.contrib import messages

def hapus_siswa(request, id_siswa):
    siswa = Siswa.objects.filter(id=id_siswa)
    siswa.delete()

    messages.success(request, "Data berhasil dihapus!")
    return redirect('data')

def ubah_siswa(request, id_siswa):
    siswa = Siswa.objects.get(id=id_siswa)
    templates = 'ubah-siswa.html'
    if request.POST:
        form = FormSiswa(request.POST, instance=siswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui!")
            return redirect('ubah-siswa', id_siswa=id_siswa)
    else:
        form = FormSiswa(instance=siswa)
        konteks = {
            'form':form,
            'siswa':siswa,
        }
    return render(request, template, konteks)


def data(request):
    siswa = Siswa.objects.all()
    konteks = {
        'siswa' : siswa,
    }
    return render(request, 'siswa.html', konteks)

def tambah_siswa(request):
    if request.POST:
        form = FormSiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormSiswa()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-siswa.html', konteks) 
    else:
        form = FormSiswa()

        konteks = {
             'form' : form,
        }

    return render(request, 'tambah-siswa.html', konteks)
