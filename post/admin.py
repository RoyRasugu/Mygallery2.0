from django.contrib import admin
from post.models import Image, Stream,Tag,Follow

# Register your models here.
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Stream)

