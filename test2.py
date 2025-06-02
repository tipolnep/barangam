while True:
    print(">>>>>>>>>>>>>>>>>>>>>>>> PROGRAM SORTING NAMA <<<<<<<<<<<<<<<<<<<<<<<<<<<\n")

    # Input jumlah elemen list
    try:
        jumlah = int(input("Input jumlah element list (Angka): "))
    except ValueError:
        print("Input harus berupa angka. Coba lagi!\n")
        continue

    # Input elemen nama
    nama_list = []
    for i in range(jumlah):
        nama = input(f"Masukkan Nama ke-{i+1} (enter untuk lanjut): ")
        nama_list.append(nama)

    print(f"\nDaftar List : {nama_list}\n")

    # Pilih metode sorting
    print("Silahkan Pilih Sorting (1/2) ?")
    print("1. Ascending")
    print("2. Descending")
    pilihan = input("Pilihan Anda: ")

    if pilihan == '1':
        nama_list.sort()
        print("\nBerikut Hasil List yang sudah di Sorting (Ascending)")
    elif pilihan == '2':
        nama_list.sort(reverse=True)
        print("\nBerikut Hasil List yang sudah di Sorting (Descending)")
    else:
        print("\nPilihan tidak valid. List tidak disortir.")

    print(nama_list)

    # Tanya user apakah ingin mengulang
    ulang = input("\nApakah Anda ingin mengulang program? (y/n): ")
    if ulang.lower() != 'y':
        print("Terima kasih telah menggunakan program ini. Sampai jumpa bapak ulun yang ganteng rupawan dan selalu jadi incaran ciwi-ciwi!\n")
        break
