from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

mywatchlist_data = MyWatchList.objects.all()
context = {
    "name": "Achieva Futura Gemilang",
    "student_id": "2106750452",
    "mywatchlist": mywatchlist_data,
    "mywatchlist_watched": sum([i.watched for i in mywatchlist_data]),
    "mywatchlist_not_watched": sum([not i.watched for i in mywatchlist_data]),
}
def show_watchlist(request):
    return render(
        request,
        "mywatchlist.html",
        context,
    )

def show_watchlist_json(request):
    return HttpResponse(
        serializers.serialize("json", mywatchlist_data), content_type="application/json"
    )

def show_watchlist_xml(request):
    return HttpResponse(
        serializers.serialize("xml", mywatchlist_data), content_type="application/xml"
    )