from ninja import NinjaAPI, Schema, ModelSchema, Router
from backend.models import (
    Client,
    Host,
    Region,
    Product,
    Booking,
    Available,
)

from .api_schemas import (
    RegionSchema,
    UserSchema,
    UserPostSchema,
    HostSchema,
    HostPostSchema,
    HostPatchSchema,
    ProductSchema,
    BookingSchema,
    BookingPostSchema,
    AvailableSchema,
)

from backend.auth import group_auth

from typing import List
from django.shortcuts import get_object_or_404
from datetime import date, timedelta

router = Router(auth=lambda request: group_auth(request, "host")) #request defineras vid call, gruppnamnet är statiskt

@router.get("/activerequests") #Visa mängden aktiva förfrågningar
def fetchactiverequests(request):
    host = Host.objects.get(user=request.user)
    pending_bookings = Booking.objects.filter(product__host=host, status__Description='pending').count()

    return pending_bookings