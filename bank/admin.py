from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from bank.models import Dolznost, Otdel, Sotrudnic, SemeinoePolozenie, TipLiza, RodDeiatelnosti, Klient, KlientFizlizo, \
    KlientUrlizo, TipIzmeneniaIstorii, IstoriaIzmeneniaKlienta, TipDocumentov, LichnieDocumentKlienta, TipSheta, Shet, \
    TipDvizeniePoShetu, DvizeniePoShetu, TipPlateznoiSistemi, Kartochka, Kredit, GraficViplatiKredita


@admin.register(Dolznost)
class DolznostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'rukovodiachia_dolnost',
    ]
    search_fields = [
        'id',
        'nazvanie',
        'rukovodiachia_dolnost',
    ]
    list_filter = [
        'rukovodiachia_dolnost',
    ]

    save_as = True
    save_on_top = True


@admin.register(Otdel)
class OtdelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    save_as = True
    save_on_top = True


@admin.register(Sotrudnic)
class SotrudnicAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'fio',
    ]
    search_fields = [
        'id',
        'user__username',
        'fio',
    ]
    list_filter = [
        'dolznost__rukovodiachia_dolnost',
        'otdel',
    ]

    save_as = True
    save_on_top = True

@admin.register(SemeinoePolozenie)
class SemeinoePolozenieAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    save_as = True
    save_on_top = True


@admin.register(TipLiza)
class TipLizaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    save_as = True
    save_on_top = True

@admin.register(RodDeiatelnosti)
class RodDeiatelnostiAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    save_as = True
    save_on_top = True

@admin.register(Klient)
class KlientAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'phone',
        'phone_dopolnitelnie',
        'email',
        'rod_deiatelnosti',
        'lichni_menedger',
    ]
    search_fields = [
        'id',
        'phone',
        'email',
    ]
    list_filter = [
        'rod_deiatelnosti',
        'lichni_menedger',
    ]


@admin.register(KlientFizlizo)
class KlientFizlizoAdmin(admin.ModelAdmin):
    @display(description='Телефон')
    def get_phone(self, obj):
        return obj.klient.phone

    @display(description='Email')
    def get_email(self, obj):
        return obj.klient.email

    @display(description='Род деятельности')
    def get_rod_deiatelnosti(self, obj):
        return obj.klient.rod_deiatelnosti

    @display(description='Личный менеджер')
    def get_lichni_menedger(self, obj):
        return obj.klient.lichni_menedger

    list_display = [
        'id',
        'fio',
        'get_phone',
        'get_email',
        'get_rod_deiatelnosti',
        'get_lichni_menedger',
    ]
    search_fields = [
        'id',
        'klient__phone',
        'fio',
    ]
    list_filter = [
        'semeinoe_polozenie',
        'kolichestvo_detei',
        'klient__rod_deiatelnosti',
        'klient__lichni_menedger',
    ]

    save_as = True
    save_on_top = True


@admin.register(KlientUrlizo)
class KlientUrlizoAdmin(admin.ModelAdmin):
    @display(description='Телефон')
    def get_phone(self, obj):
        return obj.klient.phone

    @display(description='Email')
    def get_email(self, obj):
        return obj.klient.email

    @display(description='Род деятельности')
    def get_rod_deiatelnosti(self, obj):
        return obj.klient.rod_deiatelnosti

    @display(description='Личный менеджер')
    def get_lichni_menedger(self, obj):
        return obj.klient.lichni_menedger

    list_display = [
        'id',
        'tip_liza',
        'naimenovanie',
        'inn',
        'get_phone',
        'get_email',
        'get_rod_deiatelnosti',
        'get_lichni_menedger',

    ]
    search_fields = [
        'id',
        'klient__phone',
        'inn',
        'naimenovanie',
    ]
    list_filter = [
        'tip_liza',
        'klient__rod_deiatelnosti',
        'klient__lichni_menedger',
    ]

    save_as = True
    save_on_top = True


