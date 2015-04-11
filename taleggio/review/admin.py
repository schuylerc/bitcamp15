from django.contrib import admin
from .models import DwellingReview, TenantReview, LandlordReview

# Register your models here.
admin.site.register(DwellingReview)
admin.site.register(TenantReview)
admin.site.register(LandlordReview)
