# import  pickle
#
# class Diary(object):
#
#     def __init__(self):
#         self.entries = []
#
#     @classmethod
#     def from_file(cls, file_path):
#
#         diary = cls()
#
#         with open(file_path) as file:
#             diary.entries = pickle.load(file)
#
#         return diary
#
# empty_diary = Diary()
# existing_diary = Diary.from_file("path/to/file.txt")



class Product():
    margin_factor = 0.2

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if (price < 0.0):
            raise ValueError("Price should be greater than 0!")
        self.__price = price

    @price.deleter
    def price(self):
        self.__price = None

    @property
    def margin(self):
        return self.margin_factor*self.__price



product = Product("HP printer", 1000)
product.price = 1200
print(product.price)
print(product.margin)
# del(product.price)
print(product.price)

# product.margin = 12323


class SalesOfProduct():
    def __init__(self, sales_qty, price):
        """

        :param sales_qty:
        :param price:
        """
        self.sales_qty = sales_qty
        self.price = price

    @property
    def revenue(self):
        return self.sales_qty * self.price

sales_of_pens = SalesOfProduct(20, 30)
print(sales_of_pens.revenue)