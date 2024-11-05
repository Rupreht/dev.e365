from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "get_title",
        "upc",
        "get_product_class",
        "structure",
        "attribute_summary",
        "date_created",
        "video_url",
    )


from oscar.apps.catalogue.admin import *  # pylint: disable=wildcard-import,unused-wildcard-import
