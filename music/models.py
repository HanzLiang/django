from django.db import models


# Create your models here.

class Book(models.Model):
    # 唯一 unique=True
    is_active=models.BooleanField(default=True)
    title = models.CharField("书名", max_length=50, default='',unique=True)
    pub = models.CharField("出版社", max_length=100,default='')
    # 7位总长 小数点后2位
    price = models.DecimalField('定价', max_digits=7, decimal_places=2,
                                default=0.0)
    market_price = models.DecimalField("零售价", max_digits=7,decimal_places=2,default=0.0)
    info = models.CharField("描述", max_length=100, default='')

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    
    def __str__(self):
        return '%s_%s_%s_%s'%(self.title,self.pub,self.price,self.market_price)




class Author(models.Model):
    name = models.CharField("名字", max_length=11)
    age = models.IntegerField("年龄", default=1)
    # Django创建表格是默认为非空，即默认null=False
    email = models.EmailField("邮箱", null=True)

    class Meta:
        db_table = 'author'


