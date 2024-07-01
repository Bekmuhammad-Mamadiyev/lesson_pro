from django.contrib import admin
from kompaniya.models import BlogSetting,Maqola,Resume


# Register your models here.
@admin.register(BlogSetting)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("brand_name", "author_name",'bio','github')

@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('title','description','body')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('body','is_active')