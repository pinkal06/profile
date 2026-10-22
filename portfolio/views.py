"""
Views for Pinkal Rathod Personal Portfolio.
Pure static presentation data-driven architecture:
- Zero runtime SQLite/database dependencies
- Preserves all visual styling, responsive design, animations, and interactive components
- Uses verified data store from portfolio.data
- ATS-optimized ReportLab PDF resume generation
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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
    Uses verified static data dictionary without requiring database access.
    """
    return {
        'name': PERSONAL_INFO['name'],
        'title': PERSONAL_INFO['title'],
        'college': PERSONAL_INFO['college'],
        'course': PERSONAL_INFO['course'],
        'education_period': PERSONAL_INFO['education_period'],
        'location': PERSONAL_INFO.get('location', 'Ahmedabad, Gujarat, India'),
        'phone': PERSONAL_INFO.get('phone', '7861040487'),
        'email': PERSONAL_INFO['email'],
        'academic_email': PERSONAL_INFO.get('academic_email', ''),
        'linkedin_url': PERSONAL_INFO.get('linkedin_url'),
        'github_url': PERSONAL_INFO.get('github_url'),
        'profile': None,
    }


def home(request):
    """
    Renders the Home page with hero section, verified credentials,
    and preview sections for About, Education, Technical Interests,
    Projects, and Contact.
    """
    context = get_common_context()
    edu_entry = EDUCATION_LIST[0] if EDUCATION_LIST else None
    projects_list = PROJECTS_DATA

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
    Renders the About Me page with biography sections,
    technical focus areas, and academic background at Gujarat Vidyapith.
    """
    context = get_common_context()
    context.update({
        'bio_intro': PERSONAL_INFO.get('bio_intro', ''),
        'bio_programming': PERSONAL_INFO.get('bio_programming', ''),
        'bio_web_mobile': PERSONAL_INFO.get('bio_web_mobile', ''),
        'bio_database_ml': PERSONAL_INFO.get('bio_database_ml', ''),
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
    """
    context = get_common_context()
    context.update({
        'education_list': EDUCATION_LIST,
    })
    return render(request, 'education.html', context)


def skills(request):
    """
    Renders the Technical Skills page categorized by domain.
    """
    context = get_common_context()
    context.update({
        'skills_data': SKILLS_DATA,
    })
    return render(request, 'skills.html', context)


def projects(request):
    """
    Renders the Projects page with cards for software and coursework projects.
    """
    context = get_common_context()
    context.update({
        'projects_list': PROJECTS_DATA,
    })
    return render(request, 'projects.html', context)


def resume(request):
    """
    Renders the professional interactive Resume page.
    Includes verified personal summary, education, technical skills,
    projects, experience, and download/print actions.
    """
    context = get_common_context()
    context.update({
        'personal_info': PERSONAL_INFO,
        'career_objective': PERSONAL_INFO['career_objective'],
        'professional_summary': PERSONAL_INFO['professional_summary'],
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
    """
    buffer = create_resume_pdf_buffer(
        personal_info=PERSONAL_INFO,
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
    Uses Post/Redirect/Get pattern and honeypot validation to prevent spam.
    Operates without database dependency.
    """
    context = get_common_context()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            name = getattr(contact_msg, 'name', None) or form.cleaned_data.get('name', 'there')
            messages.success(
                request,
                f"Thank you, {name}! Your message has been sent successfully. "
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
