from django.contrib import admin
from django.contrib.auth.hashers import make_password 
# Model untuk Teachers
from .models.teachers import Teachers
# Model untuk Students
from .models.students import Students
# Model untuk Users
from .models.users import Users

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('nip', 'name', 'email', 'phone_number')
    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)
    
        user, created = Users.objects.get_or_create(username=obj.nip, defaults={
            'password': make_password('default_password'),
            'role': Users.TEACHER
        })

        if not created:
            user.role= Users.TEACHER
            user.save()



admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Students)
admin.site.register(Users)