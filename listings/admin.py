from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # Able to click on id or title as a link to go to the page in the admin section
    list_filter = ('realtor', )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode') # Adds searh field in admin section
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

