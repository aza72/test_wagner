from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe
from test_site.models import Slider

@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['order','name', 'image', 'post_photo']

    @admin.display(description="Миниатюра")
    def post_photo(self, slider: Slider):
        return mark_safe(f"<img src='{slider.image.url}' width=100>")

    class Meta:
        ordering = ['order']