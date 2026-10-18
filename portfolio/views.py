"""
Views for Pinkal Rathod Personal Portfolio.
Connects public presentation pages to verified Django database models:
- SiteProfile: Owner profile information, contact details, narrative biography
- Education: Academic qualifications at Gujarat Vidyapith and secondary education
- Skill: Technical competencies categorized by functional domain
- Project: Coursework practicals and application projects
- Experience: Fresher Flutter developer career status

All database queries filter exclusively for active/published records.
Includes graceful fallbacks to verified data store if tables are empty.
Preserves existing interactive UI, animations, resume page, and ReportLab PDF download.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import (
    SiteProfile,
    Education,
    Skill,
    Project,
    Experience,
    SocialLink,
)
from .forms import ContactForm
from .data import (
    PERSONAL_INFO,
    EDUCATION_LIST,
    SKILLS_DATA,
    PROJECTS_DATA,
    RESUME_SKILLS,
    RESUME_PROJECTS,
)
from .pdf_generator import create_resume_pdf_buffer


def get_common_context():
    """
    Returns baseline personal and navigation context for all templates.
    Pulls from active SiteProfile in database with fallback to verified data dictionary.
    """
    profile = SiteProfile.objects.filter(is_active=True).first()
    
    # Check for social links in database (no fake links)
    linkedin_link = SocialLink.objects.filter(platform='LinkedIn', is_active=True).first()
    github_link = SocialLink.objects.filter(platform='GitHub', is_active=True).first()

    name = profile.name if profile else PERSONAL_INFO['name']
    title = profile.professional_title if profile else PERSONAL_INFO['title']
    location = profile.location if profile else PERSONAL_INFO.get('location', 'Ahmedabad, Gujarat, India')
    phone = profile.phone if profile else PERSONAL_INFO.get('phone', '7861040487')
    email = profile.personal_email if profile else PERSONAL_INFO['email']
    academic_email = profile.academic_email if profile else PERSONAL_INFO.get('academic_email', '')
    
    linkedin_url = linkedin_link.url if linkedin_link else PERSONAL_INFO.get('linkedin_url')
    github_url = github_link.url if github_link else PERSONAL_INFO.get('github_url')

    return {
        'name': name,
        'title': title,
        'college': PERSONAL_INFO['college'],
        'course': PERSONAL_INFO['course'],
        'education_period': PERSONAL_INFO['education_period'],
        'location': location,
        'phone': phone,
        'email': email,
        'academic_email': academic_email,
        'linkedin_url': linkedin_url,
        'github_url': github_url,
        'profile': profile,
    }


def home(request):
    """
    Renders the Home page with hero section, verified credentials,
    and preview sections for About, Education, Technical Interests,
    Projects, and Contact.
    """
    context = get_common_context()
    
    # Query published education entry from DB
    edu_qs = Education.objects.filter(is_published=True).order_by('display_order', '-created_at')
    edu_entry = edu_qs.first() if edu_qs.exists() else (EDUCATION_LIST[0] if EDUCATION_LIST else None)

    # Query published projects for preview
    projects_qs = Project.objects.filter(is_published=True).order_by('display_order', '-created_at')
    projects_list = list(projects_qs) if projects_qs.exists() else PROJECTS_DATA

    context.update({
        'typing_titles': [
            'Python Development',
            'Django Web Development',
            'Flutter App Development',
            'Android Development',
            'Frontend Development',
        ],
        'technical_interests': [
            {
                'name': 'Python',
                'icon': 'fa-brands fa-python',
                'desc': 'Core programming language for backend engineering, data structures, and computational scripting.',
                'tag': 'Core Language',
                'color_class': 'tech-python',
            },
            {
                'name': 'Django',
                'icon': 'fa-solid fa-layer-group',
                'desc': 'Full-stack web framework with Model-View-Template architecture, ORM queries, and secure user sessions.',
                'tag': 'Web Framework',
                'color_class': 'tech-django',
            },
            {
                'name': 'Flutter',
                'icon': 'fa-brands fa-flutter',
                'desc': 'Cross-platform mobile SDK building smooth Android and iOS applications with Dart and reactive widgets.',
                'tag': 'Mobile SDK',
                'color_class': 'tech-flutter',
            },
            {
                'name': 'Android Development',
                'icon': 'fa-brands fa-android',
                'desc': 'Native Android application development using Android Studio, Kotlin, Java, and local storage practicals.',
                'tag': 'Mobile Platform',
                'color_class': 'tech-android',
            },
            {
                'name': 'Frontend Development',
                'icon': 'fa-solid fa-code',
                'desc': 'Semantic HTML5 structure, responsive Bootstrap 5 grids, custom CSS3 themes, and DOM interactions in JavaScript.',
                'tag': 'UI & Web',
                'color_class': 'tech-html',
            },
            {
                'name': 'Database Management',
                'icon': 'fa-solid fa-database',
                'desc': 'Relational data modeling, table schemas, SQL queries, and local data persistence in SQLite and MySQL.',
                'tag': 'Data Storage',
                'color_class': 'tech-database',
            },
            {
                'name': 'Machine Learning',
                'icon': 'fa-solid fa-brain',
                'desc': 'Exploring image feature recognition, data preprocessing, and model classification workflows in Python.',
                'tag': 'AI & Data',
                'color_class': 'tech-ml',
            },
        ],
        'education_entry': edu_entry,
        'projects_list': projects_list,
        'has_resume': True,
        'has_linkedin': bool(context.get('linkedin_url')),
    })
    return render(request, 'portfolio/home.html', context)


def about(request):
    """
    Renders the About Me page with editable biography sections,
    technical focus areas, and academic background at Gujarat Vidyapith.
    Pulls published narrative from SiteProfile with fallback to verified defaults.
    """
    context = get_common_context()
    profile = context.get('profile')

    bio_intro = (profile.bio_intro if profile and profile.bio_intro else None) or PERSONAL_INFO.get('bio_intro', '')
    bio_programming = (profile.bio_programming if profile and profile.bio_programming else None) or PERSONAL_INFO.get('bio_programming', '')
    bio_web_mobile = (profile.bio_web_mobile if profile and profile.bio_web_mobile else None) or PERSONAL_INFO.get('bio_web_mobile', '')
    bio_database_ml = (profile.bio_database_ml if profile and profile.bio_database_ml else None) or PERSONAL_INFO.get('bio_database_ml', '')

    context.update({
        'bio_intro': bio_intro,
        'bio_programming': bio_programming,
        'bio_web_mobile': bio_web_mobile,
        'bio_database_ml': bio_database_ml,
        'technical_interests_cards': [
            {
                'title': 'Python & Django Architecture',
                'description': 'Constructing clean, secure backend services, database migrations, and Model-View-Template architectures.',
                'icon': 'fa-brands fa-python',
                'tag': 'Backend Focus'
            },
            {
                'title': 'Flutter Mobile Engineering',
                'description': 'Designing cross-platform client applications with responsive widgets, reactive state, and smooth UI animations.',
                'icon': 'fa-brands fa-flutter',
                'tag': 'Cross-Platform'
            },
            {
                'title': 'Android Native Development',
                'description': 'Exploring native Android development with Android Studio, Kotlin, Java, and local SQLite data storage.',
                'icon': 'fa-brands fa-android',
                'tag': 'Mobile Native'
            },
            {
                'title': 'Database Management',
                'description': 'Relational modeling with MySQL and SQLite, structured queries, and persistent local & cloud data storage.',
                'icon': 'fa-solid fa-database',
                'tag': 'Data Systems'
            },
            {
                'title': 'Modern Frontend Development',
                'description': 'Structuring semantic HTML5, modern CSS3 styling, Bootstrap 5 responsive grids, and vanilla JavaScript.',
                'icon': 'fa-solid fa-code',
                'tag': 'User Interface'
            },
            {
                'title': 'Machine Learning Concepts',
                'description': 'Studying classification algorithms, image feature analysis, and data preprocessing workflows in Python.',
                'icon': 'fa-solid fa-brain',
                'tag': 'Applied Intelligence'
            },
        ]
    })
    return render(request, 'about.html', context)


def education(request):
    """
    Renders the Education page with modern timeline cards.
    Queries published Education records from database with fallback to verified defaults.
    """
    context = get_common_context()
    edu_qs = Education.objects.filter(is_published=True).order_by('display_order', '-created_at')
    education_list = list(edu_qs) if edu_qs.exists() else EDUCATION_LIST

    context.update({
        'education_list': education_list,
    })
    return render(request, 'education.html', context)


def skills(request):
    """
    Renders the Technical Skills page categorized by domain.
    Queries published Skill records from database grouped by category, with fallback to verified defaults.
    """
    context = get_common_context()
    skills_qs = Skill.objects.filter(is_published=True).order_by('category', 'display_order', 'name')

    if skills_qs.exists():
        category_meta = {
            'Mobile Development': {
                'category_name': 'Mobile Development',
                'category_icon': 'fa-solid fa-mobile-screen',
                'description': 'Frameworks and tooling used for mobile applications.',
            },
            'Programming Languages': {
                'category_name': 'Programming Languages',
                'category_icon': 'fa-solid fa-code',
                'description': 'Core programming languages studied and practiced.',
            },
            'Web Development': {
                'category_name': 'Web Technologies & Frameworks',
                'category_icon': 'fa-solid fa-globe',
                'description': 'Technologies for crafting responsive frontend and backend systems.',
            },
            'Backend Framework': {
                'category_name': 'Backend Framework',
                'category_icon': 'fa-solid fa-layer-group',
                'description': 'Robust server architectures and database ORM systems.',
            },
            'Database Technologies': {
                'category_name': 'Database Technologies & Tools',
                'category_icon': 'fa-solid fa-database',
                'description': 'Relational databases, cloud services, and developer tooling.',
            },
            'Tools': {
                'category_name': 'Tools & Tooling',
                'category_icon': 'fa-solid fa-wrench',
                'description': 'Essential developer tooling and collaborative workflows.',
            },
        }

        skills_data = {}
        for category_choice, meta in category_meta.items():
            cat_skills = [s for s in skills_qs if s.category == category_choice]
            if cat_skills:
                skills_data[category_choice.lower().replace(' ', '_')] = {
                    'category_name': meta['category_name'],
                    'category_icon': meta['category_icon'],
                    'description': meta['description'],
                    'items': cat_skills,
                }
    else:
        skills_data = SKILLS_DATA

    context.update({
        'skills_data': skills_data,
    })
    return render(request, 'skills.html', context)


def projects(request):
    """
    Renders the Projects page with cards for software and coursework projects.
    Queries published Project records from database with fallback to verified defaults.
    """
    context = get_common_context()
    projects_qs = Project.objects.filter(is_published=True).order_by('display_order', '-created_at')
    projects_list = list(projects_qs) if projects_qs.exists() else PROJECTS_DATA

    context.update({
        'projects_list': projects_list,
    })
    return render(request, 'projects.html', context)


def resume(request):
    """
    Renders the professional interactive Resume page.
    Includes verified personal summary, education, technical skills,
    projects, experience, and download/print actions.
    Pulls from active SiteProfile if available.
    """
    context = get_common_context()
    profile = context.get('profile')

    personal_info = dict(PERSONAL_INFO)
    if profile:
        personal_info.update({
            'name': profile.name,
            'title': profile.professional_title,
            'location': profile.location,
            'phone': profile.phone,
            'personal_email': profile.personal_email,
            'academic_email': profile.academic_email,
            'email': profile.personal_email,
            'professional_summary': profile.professional_summary or PERSONAL_INFO['professional_summary'],
            'career_objective': profile.career_objective or PERSONAL_INFO['career_objective'],
        })

    context.update({
        'personal_info': personal_info,
        'career_objective': personal_info.get('career_objective', PERSONAL_INFO['career_objective']),
        'professional_summary': personal_info.get('professional_summary', PERSONAL_INFO['professional_summary']),
        'resume_skills': RESUME_SKILLS,
        'resume_projects': RESUME_PROJECTS,
        'education_list': EDUCATION_LIST,
        'work_experience': PERSONAL_INFO['work_experience'],
        'languages': PERSONAL_INFO['languages'],
    })
    return render(request, 'resume.html', context)


def resume_pdf(request):
    """
    Generates and returns an ATS-friendly, clean A4 PDF resume using ReportLab.
    Delivered as an attachment download: Pinkal_Rathod_Resume.pdf
    Pulls from active SiteProfile if available.
    """
    profile = SiteProfile.objects.filter(is_active=True).first()
    personal_info = dict(PERSONAL_INFO)
    if profile:
        personal_info.update({
            'name': profile.name,
            'title': profile.professional_title,
            'location': profile.location,
            'phone': profile.phone,
            'personal_email': profile.personal_email,
            'academic_email': profile.academic_email,
            'email': profile.personal_email,
            'professional_summary': profile.professional_summary or PERSONAL_INFO['professional_summary'],
            'career_objective': profile.career_objective or PERSONAL_INFO['career_objective'],
        })

    buffer = create_resume_pdf_buffer(
        personal_info=personal_info,
        education_list=EDUCATION_LIST,
        skills_list=RESUME_SKILLS,
        projects_list=RESUME_PROJECTS,
    )
    
    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Pinkal_Rathod_Resume.pdf"'
    return response


def contact(request):
    """
    Renders the Contact Me page and processes contact form submissions.
    Saves authentic inquiries into ContactMessage model for administrative review.
    Uses Post/Redirect/Get pattern and honeypot validation to prevent spam and duplicate submissions.
    """
    context = get_common_context()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            messages.success(
                request,
                f"Thank you, {contact_msg.name}! Your message has been sent successfully. "
                "I will review your inquiry and get back to you soon."
            )
            return redirect('portfolio:contact')
        else:
            messages.error(
                request,
                "Please correct the errors in the form below and submit again."
            )
    else:
        form = ContactForm()

    context.update({
        'form': form,
    })
    return render(request, 'contact.html', context)

