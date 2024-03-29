from django.contrib import admin
from .models import (
  UserProfile,
  ContactProfile,
  Testimonial,
  Media,
  Portfolio,
  Blog,
  Certificate,
  Skill
)

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('id', 'user')

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'timestamp', 'name')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

@admin.register(Portfolio)
class PortfoliolAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_active')
  readonly_fields = ('sluq')