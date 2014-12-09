from django.contrib import admin
from .models import Batch, StudentGroup, Student, GroupPreference, Selection


admin.site.register(Batch)
admin.site.register(StudentGroup)
admin.site.register(Student)
admin.site.register(GroupPreference)
admin.site.register(Selection)
