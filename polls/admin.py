from django.contrib import admin

from .models import Question

# Register your models here.

admin.site.register(Question)  # Question to appear on the admin section

# admin.site.register(Choice)  # This is presenting an error (Undefined variable). I will have to comeback to this later
