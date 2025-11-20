from django.contrib import admin
from .models import Worker, Role, Project, Payment, Schedule

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id','name','worker_type','phone','email','is_available','joined_date')
    search_fields = ('name','worker_type','email','phone')

admin.site.register(Role)
admin.site.register(Project)
admin.site.register(Payment)
admin.site.register(Schedule)
