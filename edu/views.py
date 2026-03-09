from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    HomePage, AboutSection, Program, WhyChoose, Testimonial,
    About, OurStory, StorySection, TeamMember, Approach,
    Course, TeacherTrainingCourse, AdultCourse, CourseRegistration,
    Gallery, ContactPage, ContactFormSubmission
)
from .models import Contact, Course


def home(request):
    context = {
        "content": HomePage.objects.first(),
        "about": AboutSection.objects.first(),
        "programs": Program.objects.all(),
        "why": WhyChoose.objects.all(),
        "testimonials": Testimonial.objects.all(),
    }
    return render(request, 'edu/home.html', context)


def about_page(request):
    context = {
        "about": About.objects.first(),
        "story": OurStory.objects.first(),
        "story_section": StorySection.objects.first(), 
        "team": TeamMember.objects.all(),
        "approach": Approach.objects.first(),
    }
    return render(request, "edu/about.html", context)


# def courses(request):
#     context = {
#         "courses": Course.objects.all(),
#         "teacher_courses": TeacherTrainingCourse.objects.all(),
#         "adults": AdultCourse.objects.all(),
#     }
#     return render(request, 'edu/courses.html', context)
def courses(request):
    kids = Course.objects.all()
    teacher_courses = TeacherTrainingCourse.objects.all()
    adults = AdultCourse.objects.all()

    return render(request, "edu/courses.html", {
        "courses": kids,
        "teacher_courses": teacher_courses,
        "adults": adults,
    })

from django.shortcuts import render, get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Course, CourseRegistration

def register_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    errors = {}

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        mobile = request.POST.get("mobile", "").strip()
        age = request.POST.get("age", "").strip()
        mode = request.POST.get("mode", "")
        message = request.POST.get("message", "")
        course_name = request.POST.get("course", "").strip()

        # Validation
        if not name:
            errors["name"] = "Please enter your name."

        try:
            validate_email(email)
        except ValidationError:
            errors["email"] = "Please enter a valid email address."

        if not mobile.isdigit() or len(mobile) != 10:
            errors["mobile"] = "Please enter a valid 10-digit mobile number."

        try:
            age_value = int(age)
            if age_value <= 0:
                errors["age"] = "Please enter a valid positive age."
        except ValueError:
            errors["age"] = "Please enter a valid number for age."

        if not course_name:
            errors["course"] = "Please enter your course name."

        if not errors:
            CourseRegistration.objects.create(
                course=course,
                name=name,
                email=email,
                mobile=mobile,
                age=age,
                mode=mode,
                message=message,
            )
            # Redirect to success page
            return render(request, "edu/register_success.html", {"course": course})

    return render(
        request,
        "edu/register_course.html",
        {"course": course, "errors": errors},
    )


def register_success(request):
    return render(request, "edu/register_success.html")



def gallery(request):
    return render(request, "edu/gallery.html", {
        "items": Gallery.objects.all().order_by('-id')
    })
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactFormSubmission, Contact, Course
import re

def contact_page(request):
    page = {
        "heading": "Get in Touch",
        "description": "Questions about our courses or batches? Book a free trial or message us - We'll respond within 24 hours"
    }

    contact = Contact.objects.first()
    courses_list = Course.objects.values_list('title', flat=True)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        course_interest = request.POST.get('course_interest')
        message_text = request.POST.get('message')

        if not name or not email or not mobile or not course_interest or not message_text:
            messages.error(request, "All fields are required.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, "Please enter a valid email address.")
        elif not re.match(r"^[0-9]{10}$", mobile):
            messages.error(request, "Please enter a valid 10-digit mobile number.")
        else:
            # Save the submission
            ContactFormSubmission.objects.create(
                name=name,
                email=email,
                mobile=mobile,
                course_interest=course_interest,
                message=message_text
            )
            # Set success message
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # 🔑 must match urls.py name

    return render(request, "edu/contact.html", {
        "page": page,
        "contact": contact,
        "courses_list": courses_list,
    })

    
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password

def signup_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # ✅ Check required fields
        if not email or not password:
            messages.error(request, "All fields are required!")
            return redirect("signup")

        # ✅ Validate email format
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a valid email address!")
            return redirect("signup")

        # ✅ Check duplicate email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect("signup")

        # ✅ Validate password using Django's validators
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, "; ".join(e.messages))
            return redirect("signup")

        # ✅ Create user (use part before @ as username)
        username = email.split("@")[0]
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # ✅ Redirect to Login Page
        messages.success(request, "Signup successful! Please login.")
        return redirect("login")

    return render(request, "edu/signup.html")




# ✅ LOGIN VIEW
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, "Invalid Email!")
            return redirect("login")

        user_auth = authenticate(request, username=user.username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            messages.success(request, "Login Successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid Password!")
            return redirect("login")

    return render(request, "edu/login.html")

from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render

# def forgot_password(request):
#     message = ""
#     if request.method == "POST":
#         email = request.POST.get("email")
#         if email:
#             message = "Password reset link has been sent to your email!"
#         else:
#             message = "Please enter a valid email address."
#     return render(request, "edu/forgot_password.html", {"message": message})

# views.py
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# Optional: custom wrapper to reuse your template name if you want exactly "edu/forgot_password.html"
class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = "edu/forgot_password.html"            # HTML form shown to user
    email_template_name = "registration/password_reset_email.txt"  # the email body sent
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy('password_reset_done')    # where to redirect after submit

# Keep any other views below


