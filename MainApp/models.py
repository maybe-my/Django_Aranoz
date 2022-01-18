from django.db import models
from django.db import models
# Create your models here.

# Tovars
from django.template.defaultfilters import slugify


class Tovar(models.Model):
    kod = models.IntegerField('KOD tovar*', max_length=11, blank=True, default='', db_index=True, unique=True)
    new = models.BooleanField(default=True, help_text='New?',
                              verbose_name='New?')
    top = models.BooleanField(default=False, help_text='Show main page', verbose_name='Top tovar')
    # category = models.ForeignKey(Category, verbose_name='Категория', related_name='Товар', default='Без категории',
    #                              on_delete=models.SET_DEFAULT)
    title = models.CharField('Title*', max_length=40, db_index=True)
    slug = models.SlugField('URL', max_length=200, db_index=True, unique=True)
    description = models.TextField('Description', blank=True)
    price = models.FloatField('Price*', max_length=10)
    # sale = models.IntegerField('Скидка в процентах', blank=True, default=0)
    available = models.BooleanField('Active', default=True)

    # Date
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Last edit', auto_now=True)

    # Image
    image_main = models.ImageField('Main photo*', upload_to='Products/%Y_%m_%d', blank=False)
    # image1 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)
    # image2 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)
    # image3 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)
    # image4 = models.ImageField('Дополнительное фото', upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Tovar'
        verbose_name_plural = f'Tovars'
        index_together = (('id', 'slug', 'top'),)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image_main.delete()
        notify = NotifyForAdmin.create(f"Deleted tovar: #{self.kod}", self.slug)
        notify.save()
        super(Tovar, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        notify = NotifyForAdmin.create(f"Created new Tovar: #{self.kod}", self.slug);
        notify.save()

        self.price = round(self.price, 2)
        self.slug = f"{self.slug}_{self.kod}"
        super(Tovar, self).save(*args, **kwargs)
    #
    # def get_sale(self):
    #     '''Расчитать стоимость со скидкой'''
    #     price = int(self.price * (100 - self.sale) / 100)
    #     return price


class NotifyForAdmin(models.Model):
    title = models.CharField('Title', max_length=40, db_index=True)
    slug = models.TextField('Slug', max_length=200)

    # Date
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Last edit', auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Notification'
        verbose_name_plural = f'Notifications'
        index_together = (('id', 'title'),)

    @classmethod
    def create(cls, title, slug):
        return cls(title=title, slug=slug)