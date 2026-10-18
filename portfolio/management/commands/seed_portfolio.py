"""
Idempotent Database Population Management Command for Pinkal Rathod Portfolio.
Seeds initial verified portfolio records into SQLite via Django ORM:
- SiteProfile
- Education
- Skill
- Project
- Experience

Safe to run repeatedly without creating duplicate records (uses update_or_create).
Does NOT create superusers or inject fake data.
"""

from django.core.management.base import BaseCommand
from portfolio.models import (
    SiteProfile,
    Education,
    Skill,
    Project,
    Experience,
    SocialLink,
)


class Command(BaseCommand):
    help = "Populate database with verified initial portfolio records without duplicates."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding verified portfolio data..."))

        # 1. SiteProfile
        profile, created = SiteProfile.objects.update_or_create(
            name="Pinkal Rathod",
            defaults={
                "professional_title": "ASPIRING FLUTTER DEVELOPER | BCA STUDENT",
                "location": "Ahmedabad, Gujarat, India",
                "phone": "7861040487",
                "personal_email": "pinkalrathod2007@gmail.com",
                "academic_email": "240130510053.cs@gujaratvidyapith.org",
                "short_intro": (
                    "Motivated BCA student at Gujarat Vidyapith focused on Flutter mobile application development "
                    "using Flutter and Dart, alongside full-stack web foundations in Python Django."
                ),
                "biography": (
                    "Motivated BCA student focused on Flutter mobile application development using Flutter and Dart. "
                    "Developed a Flutter-based marketplace project, RetiyaMarket, and a Python Django-based fashion e-commerce "
                    "website, VELORIA. Possess basic knowledge of Python, Django, HTML, CSS, JavaScript, and database technologies. "
                    "Interested in building attractive, responsive, and user-friendly mobile applications. Seeking a Flutter Developer "
                    "Internship or entry-level opportunity to improve technical skills and contribute to real-world mobile application projects."
                ),
                "bio_intro": (
                    "Hello! I am Pinkal Rathod, an aspiring software developer and Bachelor of Computer Applications (BCA) "
                    "student at Gujarat Vidyapith, Ahmedabad (2025 – Present). I am focused on Flutter mobile application "
                    "development and Python Django web technologies."
                ),
                "bio_programming": (
                    "My programming foundations began with Dart and Python, exploring object-oriented design, algorithmic "
                    "thinking, and clean architectural patterns. I enjoy turning software requirements into responsive, "
                    "efficient code."
                ),
                "bio_web_mobile": (
                    "In mobile engineering, I focus on Flutter and Dart to build interactive cross-platform applications like RetiyaMarket. "
                    "On the web, I develop full-stack applications using Python and Django, coupled with modern HTML5, CSS3, JavaScript, "
                    "and Bootstrap, exemplified by my VELORIA fashion e-commerce project."
                ),
                "bio_database_ml": (
                    "My academic coursework also covers database technologies including MySQL and SQLite, along with foundational "
                    "machine learning concepts and Android native development."
                ),
                "career_objective": (
                    "To build a career as a Flutter Developer by developing reliable, responsive, and user-friendly "
                    "mobile applications while continuously improving Flutter and Dart programming skills."
                ),
                "professional_summary": (
                    "Motivated BCA student focused on Flutter mobile application development using Flutter and Dart. "
                    "Developed a Flutter-based marketplace project, RetiyaMarket, and a Python Django-based fashion e-commerce "
                    "website, VELORIA. Possess basic knowledge of Python, Django, HTML, CSS, JavaScript, and database technologies. "
                    "Interested in building attractive, responsive, and user-friendly mobile applications. Seeking a Flutter Developer "
                    "Internship or entry-level opportunity to improve technical skills and contribute to real-world mobile application projects."
                ),
                "is_active": True,
            }
        )
        status_txt = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"  [Profile] {status_txt}: {profile.name}"))

        # 2. Education Records
        education_data = [
            {
                "institution": "Gujarat Vidyapith, Ahmedabad, Gujarat",
                "degree": "Bachelor of Computer Applications (BCA)",
                "department": "Computer Science",
                "qualification_type": "bca",
                "study_period": "2025 – Present",
                "start_year": 2025,
                "end_year": None,
                "passing_year": None,
                "semester": "Semester 4",
                "cgpa": 7.73,
                "percentage": None,
                "percentile_rank": None,
                "description": (
                    "Core curriculum focusing on mobile and web software engineering, data structures, "
                    "relational database architectures, and computational problem solving."
                ),
                "display_order": 1,
                "is_published": True,
            },
            {
                "institution": "Higher Secondary Certificate (12th – Science)",
                "degree": "12th Science",
                "department": "Science Stream",
                "qualification_type": "12th",
                "study_period": "Passing Year: 2024",
                "start_year": None,
                "end_year": None,
                "passing_year": 2024,
                "semester": "",
                "cgpa": None,
                "percentage": 63.38,
                "percentile_rank": None,
                "description": "Secondary science coursework providing strong analytical and mathematical fundamentals.",
                "display_order": 2,
                "is_published": True,
            },
            {
                "institution": "Secondary School Certificate (10th)",
                "degree": "10th SSC",
                "department": "General Education",
                "qualification_type": "10th",
                "study_period": "Passing Year: 2022",
                "start_year": None,
                "end_year": None,
                "passing_year": 2022,
                "semester": "",
                "cgpa": None,
                "percentage": 69.50,
                "percentile_rank": 78.35,
                "description": "Foundational high school education completed with distinction in percentile rank.",
                "display_order": 3,
                "is_published": True,
            },
        ]
        for edu in education_data:
            obj, created = Education.objects.update_or_create(
                institution=edu["institution"],
                degree=edu["degree"],
                defaults=edu,
            )
            act = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"  [Education] {act}: {obj.degree}"))

        # 3. Technical Skills
        skills_data = [
            # Mobile Development
            {"name": "Flutter", "category": "Mobile Development", "proficiency_label": "Core Focus", "description": "Widget trees, reactive UI, Android & iOS cross-platform", "icon_class": "fa-brands fa-flutter", "color_class": "tech-flutter", "display_order": 1},
            {"name": "Dart", "category": "Mobile Development", "proficiency_label": "Primary Focus", "description": "Object-oriented application logic in Flutter SDK", "icon_class": "fa-solid fa-bullseye", "color_class": "tech-dart", "display_order": 2},
            {"name": "Android Studio", "category": "Mobile Development", "proficiency_label": "Official IDE", "description": "Android SDK, emulators, layout XML & Gradle build system", "icon_class": "fa-brands fa-android", "color_class": "tech-android", "display_order": 3},
            # Programming Languages
            {"name": "Dart", "category": "Programming Languages", "proficiency_label": "Primary Focus", "description": "Flutter framework application state & widgets", "icon_class": "fa-solid fa-bullseye", "color_class": "tech-dart", "display_order": 1},
            {"name": "Python (Basic)", "category": "Programming Languages", "proficiency_label": "Basic Knowledge", "description": "Scripting, backend logic, data fundamentals", "icon_class": "fa-brands fa-python", "color_class": "tech-python", "display_order": 2},
            {"name": "Java", "category": "Programming Languages", "proficiency_label": "Core Language", "description": "OOP fundamentals, Android development practicals", "icon_class": "fa-brands fa-java", "color_class": "tech-java", "display_order": 3},
            {"name": "Kotlin", "category": "Programming Languages", "proficiency_label": "Android Development", "description": "Native Android practicals & UI", "icon_class": "fa-solid fa-terminal", "color_class": "tech-kotlin", "display_order": 4},
            # Web Development
            {"name": "HTML5", "category": "Web Development", "proficiency_label": "Markup Standard", "description": "Semantic page structure & accessible DOM", "icon_class": "fa-brands fa-html5", "color_class": "tech-html", "display_order": 1},
            {"name": "CSS3", "category": "Web Development", "proficiency_label": "Styling & Layout", "description": "Responsive flexbox/grid, animations & themes", "icon_class": "fa-brands fa-css3-alt", "color_class": "tech-css", "display_order": 2},
            {"name": "JavaScript (Basic)", "category": "Web Development", "proficiency_label": "Basic Knowledge", "description": "DOM manipulation, dynamic interactions & events", "icon_class": "fa-brands fa-js", "color_class": "tech-js", "display_order": 3},
            {"name": "Bootstrap", "category": "Web Development", "proficiency_label": "CSS Framework", "description": "Mobile-first components & responsive utilities", "icon_class": "fa-brands fa-bootstrap", "color_class": "tech-bootstrap", "display_order": 4},
            # Backend Framework
            {"name": "Django (Basic)", "category": "Backend Framework", "proficiency_label": "Basic Knowledge", "description": "MVT architecture, ORM queries, routing & admin security", "icon_class": "fa-solid fa-layer-group", "color_class": "tech-django", "display_order": 1},
            # Database Technologies
            {"name": "MySQL", "category": "Database Technologies", "proficiency_label": "Relational DB", "description": "Relational schemas, SQL queries, indexing", "icon_class": "fa-solid fa-database", "color_class": "tech-mysql", "display_order": 1},
            {"name": "SQLite", "category": "Database Technologies", "proficiency_label": "Embedded DB", "description": "Lightweight development storage, Android local DB", "icon_class": "fa-solid fa-server", "color_class": "tech-sqlite", "display_order": 2},
            {"name": "Firebase (Basic)", "category": "Database Technologies", "proficiency_label": "Basic Knowledge", "description": "Cloud storage, real-time database, auth", "icon_class": "fa-solid fa-fire", "color_class": "tech-firebase", "display_order": 3},
            # Tools & Tooling
            {"name": "Git", "category": "Tools", "proficiency_label": "Version Control", "description": "Branching, committing, and code version control", "icon_class": "fa-brands fa-git-alt", "color_class": "tech-git", "display_order": 1},
            {"name": "GitHub", "category": "Tools", "proficiency_label": "Code Hosting", "description": "Remote repositories and open source collaboration", "icon_class": "fa-brands fa-github", "color_class": "tech-git", "display_order": 2},
            {"name": "XAMPP", "category": "Tools", "proficiency_label": "Local Server", "description": "Apache & MySQL local testing environment", "icon_class": "fa-solid fa-server", "color_class": "tech-xampp", "display_order": 3},
        ]
        for sk in skills_data:
            obj, created = Skill.objects.update_or_create(
                name=sk["name"],
                category=sk["category"],
                defaults=sk,
            )
            act = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"  [Skill] {act}: {obj.name} ({obj.category})"))

        # 4. Verified Projects
        projects_data = [
            {
                "title": "RetiyaMarket – Flutter Mobile Application",
                "slug": "retiyamarket",
                "category": "Mobile Application",
                "status": "in_progress",
                "technologies": "Flutter, Dart, MySQL",
                "short_description": "A mobile marketplace project focused on buying and selling products.",
                "detailed_description": (
                    "Developed a mobile marketplace project focused on buying and selling products. "
                    "Worked on a user-friendly mobile interface for a student marketplace. "
                    "Planned marketplace features such as product listings, user authentication, wishlist, chat, and order management. "
                    "(Note: Planned features are actively in coursework development and not marked as completed)."
                ),
                "icon": "fa-solid fa-cart-shopping",
                "art_class": "art-retiyamarket",
                "accent_color": "#38bdf8",
                "display_order": 1,
                "is_featured": True,
                "is_published": True,
            },
            {
                "title": "VELORIA – Fashion E-Commerce Website",
                "slug": "veloria",
                "category": "Web Application",
                "status": "in_progress",
                "technologies": "Python, Django, HTML, CSS, Bootstrap, JavaScript",
                "short_description": "A fashion e-commerce website project focused on product presentation and shopping UI.",
                "detailed_description": (
                    "Created a fashion e-commerce website project with a modern shopping interface. "
                    "Worked on product categories and the design of a responsive shopping experience. "
                    "Explored features such as user authentication, shopping cart, and wishlist."
                ),
                "icon": "fa-solid fa-bag-shopping",
                "art_class": "art-veloria",
                "accent_color": "#ec4899",
                "display_order": 2,
                "is_featured": True,
                "is_published": True,
            },
            {
                "title": "GameZone – Gaming Platform",
                "slug": "gamezone",
                "category": "Web Platform Concept",
                "status": "planned",
                "technologies": "JavaScript, HTML5, CSS3",
                "short_description": "A gaming platform concept for browsing and playing games.",
                "detailed_description": (
                    "GameZone explores a modern interactive web hub for casual browser games. "
                    "The design features game genre filtering, leaderboard cards, game showcase tiles, "
                    "and responsive player controls using modern JavaScript and semantic HTML5."
                ),
                "icon": "fa-solid fa-gamepad",
                "art_class": "art-gamezone",
                "accent_color": "#8b5cf6",
                "display_order": 3,
                "is_featured": True,
                "is_published": True,
            },
            {
                "title": "Animal Classification – Machine Learning Project",
                "slug": "animal-classification",
                "category": "Machine Learning",
                "status": "in_progress",
                "technologies": "Python, Machine Learning, Data Preprocessing, Image Classification",
                "short_description": "An animal-classification machine learning project.",
                "detailed_description": (
                    "An academic exploration into computer vision and machine learning fundamentals. "
                    "Involves collecting and preprocessing image datasets of diverse animal classes, "
                    "extracting visual features, and training lightweight classification models using Python."
                ),
                "icon": "fa-solid fa-paw",
                "art_class": "art-animal",
                "accent_color": "#10b981",
                "display_order": 4,
                "is_featured": False,
                "is_published": True,
            },
            {
                "title": "Android Student Data Storage – Android Practical",
                "slug": "android-student-storage",
                "category": "Mobile Practical",
                "status": "in_progress",
                "technologies": "Android Studio, Java / Kotlin, SQLite, Android SDK",
                "short_description": "An Android learning project related to student data storage.",
                "detailed_description": (
                    "An Android practical application demonstrating local mobile persistence. "
                    "Implements structured SQLite database helpers, CRUD operations for student records, "
                    "clean form inputs with validation, and responsive RecyclerView lists."
                ),
                "icon": "fa-solid fa-mobile-screen-button",
                "art_class": "art-android-storage",
                "accent_color": "#f59e0b",
                "display_order": 5,
                "is_featured": False,
                "is_published": True,
            },
        ]
        for prj in projects_data:
            obj, created = Project.objects.update_or_create(
                slug=prj["slug"],
                defaults=prj,
            )
            act = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"  [Project] {act}: {obj.title}"))

        # 5. Experience (Fresher status)
        exp, created = Experience.objects.update_or_create(
            role="Fresher | Flutter Mobile App Development",
            defaults={
                "organization": "",
                "employment_type": "fresher",
                "description": (
                    "Seeking an opportunity to begin a professional career in Flutter development, "
                    "gain hands-on industry experience, and build cross-platform mobile applications."
                ),
                "is_current": True,
                "is_published": True,
                "display_order": 1,
            }
        )
        act = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"  [Experience] {act}: {exp.role}"))

        # 6. Social Links (Verified LinkedIn profile)
        social, created = SocialLink.objects.update_or_create(
            platform="LinkedIn",
            defaults={
                "label": "Pinkal Rathod on LinkedIn",
                "url": "https://www.linkedin.com/in/pinkal-rathod-a303183b4/",
                "display_order": 1,
                "is_active": True,
            }
        )
        act = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"  [SocialLink] {act}: {social.platform} ({social.url})"))

        self.stdout.write(self.style.SUCCESS("\nSuccessfully seeded verified portfolio records!"))

