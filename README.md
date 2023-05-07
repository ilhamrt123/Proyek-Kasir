# PROYEK KASIR ILHAMMART

## Latar Belakang

Aplikasi kasir merupakan sebuah sistem dasar yang dibutuhkan untuk membantu manusia dalam menjalankan bisnis. Dengan adanya sistem kasir dapat membantu pencatatan lebih akurat dan rapi sehingga dengan aplikasi ini kami berharap dapat membantu bisnis dalam skala kecil maupun menengah.

## Objective

Beberapa tujuan yang ingin dicapai dalam program kasir IlhamMart:
a. Memungkinkan pengguna untuk menambahkan, memperbarui, dan menghapus item
b. Menghitung total harga transaksi sebelum dan sesudah diskon tertentu diberikan
c. Menghitung kembalian pembayaran (asumsi pembeli membayar dengan cash)

## Alur code/flowchart

1. Program dimulai dengan menampilkan 8 opsi menu
2. Pengguna dapat memilih menu sesuai yang diinginkan
3. Program akan melakukan aksi berdasarkan menu yang dipilih
4. Apabila sudah yakin dengan item dan akan melakukan pembayaran, dapat memilih nomor 7 dan sistem akan meminta kita memasukkan nominal
5. Jika pembayaran berhasil, program akan mencetakn tanda terima yang berisi detail transaksi dan kembalian

## Penjelasan fungsi/attribut

Beberapa contoh fungsi:
1. Transaction() : membuat object transaction untuk menyimpan item-item
2. add_item(name, qty, price) : Menambahkan item dengan parameter name, qty, dan price
3. update_item(name, qty, price) : Melakukan update terhadap item dengan mengisi name, qty dan price yang baru
4. remove_item(name) : Menghapus item berdasarkan nama item
5. reset_transaction() : Melakukan reset terhadap transaksi
6. print_order() : Mencetak item-item yang telah diinput
7. total_price() : Menghitung harga awal sebelum diskon
8. get_discount() : Menghitung jumlah diskon
9. total_price_after_discount() : Menghitung harga setelah diskon

Beberapa contoh atribut:
1. Items: Untuk menyimpan item-item
2. discount_thresholds : Menyimpanan besaran diskon bergantung dengan total harga


## Demonstrasi code

1. Test 1:
   Customer ingin menginput barang:
   Pilih menu dan Input item 1:
   ![Contoh Gambar 1 Test 1](C:\Users\ilham\Downloads\Screenshot_1.jpg "Ini adalah contoh gambar pertama untuk tes 1")
    Pilih menu dan Input item 2:
    ![Contoh Gambar 2 Test 1](C:\Users\ilham\Downloads\Screenshot_2.jpg "Ini adalah contoh gambar kedua untuk tes 1")
    Menampilkan item yang telah diinput:
    ![Contoh Gambar 3 Test 1](C:\Users\ilham\Downloads\Screenshot_3.jpg "Ini adalah contoh gambar ketiga untuk tes 1")

2. Test 2:
   Customer ingin mendelete barang:
   Pilih menu 3 dan input item yang akan dihapus
   ![Contoh Gambar 1 Test 2](C:\Users\ilham\Downloads\Screenshot_4.jpg "Ini adalah contoh gambar pertama untuk tes 1")

3. Test 3:
   Customer ingin mereset transaksi
   Pilih menu 4 dan transaksi akan hilang semua
    ![Contoh Gambar 1 Test 3](C:\Users\ilham\Downloads\Screenshot_5.jpg "Ini adalah contoh gambar pertama untuk tes 3")

4. Test 4:
    Customer ingin menjumlah semua item dan menghitung harga akhir setelah diskon:
    ![Contoh Gambar 1 Test 4](C:\Users\ilham\Downloads\Screenshot_6.jpg"Ini adalah contoh gambar pertama untuk tes 4")