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
