from django.contrib import admin
from .models import Author



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id','joined_date','image')


admin.site.register(Author,AuthorAdmin)
# admin.site.register(Post,PostAdmin)