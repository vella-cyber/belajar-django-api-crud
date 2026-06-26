from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Data dummy di memori menggunakan format asisten
asisten = [
    {
        "id": 1,
        "nama asisten": "Muhammad Idham Faiq",
        "asisten praktikum": "Mikrokontroler"
    },
    {
        "id": 2,
        "nama asisten": "Fadias Virgiansyah",
        "asisten praktikum": "Jaringan Komputer"
    }
]

@csrf_exempt
def asisten_api(request):
    
    # 1. Menampilkan Data (GET)
    if request.method == "GET":
        return JsonResponse({
            "method": "GET",
            "data": asisten
        })
        
    # 2. Menambah Data Baru (POST)
    elif request.method == "POST":
        data_baru = json.loads(request.body)
        
        # Validasi pastikan key bahasa Indonesia ada
        if "id" not in data_baru or "nama asisten" not in data_baru or "asisten praktikum" not in data_baru:
            return JsonResponse({
                "message": "ID, nama asisten, dan asisten praktikum harus dikirim lengkap!"
            }, status=400)
            
        asisten.append(data_baru)
        return JsonResponse({
            "method": "POST",
            "message": "Data berhasil ditambahkan!",
            "data": data_baru
        }, status=201)

    # 3. Memperbarui Data (PUT)
    elif request.method == "PUT":
        data_update = json.loads(request.body)
        id_target = data_update.get("id")
        
        if not id_target or "nama asisten" not in data_update or "asisten praktikum" not in data_update:
            return JsonResponse({
                "message": "ID, nama asisten, dan asisten praktikum harus dikirim lengkap!"
            }, status=400)
        
        for ast in asisten:
            if ast["id"] == id_target:
                ast["nama asisten"] = data_update.get("nama asisten")
                ast["asisten praktikum"] = data_update.get("asisten praktikum")
                
                return JsonResponse({
                    "method": "PUT",
                    "message": f"Data dengan ID {id_target} berhasil diperbarui!",
                    "data": ast
                }, status=200)
                
        return JsonResponse({"message": f"Data dengan ID {id_target} tidak ditemukan!"}, status=404)

    # 4. Memperbarui Data Sebagian (PATCH)
    elif request.method == "PATCH":
        data_patch = json.loads(request.body)
        id_target = data_patch.get("id")
        
        for ast in asisten:
            if ast["id"] == id_target:
                if "nama asisten" in data_patch:
                    ast["nama asisten"] = data_patch["nama asisten"]
                if "asisten praktikum" in data_patch:
                    ast["asisten praktikum"] = data_patch["asisten praktikum"]
                    
                return JsonResponse({
                    "method": "PATCH",
                    "message": f"Bagian data dengan ID {id_target} berhasil diubah!",
                    "data": ast
                }, status=200)
                
        return JsonResponse({"message": f"Data ID {id_target} tidak ditemukan!"}, status=404)

    # 5. Menghapus Data (DELETE)
    elif request.method == "DELETE":
        data_delete = json.loads(request.body)
        id_target = data_delete.get("id")
        
        for ast in asisten:
            if ast["id"] == id_target:
                asisten.remove(ast)
                return JsonResponse({
                    "method": "DELETE",
                    "message": f"Data dengan ID {id_target} berhasil dihapus!"
                }, status=200)
                
        return JsonResponse({"message": f"Data ID {id_target} tidak ditemukan!"}, status=404)