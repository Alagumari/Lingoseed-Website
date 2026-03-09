from edu.models import Footer, QuickLink, FooterCourse, ContactDetail

def global_footer(request):
    footer = Footer.objects.first()
    quick_links = QuickLink.objects.all()
    footer_courses = FooterCourse.objects.first()
    course_list = []

    if footer_courses and footer_courses.course_list:
        course_list = [c.strip() for c in footer_courses.course_list.split(",")]

    contact = ContactDetail.objects.first()

    return {
        "footer": footer,
        "quick_links": quick_links,
        "courses_list": course_list,
        "contact": contact,
    }


