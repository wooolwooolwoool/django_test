from django.db import models

# Create your models here.

category = (
    (0,"指定なし"),
    (1,"マンガ"),
    (2,"小説"),
    (3,"参考書"),
    (4,"実用書"),
    (5,"教科書"),
    (6,"雑誌"),
)

class Bookshelf(models.Model):
    title = models.CharField(verbose_name="本棚タイトル", 
                             max_length=20)
    cat = models.PositiveIntegerField(
        verbose_name="カテゴリ",
        choices=category, default=0)
    def __str__(self):
        return self.title

class Book(models.Model):
    target = models.ForeignKey(
        Bookshelf, verbose_name='紐づく本棚',
        blank=True, null=True,
        on_delete=models.SET_NULL)
    title = models.CharField(verbose_name="本タイトル", 
                             max_length=100)
    isbn = models.CharField(verbose_name="ISBNコード", 
                             max_length=13)
    comment = models.CharField(verbose_name="コメント", 
                               blank=True, null=True, max_length=100)
    def __str__(self):
        return self.title