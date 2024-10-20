from django.db.models import Q
from .models import DataCris


def q_DataCris(query: str) -> DataCris:
    if query.isdigit() and len(query) <= 5:
        return DataCris.objects.filter(id=int(query))

    keywords: list[str] = [word for word in query.split() if len(word) > 1]

    q_objects: Q = Q()

    for token in keywords:
        q_objects |= Q(typ__icontains=token)
        q_objects |= Q(masa__icontains=token)
        q_objects |= Q(czystosc__contains=token)
        q_objects |= Q(barwa__icontains=token)
        q_objects |= Q(pochodzenie__icontains=token)
        q_objects |= Q(wlasciciel__icontains=token)

    return DataCris.objects.filter(q_objects)
