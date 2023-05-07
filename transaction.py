from payment import Payment

class Transaction:
    def __init__(self):
        self.items = {}
        self.payments = {}
        self.discount_rate = 0.0

    def add_item(self, name, qty, price):
        """
        Menambah item ke dalam keranjang belanja. Apabila item sudah ada, quantity
        akan ditambahkan, apabila belum ada maka item ditambahkan
        """
        if name in self.items:
            self.items[name]['qty'] += qty
        else:
            self.items[name] = {'qty': qty, 'price': price}

    def remove_item(self, name):
        """
        Menghapus item tertentu dari keranjang belanja
        """
        if name in self.items:
            del self.items[name]
            return True
        else:
            return False

    def update_item(self, name, qty, price):
        """
        Mengubah detail dari item yang sudah ada di keranjang, baik dari segi jumlah
        maupun harga
        """
        if name in self.items:
            self.items[name]['qty'] = qty
            self.items[name]['price'] = price
            return True
        else:
            return False

    def reset_transaction(self):
        """
        Reset seluruh item di dalam keranjang
        """
        self.items = {}
        self.payments = {}

    def print_order(self):
        """
        Mencetak semua detail item di dalam keranjang belanja
        """
        if self.items:
            print("Keranjang belanja Anda:")
            for name, item in self.items.items():
                qty = item['qty']
                price = item['price']
                total_price = qty * price
                print(f"{name}:({qty}) * {price} = Rp {total_price}")
        else:
            print("Keranjang belanja Anda kosong.")

    def total_price(self):
        """
        Menghitung total harga dari semua item dalam keranjang belanja
        """
        total = 0
        for item in self.items.values():
            qty = item['qty']
            price = item['price']
            total += qty * price
        return total
    
    def calculate_discount_rate(self, total_price):
        """
        Menghitung persentase diskon berdasarkan total harga
        """
        if total_price > 500000:
            return 0.1
        elif total_price > 300000:
            return 0.08
        elif total_price > 200000:
            return 0.05
        else:
            return 0.0
    
    def get_discount(self):
        """
        Mengambil data diskon dari pencari fungsi calculate_discount_rate
        """
        total_price = self.total_price()
        self.discount_rate = self.calculate_discount_rate(total_price)
        return total_price * self.discount_rate
    
    def total_price_after_discount(self):
        """
        Menghitung total harga setelah diskon diterapkan
        """
        return self.total_price() - self.get_discount()

    def total_items(self):
        """
        Menghitung total item di dalam keranjang belanja
        """
        return sum(item['qty'] for item in self.items.values())
