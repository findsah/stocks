from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Stocks


class StockAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Stocks, StockAdmin)
