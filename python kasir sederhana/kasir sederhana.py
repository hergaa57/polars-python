pilihan="y"
while pilihan=="y":
    print("""
    ==============================
                Menu
    ==============================
    1. Kopi Besar
    2. Kopi Sedang
    3. Kopi Kecil
    4. Susu
    5. Muffin
    6. Roti Croissant
    7. Donat
    ==============================
    """)
    pesan=str(input("masukkan list nomor menu ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "1":
        listnama= "Kopi Besar"
        harga=(48000*jumlahpesan)
        ppn= int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "2":
        listnama= "Kopi Sedang"
        harga = (32000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "3":
        listnama= "Kopi Kecil"
        harga=int(16000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "4":
        listnama= "Susu"
        harga=int(8000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "5":
        listnama= "Muffin"
        harga=int(15000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "6":
        listnama= "Roti Croissant"
        harga=int(15000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "7":
        listnama= "Donat"
        harga=int(8000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
    print("--------------------------")
    print("Menu")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")