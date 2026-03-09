from django.db import models

class HomePage(models.Model):
    # Navbar section
    logo = models.ImageField(upload_to='logos/', default='logos/default.png')
    nav_home = models.CharField(max_length=50, default="Home")
    nav_about = models.CharField(max_length=50, default="About us")
    nav_courses = models.CharField(max_length=50, default="Courses")
    nav_gallery = models.CharField(max_length=50, default="Gallery")
    nav_contact = models.CharField(max_length=50, default="Contact us")
    nav_login = models.CharField(max_length=50, default="Login")

    # Hero section
    heading = models.CharField(max_length=200)
    sub_heading = models.TextField()
    button_text = models.CharField(max_length=50, default="Explore Courses")
    hero_image = models.ImageField(upload_to='home/')

    def __str__(self):
        return self.heading

class AboutSection(models.Model):
    title = models.CharField(max_length=200, default="About LingoSeed")
    description1 = models.TextField()
    description2 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about_images/')
    trainer_text = models.CharField(max_length=100, default="Qualified Trainers")
    skill_text = models.CharField(max_length=100, default="Skill-Based Learning")
    global_text = models.CharField(max_length=100, default="Global Communication Focus")

    def __str__(self):
        return self.title
    
class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    button_text = models.CharField(max_length=50, default="Learn More")
    bg_color = models.CharField(max_length=50, default="#2e5831")  # dark green default
    text_color = models.CharField(max_length=50, default="#ffffff")  # white text
    button_bg = models.CharField(max_length=50, default="#faebd7")  # light color button
    button_text_color = models.CharField(max_length=50, default="#000000")  # black button text

    def __str__(self):
        return self.title

class WhyChoose(models.Model):
    icon = models.ImageField(upload_to='why_icons/')
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    review = models.TextField()
    stars = models.IntegerField(default=5)
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name
    
class CourseName(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


from django.db import models

class FooterInfo(models.Model):
    logo = models.ImageField(upload_to='footer_logo/', blank=True, null=True)
    brand_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)

    # Quick Links
    home = models.CharField(max_length=100, default="Home")
    about = models.CharField(max_length=100, default="About")
    courses = models.CharField(max_length=100, default="Courses")
    contact = models.CharField(max_length=100, default="Contact")

    # Courses List
    course_list = models.TextField(help_text="Add courses separated by commas")

    # Contact Info
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    instagram = models.CharField(max_length=100)

    copyright_text = models.CharField(max_length=255, default="© 2025 LingoSeed Global English Academy.")

    def __str__(self):
        return self.brand_name

class About(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    button_text = models.CharField(max_length=50, default="Explore Courses")
    button_link = models.CharField(max_length=200, default="/courses/")
    teacher_image = models.ImageField(upload_to='about/')
    bg_color = models.CharField(max_length=20, default="#F6EFCE")  # screenshot background color
    text_color = models.CharField(max_length=20, default="#000")   # editable text color

    def __str__(self):
        return self.title
    
# class OurStory(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     image = models.ImageField(upload_to='about/story/')

#     def __str__(self):
#         return self.title
    
# class StorySection(models.Model):
#     mission_title = models.CharField(max_length=200, default="Our Mission")
#     mission_description = models.TextField()

#     vision_title = models.CharField(max_length=200, default="Vision & Values")

#     vision_text = models.TextField()
#     approach_text = models.TextField()
#     values_text = models.TextField()

#     icon1 = models.ImageField(upload_to="story_icons/", null=True, blank=True)
#     icon2 = models.ImageField(upload_to="story_icons/", null=True, blank=True)
#     icon3 = models.ImageField(upload_to="story_icons/", null=True, blank=True)

#     def __str__(self):
#         return "Our Story Section"
class OurStory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="our_story/", null=True, blank=True)

    def __str__(self):
        return self.title


class StorySection(models.Model):
    mission_title = models.CharField(max_length=200, default="Our Mission")
    mission_description = models.TextField()

    vision_title = models.CharField(max_length=200, default="Vision & Values")
    vision_text = models.TextField()
    approach_text = models.TextField()
    values_text = models.TextField()

    icon1 = models.ImageField(upload_to="story_icons/", null=True, blank=True)
    icon2 = models.ImageField(upload_to="story_icons/", null=True, blank=True)
    icon3 = models.ImageField(upload_to="story_icons/", null=True, blank=True)

    def __str__(self):
        return "Mission, Vision & Values Section"
class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to="team/")

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name
    
class Approach(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    button_text = models.CharField(max_length=100, default="Explore Courses")
    # button_link = models.URLField(default="#")

    class Meta:
        verbose_name = "Our Approach"
        verbose_name_plural = "Our Approach Content"

    def __str__(self):
        return self.title
    
class Footer(models.Model):
    logo = models.ImageField(upload_to="footer/")
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    copyright_text = models.CharField(max_length=200, default="© 2025 LingoSeed Global English Academy.")

    def __str__(self):
        return "Footer Settings"


class QuickLink(models.Model):
    home = models.CharField(max_length=100, default="Home")
    about = models.CharField(max_length=100, default="About")
    courses = models.CharField(max_length=100, default="Courses")
    contact = models.CharField(max_length=100, default="Contact")

    def __str__(self):
        return "Quick Links"   


class FooterCourse(models.Model):
    course_list = models.TextField(help_text="Add courses separated by commas")

    def __str__(self):
        return self.course_list



class ContactDetail(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    instagram = models.CharField(max_length=200)

    def __str__(self):
        return "Footer Contact Details"



class Course(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    duration = models.CharField(max_length=150)
    short_description = models.TextField()
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses/')

    def __str__(self):
        return self.title

class TeacherTrainingCourse(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    outcomes = models.TextField()
    
    
    image = models.ImageField(upload_to="courses/teachers/")

    def __str__(self):
        return self.title
class AdultCourse(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='adults/')

    def __str__(self):
        return self.title
    
class CourseRegistration(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    age = models.IntegerField()
    mode = models.CharField(max_length=10, choices=(('ONLINE','ONLINE'),('OFFLINE','OFFLINE')))
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    


class ContactPage(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.heading


class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    course_interest = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    whatsapp_qr = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.email

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username

