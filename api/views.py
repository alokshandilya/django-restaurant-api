from rest_framework.decorators import api_view
from rest_framework.response import Response

from menu.models import Item

from .serializers import ItemSerializer

# serialization: converting complex data types (like models, QuerySets) into
# simpler data types (like dictionaries) that can be easily converted to JSON

# deserialization: converting JSON data into complex data types (like models,
# QuerySets) by validating the data and saving it to the database/model


@api_view(["GET"])
def get_items(request):
    items = Item.objects.all()

    # many=True for QuerySets with multiple instances
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_item(request, id):
    item = Item.objects.get(id=id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
