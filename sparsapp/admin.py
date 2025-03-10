from django.contrib import admin
from .models import Project , profile ,wallet
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.register(Project)

class profileInline(admin.StackedInline):
	model=profile

class UserAdmin(admin.ModelAdmin):
	model = User

	fields=["username"]
	inline=[profileInline]

admin.site.unregister(User)
admin.site.register(profile)
admin.site.register(wallet)
admin.site.register(User,UserAdmin)	