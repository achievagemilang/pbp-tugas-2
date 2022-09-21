from django.urls import path
from mywatchlist.views import show_mywatchlist_html, show_mywatchlist_json, show_mywatchlist_xml

app_name = "mywatchlist"
urlpatterns = [
    path("html/", show_mywatchlist_html, name="show_mywatchlist_html"),
    path("json/", show_mywatchlist_json, name="show_mywatchlist_json"),
    path("xml/", show_mywatchlist_xml, name="show_mywatchlist_xml"),
]