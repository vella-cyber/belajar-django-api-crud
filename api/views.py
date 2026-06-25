from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Data dummy di memori
mahasiswa = [
    {
        "id": 1,
        "nama": "Vellaro",
        "jurusan": "Sistem Komputer"
    }
]

@csrf_exempt  # Dipasang agar Django mengizinkan request POST tanpa token keamanan CSRF untuk sementara
def mahasiswa_api(request):
    
    # 1. Menampilkan Data (GET)
    if request.method == "GET":
        return JsonResponse({
            "method": "GET",
            "data": mahasiswa
        })
        
    # 2. Menambah Data Baru (POST)
    elif request.method == "POST":
        # Membaca data JSON yang dikirim oleh Postman
        data_baru = json.loads(request.body)
        
        # Memasukkan data baru ke dalam list mahasiswa
        mahasiswa.append(data_baru)
        
        return JsonResponse({
            "method": "POST",
            "message": "Data berhasil ditambahkan!",
            "data": data_baru
        }, status=201)
    # 3. Memperbarui Data (PUT)
    elif request.method == "PUT":
        data_update = json.loads(request.body)
        id_target = data_update.get("id") # Mengambil ID mahasiswa yang mau diedit
        
        # Cari datanya di dalam list berdasarkan id
        for mhs in mahasiswa:
            if mhs["id"] == id_target:
                mhs["nama"] = data_update.get("nama", mhs["nama"])
                mhs["jurusan"] = data_update.get("jurusan", mhs["jurusan"])
                
                return JsonResponse({
                    "method": "PUT",
                    "message": f"Data dengan ID {id_target} berhasil diperbarui!",
                    "data": mhs
                }, status=200)
            # Jika ID tidak ditemukan di dalam list
        return JsonResponse({
            "message": f"Data dengan ID {id_target} tidak ditemukan!"
        }, status=404)
    # 4. Memperbarui Data Sebagian (PATCH)
    elif request.method == "PATCH":
        data_patch = json.loads(request.body)
        id_target = data_patch.get("id")
        
        for mhs in mahasiswa:
            if mhs["id"] == id_target:
                # Menggunakan if terpisah agar hanya mengupdate field yang dikirim saja
                if "nama" in data_patch:
                    mhs["nama"] = data_patch["nama"]
                if "jurusan" in data_patch:
                    mhs["jurusan"] = data_patch["jurusan"]
                    
                return JsonResponse({
                    "method": "PATCH",
                    "message": f"Bagian data dengan ID {id_target} berhasil diubah!",
                    "data": mhs
                }, status=200)
                
        return JsonResponse({"message": f"Data ID {id_target} tidak ditemukan!"}, status=404)
    # 5. Menghapus Data (DELETE)
    elif request.method == "DELETE":
        data_delete = json.loads(request.body)
        id_target = data_delete.get("id") # Mengambil ID yang mau dihapus
        
        for mhs in mahasiswa:
            if mhs["id"] == id_target:
                mahasiswa.remove(mhs) # Menghapus data dari list mahasiswa
                
                return JsonResponse({
                    "method": "DELETE",
                    "message": f"Data dengan ID {id_target} berhasil dihapus!"
                }, status=200)
                
        return JsonResponse({"message": f"Data ID {id_target} tidak ditemukan!"}, status=404)
            