from django.contrib import admin
from .models import category, subcategory, userPreference, userSubPreference
# Register your models here.


class userSubPreferenceAdmin(admin.ModelAdmin):

    list_display = ('userPreference_FK', 'subpreferenceCode', 'subpreferenceScore')


admin.site.register(userSubPreference)

admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(userPreference)

