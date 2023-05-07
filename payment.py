class Payment:
    def __init__(self, transaction):
        """
        Membuat objek payment dengan inisiasi nilai untuk atribut 
        transaksi, discount, net price dan amount paid
        """
        self.transaction = transaction
        self.discount = 0
        self.net_price = 0
        self.amount_paid = 0

    def calculate_discount(self):
        """
        Menghitung nilai diskon dari transaksi
        """
        discount = self.transaction.get_discount()
        self.discount = discount

    def calculate_net_price(self):
        """
        Menghitung total harga akhir setelah dikurangi diskon
        """
        self.calculate_discount()
        total_price = self.transaction.total_price_after_discount()
        self.net_price = total_price

    def get_discount_amount(self):
        """
        Menghitung nilai diskon dalam rupiah
        """
        discount_amount = self.transaction.total_price() * self.discount
        return discount_amount

    def get_net_price(self):
        """
        Mendapatkan total harga akhir dari calculate_net_price
        """
        self.calculate_net_price()
        return self.net_price

    def calculate_change(self, amount=None):
        """
        Menghitung nilai kembalian dari pembayaran dengan uang tunai
        """
        if amount is None:
            amount = self.amount_paid
        total_price = self.transaction.total_price_after_discount()
        return amount - total_price

    def pay_with_cash(self, amount):
        """
        Menerima pembayaran dengan uang tunai, True jika berhasil, False jika gagal
        """
        total_price = self.transaction.total_price()
        if amount < total_price:
            return False
        self.amount_paid = amount
        return True
