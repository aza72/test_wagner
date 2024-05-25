from django import template
from test_site.models import Slider

register = template.Library()

@register.inclusion_tag('test_site/slider_tag.html')
def show_slider():
    img = Slider.objects.all()
    return {'img': img}
