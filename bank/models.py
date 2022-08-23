from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class Dolznost(models.Model):
    class Meta:
        verbose_name = 'Должности'
        verbose_name_plural = '01 Должности'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)
    rukovodiachia_dolnost = models.BooleanField('Руководящая должность', default=False)

    def __str__(self):
        return self.nazvanie


class Otdel(models.Model):
    class Meta:
        verbose_name = 'Отделы'
        verbose_name_plural = '02 Отделы'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class Sotrudnic(models.Model):
    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = '03 Сотрудники'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Логин')
    fio = models.CharField('ФИО', db_index=True, max_length=255)
    dolznost = models.ForeignKey(Dolznost, verbose_name='Должность', on_delete=models.PROTECT)
    otdel = models.ForeignKey(Otdel, verbose_name='Отдел', on_delete=models.PROTECT)

    def __str__(self):
        return self.fio


class SemeinoePolozenie(models.Model):
    class Meta:
        verbose_name = 'Семейные положения'
        verbose_name_plural = '04 Семейные положения'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class TipLiza(models.Model):
    class Meta:
        verbose_name = 'Типы юр лица'
        verbose_name_plural = '05 Типы юр лица'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class RodDeiatelnosti(models.Model):
    class Meta:
        verbose_name = 'Род деятельности'
        verbose_name_plural = '06 Род деятельности'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class Klient(models.Model):
    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиент'


    phone = models.CharField('Контактный телефон', db_index=True, null=True, blank=True, max_length=255)
    phone_dopolnitelnie = models.CharField('Дополнительные телефоны', null=True, blank=True, max_length=255)
    email = models.CharField('Email', null=True, blank=True, max_length=255)

    rod_deiatelnosti = models.ForeignKey(RodDeiatelnosti, verbose_name='Род деятельности', on_delete=models.PROTECT, null=True, blank=True)

    lichni_menedger = models.ForeignKey(Sotrudnic, on_delete=models.SET_NULL, verbose_name='Личный менеджер банка',
                                        null=True, blank=True)

    def __str__(self):
        return self.get_fio_or_nazvanie()

    def get_fio_or_nazvanie(self):
        try:
            return self.klientfizlizo.fio
        except Exception:
            pass

        try:
            return self.klienturlizo.naimenovanie
        except Exception:
            pass

        return '-'


class KlientFizlizo(models.Model):
    class Meta:
        verbose_name = 'Клиенты физ лица'
        verbose_name_plural = '07 Клиенты физ лица'

    klient = models.OneToOneField(Klient, on_delete=models.CASCADE, verbose_name='Клиент')
    fio = models.CharField('ФИО', db_index=True, max_length=255)
    photo = models.ImageField('Фото', null=True, blank=True)
    data_rozdenia = models.DateField('Дата рождения', blank=True, null=True)
    semeinoe_polozenie = models.ForeignKey(SemeinoePolozenie, verbose_name='Семейное положение', blank=True, null=True,
                                           on_delete=models.SET_NULL)
    kolichestvo_detei = models.IntegerField('Количество детей', blank=True, null=True)

    def __str__(self):
        return self.klient.get_fio_or_nazvanie()

class KlientUrlizo(models.Model):
    class Meta:
        verbose_name = 'Клиенты юр лица'
        verbose_name_plural = '08 Клиенты юр лица'

    klient = models.OneToOneField(Klient, on_delete=models.CASCADE, verbose_name='Клиент')
    naimenovanie = models.CharField('Наименование', db_index=True, max_length=255)
    inn = models.CharField('ИНН', db_index=True, max_length=255)
    tip_liza = models.ForeignKey(TipLiza, verbose_name='Тип юр лица', on_delete=models.PROTECT)

    def __str__(self):
        return self.klient.get_fio_or_nazvanie()

class TipIzmeneniaIstorii(models.Model):
    class Meta:
        verbose_name = 'Типы изменения историй клиентов'
        verbose_name_plural = '09 Типы изменения историй клиентов'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class IstoriaIzmeneniaKlienta(models.Model):
    class Meta:
        verbose_name = 'Истории изменений'
        verbose_name_plural = '10 Истории изменений'

    klient = models.ForeignKey(Klient, verbose_name='Клиент у которого поменяли данные', on_delete=models.PROTECT)
    tip_izmenenia_istorii = models.ForeignKey(TipIzmeneniaIstorii, verbose_name='Тип изменения',
                                              on_delete=models.PROTECT)
    danie_bili = models.JSONField('Данные были', null=True, blank=True)
    danie_stali = models.JSONField('Данные стали', null=True, blank=True)
    sotrudnic = models.ForeignKey(Sotrudnic, verbose_name='Сотрудник который внёс изменение', on_delete=models.PROTECT,
                                  null=True, blank=True)
    data = models.DateTimeField('Дата изменения', null=True, blank=True)

    def __str__(self):
        return f'История изменения {self.klient}'


