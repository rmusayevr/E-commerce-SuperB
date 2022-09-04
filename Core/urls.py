from django.urls import path
from .views import error, about_us, ContactUs, FAQ, index

urlpatterns = [
    path('404error/', error, name = "error"),
    path('about_us/', about_us, name = "about_us"),
    path('contact_us/', ContactUs.as_view(), name = "contact_us"),
    path('faq/', FAQ.as_view(), name = "faq"),
    path('', index, name = "index")
]