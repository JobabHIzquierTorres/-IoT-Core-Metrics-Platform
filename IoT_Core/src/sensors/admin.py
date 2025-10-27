from django.contrib import admin

from .models import Metric

# Register your models here.


class MetricAdmin(admin.ModelAdmin):
    list_display = ("node_id", "temperature", "time")


admin.site.register(Metric, MetricAdmin)
