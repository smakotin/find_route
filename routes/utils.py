from trains.models import Train


def get_graph(qs):
    ...

def get_routes(request, form) -> dict:
    qs = Train.objects.all()
