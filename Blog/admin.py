from django.contrib import admin
from .models import Blogs, Comments, Categories, Authors

admin.site.register(Categories)
admin.site.register(Blogs)
admin.site.register(Comments)
admin.site.register(Authors)