class TipDocumentov(models.Model):
    class Meta:
        verbose_name = 'Типы документов'
        verbose_name_plural = '11 Типы документов'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class LichnieDocumentKlienta(models.Model):
    class Meta:
        verbose_name = 'Личные документы клиентов'
        verbose_name_plural = '12 Личные документы клиентов'

    klient = models.ForeignKey(Klient, verbose_name='Клиент', on_delete=models.PROTECT)
    tip_documentov = models.ForeignKey(TipDocumentov, verbose_name='Тип документов', on_delete=models.PROTECT)
    data_vidachi = models.DateField('Дата выдачи', null=True, blank=True)
    nomer_dokumenta = models.CharField('Номер документа', null=True, blank=True, max_length=255, db_index=True)
    organ_vidavshii = models.CharField('Орган выдавший', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.nomer_dokumenta


class TipSheta(models.Model):
    class Meta:
        verbose_name = 'Типы счетов'
        verbose_name_plural = '13 Типы счетов'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class Shet(models.Model):
    class Meta:
        verbose_name = 'Счета'
        verbose_name_plural = '14 Счета'

    nomer_sheta = models.CharField('Номер счёта',max_length=255, db_index=True, unique=True)
    tip_sheta = models.ForeignKey(TipSheta, verbose_name='Тип счёта', on_delete=models.PROTECT)
    klient = models.ForeignKey(Klient, verbose_name='Клиент владелец счёта', on_delete=models.PROTECT)
    data_otkritia = models.DateField('Дата открытия')
    data_zakritia = models.DateField('Дата закрытия', null=True, blank=True)
    balans_seishas = models.FloatField('Баланс сейчас', default=0)
    skan_dogovora = models.FileField('Скан договора об открытие счета', null=True, blank=True)

    def __str__(self):
        return self.nomer_sheta


class TipDvizeniePoShetu(models.Model):
    class Meta:
        verbose_name = 'Типы движения по счетам'
        verbose_name_plural = '15 Типы движения по счетам'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)
    spisanie_ili_popolnenenie = models.CharField('Списание или пополнение', max_length=1, choices=(
        ('-', 'Списание'),
        ('+', 'Пополнение'),
    ))

    def __str__(self):
        return self.nazvanie


class DvizeniePoShetu(models.Model):
    class Meta:
        verbose_name = 'Движения по счётам'
        verbose_name_plural = '16 Движения по счётам'

    shet = models.ForeignKey(Shet, verbose_name='Счёт', on_delete=models.PROTECT)
    tip_dvizenie_po_shetu = models.ForeignKey(TipDvizeniePoShetu, verbose_name='Тип операции', on_delete=models.PROTECT)
    summa = models.FloatField('Сумма', default=0, db_index=True)
    data = models.DateTimeField('Дата и время операция')

    fiz_adres_operazii = models.JSONField('Координаты где была совершенна операция', null=True, blank=True)

    naznachenie_plateza = models.TextField('Назначение платежа', null=True, blank=True)
    naimenovanie_prodovza = models.CharField('Наименование продовца', null=True, blank=True, max_length=255)
    inn_podavza = models.CharField('ИНН продавца', null=True, blank=True, max_length=255)
    rs_prodavza = models.CharField('РС продавца', null=True, blank=True, max_length=255)
    bik_prodavza = models.CharField('БИК продавца', null=True, blank=True, max_length=255)

    def __str__(self):
        return f'Движение по счёту {self.shet.nomer_sheta}'


class TipPlateznoiSistemi(models.Model):
    class Meta:
        verbose_name = 'Типы платёжной системы'
        verbose_name_plural = '17 Типы платёжной системы'

    nazvanie = models.CharField('Название', db_index=True, max_length=255, unique=True)

    def __str__(self):
        return self.nazvanie


class Kartochka(models.Model):
    class Meta:
        verbose_name = 'Карточки'
        verbose_name_plural = '18 Карточки'

    nomer = models.CharField('Номер карты', unique=True, max_length=255)
    shet = models.ForeignKey(Shet, verbose_name='Счёт', on_delete=models.PROTECT)
    tip_plateznoi_sistemi = models.ForeignKey(TipPlateznoiSistemi, verbose_name='Тип платежной системы', on_delete=models.PROTECT)

    def __str__(self):
        return self.nomer


class Kredit(models.Model):
    class Meta:
        verbose_name = 'Кредитования'
        verbose_name_plural = '19 Кредитования'

    klient = models.ForeignKey(Klient, verbose_name='Клиент', on_delete=models.PROTECT)
    sotrudnoc_vidavchi_kredit = models.ForeignKey(Sotrudnic, verbose_name='Сотрудник который выдал кредит',
                                                  on_delete=models.SET_NULL, null=True, blank=True)
    summa_kredita = models.FloatField('Сумма кредита', db_index=True)
    srok_v_mesiazah = models.IntegerField('Срок кредита в месяцах', db_index=True)
    stavka = models.FloatField('Процентная ставка', db_index=True)
    data_vidachi_kredita = models.DateField('Дата выдачи кредита', db_index=True)
    rs_dlia_rasheta = models.ForeignKey(Shet, verbose_name='Расчетный счет', on_delete=models.PROTECT)

    def __str__(self):
        return f'Кредит # {self.id} от {self.data_vidachi_kredita}'


class GraficViplatiKredita(models.Model):
    class Meta:
        verbose_name = 'Графики выплат кредитов'
        verbose_name_plural = '20 Графики выплат кредитов'

    kredit = models.ForeignKey(Kredit, verbose_name='Кредит', on_delete=models.PROTECT)
    data_planovogo_plateza = models.DateField('Дата планового платежа')
    summa_k_viplate = models.FloatField('Сумма к выплате за период')
    ostatok_k_viplate_nachalo = models.FloatField('Остаток по кредиту на начало периода')

    def __str__(self):
        return f'График {self.id}'