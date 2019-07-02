from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    #列表展示记录的属性的顺序
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    #过滤器列表
    list_filter = ('sex', 'status', 'created_time')
    #加一个搜索框，关键词只能是name，profession
    search_fields = ('name', 'profession')
    #添加记录时填空的排列
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status',
            )
        }),
    )

admin.site.register(Student, StudentAdmin)