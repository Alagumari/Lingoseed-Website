from django.contrib import admin
from .models import About
from .models import HomePage
from .models import AboutSection
from .models import Program
from .models import WhyChoose
from .models import Testimonial
from .models import FooterInfo
from .models import OurStory
from .models import StorySection
from .models import TeamMember
from .models import Approach
from .models import Footer, QuickLink, FooterCourse, ContactDetail
from .models import Course, TeacherTrainingCourse, AdultCourse
from .models import Gallery





admin.site.register(AboutSection)
admin.site.register(HomePage)
admin.site.register(Program)
admin.site.register(WhyChoose)
admin.site.register(Testimonial)
admin.site.register(FooterInfo)

admin.site.register(About)
admin.site.register(OurStory)
admin.site.register(StorySection)
admin.site.register(TeamMember)
admin.site.register(Approach)
admin.site.register(Footer)
admin.site.register(QuickLink)
admin.site.register(FooterCourse)
admin.site.register(ContactDetail)
from .models import ContactPage, ContactFormSubmission





class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'duration', 'price')
admin.site.register(TeacherTrainingCourse)
admin.site.register(AdultCourse)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Gallery, GalleryAdmin)

admin.site.register(ContactPage)
admin.site.register(ContactFormSubmission)
    


# @admin.register(ContactPage)
# class ContactPageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'message')


from .models import Contact
from django.utils.html import mark_safe

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('phone', 'email', 'whatsapp_qr')
# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('phone', 'email', 'qr_preview')

#     def qr_preview(self, obj):
#         if obj.whatsapp_qr:
#             return mark_safe(f'<img src="{obj.whatsapp_qr.url}" width="70" height="70" />')
#         return "(No QR)"

#     qr_preview.short_description = "QR Code"
from django.contrib import admin
from django.utils.html import mark_safe
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone','show_qr')

    def show_qr(self, obj):
        if obj.whatsapp_qr:
            return mark_safe(f'<img src="{obj.whatsapp_qr.url}" width="60" height="60" style="border-radius:5px;" />')
        return "No QR"
        
    show_qr.short_description = "QR Code"

from django.contrib import admin
from .models import Course, CourseRegistration

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    search_fields = ("title",)

@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "mobile", "course", "mode", "age", "created_at")
    list_filter = ("course", "mode", "created_at")
    search_fields = ("name", "email", "mobile")
    ordering = ("-created_at",)
    
from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile

# Show User Profile in Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'user__email', 'phone')

admin.site.register(UserProfile, UserProfileAdmin)


