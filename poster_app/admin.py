from django.contrib.admin import register, ModelAdmin
from poster_app.models import *


@register(Poster)
class PosterAdmin(ModelAdmin):
    pass
