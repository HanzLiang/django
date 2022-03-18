from django.contrib import admin
from .models import Book

# Register your models here.


class BookManager(admin.ModelAdmin):

    # 列表页显示那些字段的列
    list_display = ['id','title','pub','price']
    # 控制list_display中的字段 那些可以连接到修改页
    list_display_links = ['title']
    # 添加过滤器
    list_filter = ['pub']
    # 添加搜索框 [进行模糊查询，可以继续添加参数]
    search_fields = ['title']
    # 添加可在列表页编辑的字段 与 list_display_links 互斥
    list_editable = ['price']




admin.site.register(Book,BookManager)
