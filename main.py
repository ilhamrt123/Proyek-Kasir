from transaction import Transaction
from payment import Payment

def main():
    """
    Digunakan untuk memilih menu sehingga customer dapat berpindah-pindah fitur
    sesuai dengan kebutuhan
    """
    transaction = Transaction()
    while True:
        print("=== Selamat Datang di Program Kasir IlhamMart ===")
        print("1. Tambah Item")
        print("2. Update Item")
        print("3. Hapus Item")
        print("4. Reset Transaksi")
        print("5. Check Order")
        print("6. Total Harga")
        print("7. Bayar dengan Cash")
        print("8. Keluar")

        choice = input("Masukkan pilihan anda: ")
        
        if choice == '1':
            try:
                name = input("Masukkan nama item: ")
                qty = int(input("Masukkan jumlah item: "))
                price = int(input("Masukkan harga per item: "))
                transaction.add_item(name, qty, price)
                print(f"{qty} {name} ditambahkan ke keranjang.")
            except ValueError:
                print("Input tidak valid. Masukkan angka pada jumlah item dan harga per item.")
        
        elif choice == '2':
            name = input("Masukkan nama item: ")
            qty = int(input("Masukkan jumlah item: "))
            price = int(input("Masukkan harga per item: "))
            if transaction.update_item(name, qty, price):
                print(f"{qty} {name} berhasil diupdate.")
            else:
                print(f"{name} tidak ditemukan.")
        
        elif choice == '3':
            name = input("Masukkan nama item: ")
            if transaction.remove_item(name):
                print(f"{name} berhasil dihapus.")
            else:
                print(f"{name} tidak berhasil dihapus.")
        
        elif choice == '4':
            transaction.reset_transaction()
            print("Transaksi berhasil direset.")

        elif choice == '5':
            transaction.print_order()

        elif choice == '6':
            total_before_discount = transaction.total_price()
            discount = transaction.get_discount()
            total_after_discount = transaction.total_price_after_discount()
            print(f"Total harga sebelum diskon: Rp {total_before_discount}")
            print(f"Diskon: Rp {discount}")
            print(f"Total harga setelah diskon: Rp {total_after_discount}")

        elif choice == '7':
            if transaction.total_items() == 0:
                print("Keranjang kosong. Tidak ada transaksi yang dapat dilakukan.")
            else:
                amount = int(input("Masukkan jumlah uang tunai: "))
                payment = Payment(transaction)  # mengirimkan objek transaction ke Payment
                if payment.pay_with_cash(amount):
                    print("Pembayaran dengan cash berhasil.")
                    change = payment.calculate_change()
                    print(f"Kembalian: Rp {change}")
                else:
                    print("Pembayaran dengan cash gagal.")

        elif choice == '8':
            print("Terima kasih telah menggunakan program kasir IlhamMart.")
            break

        else:
            print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")

main()