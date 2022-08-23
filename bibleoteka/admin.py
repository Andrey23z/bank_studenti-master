from django.contrib import admin

from bibleoteka.models import Author, AuthorBook, Book, City, Customer, Delivery, Employees, Genre, \
    Order, OrderBook, OrderDetails, Purchase, Stock, Suppliers, Treaty



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
    list_filter = [
        'name',
    ]

    save_as = True
    save_on_top = True


@admin.register(AuthorBook)
class Author_bookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'book',
    ]
    search_fields = [
        'id',
        'author',
        'book',
    ]
    list_filter = [
        'author',
        'book',
    ]

    save_as = True
    save_on_top = True


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'genre',
    ]
    search_fields = [
        'id',
        'name',
        'genre',
    ]
    list_filter = [
        'name',
        'genre',
    ]

    save_as = True
    save_on_top = True


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
    list_filter = [
        'name',
    ]

    save_as = True
    save_on_top = True


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'address',
        'phone',
    ]
    search_fields = [
        'id',
        'name',
        'address',
        'phone',
    ]
    list_filter = [
        'name',
    ]

    save_as = True
    save_on_top = True


@admin.register(Delivery)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'suppliers',
        'city',
        'date',
    ]
    search_fields = [
        'id',
        'suppliers',
        'city',
        'date',
    ]
    list_filter = [
        'date',
    ]

    save_as = True
    save_on_top = True


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'address',
        'phone',
        'birthday',
    ]
    search_fields = [
        'id',
        'name',
        'address',
        'phone',
        'birthday',
    ]
    list_filter = [
        'name',
    ]

    save_as = True
    save_on_top = True


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
    search_fields = [
        'id',
        'name',
    ]
    list_filter = [
        'name',
    ]

    save_as = True
    save_on_top = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'date',
        'treaty',
        'employees',
    ]
    search_fields = [
        'id',
        'customer',
        'date',
        'treaty',
        'employees',
    ]
    list_filter = [
        'customer',
    ]

    save_as = True
    save_on_top = True


@admin.register(OrderBook)
class Order_bookAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'book',
        'date_vozvrata',
    ]
    search_fields = [
        'id',
        'customer',
        'book',
        'date_vozvrata',
    ]
    list_filter = [
        'date_vozvrata',
    ]

    save_as = True
    save_on_top = True


@admin.register(OrderDetails)
class Order_detailsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'book',
        'order',
        'count',
        'purchase',
    ]
    search_fields = [
        'id',
        'book',
        'order',
        'count',
        'purchase',
    ]
    list_filter = [
        'count',
    ]

    save_as = True
    save_on_top = True


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'book',
        'customer',
        'price',
        'date',
    ]
    search_fields = [
        'id',
        'book',
        'customer',
        'price',
        'date',
    ]
    list_filter = [
        'price',
        'date',
    ]

    save_as = True
    save_on_top = True


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'book',
        'delivery',
    ]
    search_fields = [
        'id',
        'book',
        'delivery',
    ]
    list_filter = [
        'book',
        'delivery',
    ]

    save_as = True
    save_on_top = True


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'address',
        'inn',
        'fax',
    ]
    search_fields = [
        'id',
        'name',
        'address',
        'inn',
        'fax',
    ]
    list_filter = [
        'name',
    ]

    save_as = True
    save_on_top = True


@admin.register(Treaty)
class TreatyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'date',
    ]
    search_fields = [
        'id',
        'customer',
        'date',
    ]
    list_filter = [
        'date',
    ]

    save_as = True
    save_on_top = True
