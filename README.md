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
   Customer ingin menginput barang: <br />
   Pilih menu dan Input item 1: <br />
   ![Screenshot_1](https://user-images.githubusercontent.com/132833682/236685643-2d8d95ce-0a6f-4135-9ddf-74460e0cc35d.jpg) <br />
    Pilih menu dan Input item 2: <br />
    ![Screenshot_2](https://user-images.githubusercontent.com/132833682/236685656-ef215ac0-4b2f-456a-8dc8-0088d2790f8c.jpg) <br />
    Menampilkan item yang telah diinput: <br />
    ![Screenshot_3](https://user-images.githubusercontent.com/132833682/236686047-f1bf2e19-f7fb-4712-894a-33fb6fae0b17.jpg) <br />

2. Test 2:
   Customer ingin delete barang: <br />
   Pilih menu 3 dan input item yang akan dihapus <br />
   ![Screenshot_4](https://user-images.githubusercontent.com/132833682/236686082-273dd0db-4d84-4300-939b-46561f389aab.jpg) <br />

3. Test 3:
   Customer ingin mereset transaksi <br />
   Pilih menu 4 dan transaksi akan hilang semua <br />
   ![Screenshot_5](https://user-images.githubusercontent.com/132833682/236686140-a06f96cc-51b2-44b7-9cab-91ad4359a944.jpg) <br />

4. Test 4:
    Customer ingin menjumlah semua item dan menghitung harga akhir setelah diskon: <br />
    ![Screenshot_6](https://user-images.githubusercontent.com/132833682/236686158-3ca68d40-4b80-4f0c-bfa3-3557b61e1486.jpg) <br />
    
## Kesimpulan
Proyek ini sudah memenuhi fungsi-fungsi dasar untuk program kasir seperti menambah item, update item, dan hapus item. Program ini dapat melakukan perhitungan untuk harga sebelum dan sesudah diskon serta dapat menghitung kembalian pembayaran cash. <br />
Program ini berdasarkan OOP untuk mempermudah pengembangan dan perawatan. Terdapat dua kelas yakni Transaction dan Payment. Transaction digunakan berkaitan dengan mengatur detail dari transaksi sedangkan payment untuk pembayaran dan menghitung kembalian <br />
Karena fungsionalitasnya dan sederhana, program ini cocok untuk industri UMKM.
