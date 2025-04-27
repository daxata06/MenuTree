from django.contrib import admin

from .models import MenuName, Menu

def path_element(request):
    return list(filter(None, request.path.split('/')))

class MenuItemInline(admin.TabularInline):
    model = Menu
    extra = 0
    ordering = ('id',)

    def formfield_for_foreignkey(self, db_field, request, *args, **kwargs):
        if path_element(request)[-1] == 'change':
            kwargs['queryset'] = Menu.objects.filter(menu_id=path_element(request)[-2])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    inlines = [MenuItemInline]
