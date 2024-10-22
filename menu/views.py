from django.http import JsonResponse

from .models import Item


# Create your views here.
def index(request):
    items = Item.objects.all()
    # items: QuerySet of Item model instances

    # items.values(): Value QuerySet, list of dictionaries
    # each dictionary represents a row from the database
    return JsonResponse({"items": list(items.values())})
