from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    # Data from Database / Model. Listings by order of date
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # If not checked "is published" in admin listings wont show
    print(listings)
    #Pagination at the bottom of the listings pages, adding 3
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings': page_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list =  Listing.objects.order_by('-list_date')
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']  # From field that has an attribute name  of keywords 
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city'] # From field that has an attribute name  of city
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # State
    if 'state' in request.GET:
        state = request.GET['state']   # From field that has an attribute name of state
        if state:
            queryset_list = queryset_list.filter(state__iexact=state) #iexact means exact match

    # Price
    if 'price' in request.GET:
        price = request.GET['price']   # From field that has an attribute name of price
        if price:
            queryset_list = queryset_list.filter(price__lte=price) # lte means less then or equal to

    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
