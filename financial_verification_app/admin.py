from django.contrib import admin
from .models import Institution,Category,User,Role

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'tin','category','status')
    search_fields = ('name', 'tin','category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
# admin.site.register(User)
# admin.site.register(Role)

# Alternatively, you can use the simpler method without decorator
# admin.site.register(Institution, InstitutionAdmin)