@admin.register(TipIzmeneniaIstorii)
class TipIzmeneniaIstoriiAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    save_as = True
    save_on_top = True


@admin.register(IstoriaIzmeneniaKlienta)
class IstoriaIzmeneniaKlientaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'klient',
        'tip_izmenenia_istorii',
        'danie_bili',
        'danie_stali',
        'sotrudnic',
        'data',
    ]
    search_fields = [
        'id',
        'danie_bili',
        'danie_stali',
    ]
    list_filter = [
        'sotrudnic',
        'data',
    ]

    save_as = True
    save_on_top = True


@admin.register(TipDocumentov)
class TipDocumentovAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    save_as = True
    save_on_top = True



@admin.register(LichnieDocumentKlienta)
class LichnieDocumentKlientaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'klient',
        'tip_documentov',
        'data_vidachi',
        'nomer_dokumenta',
        'organ_vidavshii',
    ]
    search_fields = [
        'id',
        'data_vidachi',
        'nomer_dokumenta',
    ]
    list_filter = [
        'tip_documentov',
        'data_vidachi',
    ]

    save_as = True
    save_on_top = True

@admin.register(TipSheta)
class TipShetaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    save_as = True
    save_on_top = True


@admin.register(Shet)
class ShetAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nomer_sheta',
        'tip_sheta',
        'klient',
        'data_otkritia',
        'data_zakritia',
        'balans_seishas',
    ]
    search_fields = [
        'id',
        'nomer_sheta',
    ]
    list_filter = [
        'tip_sheta',
        'data_otkritia',
        'data_zakritia',
    ]

    save_as = True
    save_on_top = True


@admin.register(TipDvizeniePoShetu)
class TipDvizeniePoShetuAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
        'spisanie_ili_popolnenenie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]
    list_filter = [
        'spisanie_ili_popolnenenie',
    ]

    save_as = True
    save_on_top = True


@admin.register(DvizeniePoShetu)
class DvizeniePoShetuAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'tip_dvizenie_po_shetu',
        'summa',
        'data',
        'fiz_adres_operazii',
        'naznachenie_plateza',
        'naimenovanie_prodovza',
        'rs_prodavza',
        'bik_prodavza',
    ]
    search_fields = [
        'id',
        'summa',
        'data',
        'fiz_adres_operazii',
        'naznachenie_plateza',
        'rs_prodavza',
        'bik_prodavza',
    ]
    list_filter = [
        'tip_dvizenie_po_shetu',
    ]

    save_as = True
    save_on_top = True


@admin.register(TipPlateznoiSistemi)
class TipPlateznoiSistemiAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nazvanie',
    ]
    search_fields = [
        'id',
        'nazvanie',
    ]

    save_as = True
    save_on_top = True



@admin.register(Kartochka)
class KartochkaAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nomer',
        'shet',
        'tip_plateznoi_sistemi',
    ]
    search_fields = [
        'id',
        'nomer',
    ]
    list_filter = [
        'tip_plateznoi_sistemi',
    ]

    save_as = True
    save_on_top = True



@admin.register(Kredit)
class KreditAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'klient',
        'sotrudnoc_vidavchi_kredit',
        'summa_kredita',
        'srok_v_mesiazah',
        'stavka',
        'data_vidachi_kredita',
        'rs_dlia_rasheta',
    ]
    search_fields = [
        'id',
        'summa_kredita',
    ]
    list_filter = [
        'sotrudnoc_vidavchi_kredit',
        'srok_v_mesiazah',
        'data_vidachi_kredita',
    ]

    save_as = True
    save_on_top = True

@admin.register(GraficViplatiKredita)
class GraficViplatiKreditatAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'kredit',
        'data_planovogo_plateza',
        'summa_k_viplate',
        'ostatok_k_viplate_nachalo',
    ]
    search_fields = [
        'id',
        'data_planovogo_plateza',
        'summa_k_viplate',
        'ostatok_k_viplate_nachalo',
    ]
    list_filter = [
        'data_planovogo_plateza',
    ]

    save_as = True
    save_on_top = True