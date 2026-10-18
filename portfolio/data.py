"""
Pinkal Rathod Portfolio – Verified Presentation Data Store
This module holds structured presentation data for Pinkal Rathod's personal portfolio.
Strictly adheres to verified credentials without invented information.
Designed for easy migration to Django models in Phase 5.
"""

PERSONAL_INFO = {
    'name': 'Pinkal Rathod',
    'title': 'ASPIRING FLUTTER DEVELOPER | BCA STUDENT',
    'college': 'Gujarat Vidyapith, Ahmedabad, Gujarat',
    'department': 'Computer Science',
    'course': 'Bachelor of Computer Applications (BCA)',
    'education_period': '2025 – Present',
    'location': 'Ahmedabad, Gujarat, India',
    'phone': '7861040487',
    'personal_email': 'pinkalrathod2007@gmail.com',
    'academic_email': '240130510053.cs@gujaratvidyapith.org',
    'email': 'pinkalrathod2007@gmail.com',
    'short_intro': (
        'Motivated BCA student at Gujarat Vidyapith focused on Flutter mobile application development '
        'using Flutter and Dart, alongside full-stack web foundations in Python Django.'
    ),
    'career_objective': (
        'To build a career as a Flutter Developer by developing reliable, responsive, and user-friendly '
        'mobile applications while continuously improving Flutter and Dart programming skills.'
    ),
    'professional_summary': (
        'Motivated BCA student focused on Flutter mobile application development using Flutter and Dart. '
        'Developed a Flutter-based marketplace project, RetiyaMarket, and a Python Django-based fashion e-commerce '
        'website, VELORIA. Possess basic knowledge of Python, Django, HTML, CSS, JavaScript, and database technologies. '
        'Interested in building attractive, responsive, and user-friendly mobile applications. Seeking a Flutter Developer '
        'Internship or entry-level opportunity to improve technical skills and contribute to real-world mobile application projects.'
    ),
    'bio_intro': (
        'Hello! I am Pinkal Rathod, an aspiring software developer and Bachelor of Computer Applications (BCA) '
        'student at Gujarat Vidyapith, Ahmedabad (2025 – Present). I am focused on Flutter mobile application '
        'development and Python Django web technologies.'
    ),
    'bio_programming': (
        'My programming foundations began with Dart and Python, exploring object-oriented design, algorithmic '
        'thinking, and clean architectural patterns. I enjoy turning software requirements into responsive, '
        'efficient code.'
    ),
    'bio_web_mobile': (
        'In mobile engineering, I focus on Flutter and Dart to build interactive cross-platform applications like RetiyaMarket. '
        'On the web, I develop full-stack applications using Python and Django, coupled with modern HTML5, CSS3, JavaScript, '
        'and Bootstrap, exemplified by my VELORIA fashion e-commerce project.'
    ),
    'bio_database_ml': (
        'My academic coursework also covers database technologies including MySQL and SQLite, along with foundational '
        'machine learning concepts and Android native development.'
    ),
    'work_experience': {
        'role': 'Fresher | Flutter Mobile App Development',
        'details': (
            'Seeking an opportunity to begin a professional career in Flutter development, '
            'gain hands-on industry experience, and build cross-platform mobile applications.'
        )
    },
    'languages': ['Gujarati', 'Hindi', 'English'],
    'linkedin_url': 'https://www.linkedin.com/in/pinkal-rathod-a303183b4/',
    'github_url': None,     # Kept editable, not invented
}

EDUCATION_LIST = [
    {
        'institution': 'Gujarat Vidyapith, Ahmedabad, Gujarat',
        'degree': 'Bachelor of Computer Applications (BCA)',
        'department': 'Computer Science',
        'period': '2025 – Present',
        'status': 'Currently Pursuing',
        'is_current': True,
        'cgpa': '7.73 after Semester 4',
        'score_label': 'CGPA',
        'score_value': '7.73 (after Sem 4)',
        'icon': 'fa-solid fa-graduation-cap',
        'description': (
            'Core curriculum focusing on mobile and web software engineering, data structures, '
            'relational database architectures, and computational problem solving.'
        ),
    },
    {
        'institution': 'Higher Secondary Certificate (12th – Science)',
        'degree': '12th Science',
        'department': 'Science Stream',
        'period': 'Passing Year: 2024',
        'status': 'Completed',
        'is_current': False,
        'percentage': '63.38%',
        'score_label': 'Percentage',
        'score_value': '63.38%',
        'icon': 'fa-solid fa-school',
        'description': 'Secondary science coursework providing strong analytical and mathematical fundamentals.',
    },
    {
        'institution': 'Secondary School Certificate (10th)',
        'degree': '10th SSC',
        'department': 'General Education',
        'period': 'Passing Year: 2022',
        'status': 'Completed',
        'is_current': False,
        'percentage': '69.50%',
        'percentile_rank': '78.35',
        'score_label': 'Percentage / Percentile',
        'score_value': '69.50% (PR: 78.35)',
        'icon': 'fa-solid fa-award',
        'description': 'Foundational high school education completed with distinction in percentile rank.',
    }
]

RESUME_SKILLS = [
    {
        'category': 'Mobile Development',
        'icon': 'fa-solid fa-mobile-screen-button',
        'skills': ['Flutter', 'Dart', 'Android Studio'],
    },
    {
        'category': 'Programming Languages',
        'icon': 'fa-solid fa-code',
        'skills': ['Dart', 'Python (Basic)'],
    },
    {
        'category': 'Web Technologies',
        'icon': 'fa-solid fa-globe',
        'skills': ['HTML5', 'CSS3', 'JavaScript (Basic)', 'Bootstrap'],
    },
    {
        'category': 'Backend Framework',
        'icon': 'fa-solid fa-layer-group',
        'skills': ['Django (Basic)'],
    },
    {
        'category': 'Database Technologies',
        'icon': 'fa-solid fa-database',
        'skills': ['MySQL', 'SQLite', 'Firebase (Basic)'],
    },
    {
        'category': 'Tools & Platforms',
        'icon': 'fa-solid fa-wrench',
        'skills': ['Git', 'GitHub', 'Android Studio', 'XAMPP'],
    },
]

RESUME_PROJECTS = [
    {
        'title': 'RetiyaMarket – Flutter Mobile Application',
        'technologies': 'Flutter, Dart, MySQL',
        'category': 'Mobile Application',
        'points': [
            'Developed a mobile marketplace project focused on buying and selling products.',
            'Worked on a user-friendly mobile interface for a student marketplace.',
            'Planned marketplace features such as product listings, user authentication, wishlist, chat, and order management.',
        ],
    },
    {
        'title': 'VELORIA – Fashion E-Commerce Website',
        'technologies': 'Python, Django, HTML, CSS, Bootstrap, JavaScript',
        'category': 'Web Application',
        'points': [
            'Created a fashion e-commerce website project with a modern shopping interface.',
            'Worked on product categories and the design of a responsive shopping experience.',
            'Explored features such as user authentication, shopping cart, and wishlist.',
        ],
    },
]

SKILLS_DATA = {
    'mobile_development': {
        'category_name': 'Mobile Development',
        'category_icon': 'fa-solid fa-mobile-screen',
        'description': 'Frameworks and tooling used for mobile applications.',
        'items': [
            {'name': 'Flutter', 'icon': 'fa-brands fa-flutter', 'status': 'Core Focus', 'focus': 'Widget trees, reactive UI, Android & iOS', 'color_class': 'tech-flutter'},
            {'name': 'Dart', 'icon': 'fa-solid fa-bullseye', 'status': 'Mobile Language', 'focus': 'Object-oriented application logic in Flutter', 'color_class': 'tech-dart'},
            {'name': 'Android Studio', 'icon': 'fa-brands fa-android', 'status': 'Official IDE', 'focus': 'Android SDK, emulators, layout XML & Gradle', 'color_class': 'tech-android'},
        ]
    },
    'programming_languages': {
        'category_name': 'Programming Languages',
        'category_icon': 'fa-solid fa-code',
        'description': 'Core programming languages studied and practiced.',
        'items': [
            {'name': 'Dart', 'icon': 'fa-solid fa-bullseye', 'status': 'Primary Focus', 'focus': 'Flutter framework application state & widgets', 'color_class': 'tech-dart'},
            {'name': 'Python (Basic)', 'icon': 'fa-brands fa-python', 'status': 'Basic Knowledge', 'focus': 'Scripting, backend logic, data fundamentals', 'color_class': 'tech-python'},
            {'name': 'Java', 'icon': 'fa-brands fa-java', 'status': 'Core Language', 'focus': 'OOP fundamentals, Android development', 'color_class': 'tech-java'},
            {'name': 'Kotlin', 'icon': 'fa-solid fa-terminal', 'status': 'Android Development', 'focus': 'Native Android practicals & UI', 'color_class': 'tech-kotlin'},
        ]
    },
    'web_development': {
        'category_name': 'Web Technologies & Frameworks',
        'category_icon': 'fa-solid fa-globe',
        'description': 'Technologies for crafting responsive frontend and backend systems.',
        'items': [
            {'name': 'HTML5', 'icon': 'fa-brands fa-html5', 'status': 'Markup Standard', 'focus': 'Semantic page structure & accessible DOM', 'color_class': 'tech-html'},
            {'name': 'CSS3', 'icon': 'fa-brands fa-css3-alt', 'status': 'Styling & Layout', 'focus': 'Responsive flexbox/grid, animations & themes', 'color_class': 'tech-css'},
            {'name': 'JavaScript (Basic)', 'icon': 'fa-brands fa-js', 'status': 'Basic Knowledge', 'focus': 'DOM manipulation, dynamic interactions & events', 'color_class': 'tech-js'},
            {'name': 'Bootstrap', 'icon': 'fa-brands fa-bootstrap', 'status': 'CSS Framework', 'focus': 'Mobile-first components & responsive utilities', 'color_class': 'tech-bootstrap'},
            {'name': 'Django (Basic)', 'icon': 'fa-solid fa-layer-group', 'status': 'Basic Knowledge', 'focus': 'MVT architecture, ORM, routing & security', 'color_class': 'tech-django'},
        ]
    },
    'database_and_tools': {
        'category_name': 'Database Technologies & Tools',
        'category_icon': 'fa-solid fa-database',
        'description': 'Relational databases, cloud services, and developer tooling.',
        'items': [
            {'name': 'MySQL', 'icon': 'fa-solid fa-database', 'status': 'Relational DB', 'focus': 'Relational schemas, SQL queries, indexing', 'color_class': 'tech-mysql'},
            {'name': 'SQLite', 'icon': 'fa-solid fa-server', 'status': 'Embedded DB', 'focus': 'Lightweight development storage, Android local DB', 'color_class': 'tech-sqlite'},
            {'name': 'Firebase (Basic)', 'icon': 'fa-solid fa-fire', 'status': 'Basic Knowledge', 'focus': 'Cloud storage, real-time database, auth', 'color_class': 'tech-firebase'},
            {'name': 'Git & GitHub', 'icon': 'fa-brands fa-github', 'status': 'Version Control', 'focus': 'Repository management & commit workflows', 'color_class': 'tech-git'},
            {'name': 'XAMPP', 'icon': 'fa-solid fa-server', 'status': 'Local Server', 'focus': 'Apache & MySQL local testing environment', 'color_class': 'tech-xampp'},
        ]
    }
}

PROJECTS_DATA = [
    {
        'slug': 'retiyamarket',
        'title': 'RetiyaMarket – Flutter Mobile Application',
        'description': 'A mobile marketplace project focused on buying and selling products.',
        'full_overview': (
            'Developed a mobile marketplace project focused on buying and selling products. '
            'Worked on a user-friendly mobile interface for a student marketplace. '
            'Planned marketplace features such as product listings, user authentication, wishlist, chat, and order management.'
        ),
        'category': 'Mobile Application',
        'tags': ['Flutter', 'Dart', 'MySQL'],
        'status': 'Mobile Project',
        'icon': 'fa-solid fa-cart-shopping',
        'art_class': 'art-retiyamarket',
        'accent_color': '#38bdf8',
        'github_url': None,
        'demo_url': None,
    },
    {
        'slug': 'veloria',
        'title': 'VELORIA – Fashion E-Commerce Website',
        'description': 'A fashion e-commerce website project focused on product presentation and shopping UI.',
        'full_overview': (
            'Created a fashion e-commerce website project with a modern shopping interface. '
            'Worked on product categories and the design of a responsive shopping experience. '
            'Explored features such as user authentication, shopping cart, and wishlist.'
        ),
        'category': 'Web Application',
        'tags': ['Python', 'Django', 'HTML', 'CSS', 'Bootstrap', 'JavaScript'],
        'status': 'Web Project',
        'icon': 'fa-solid fa-bag-shopping',
        'art_class': 'art-veloria',
        'accent_color': '#ec4899',
        'github_url': None,
        'demo_url': None,
    },
    {
        'slug': 'gamezone',
        'title': 'GameZone – Gaming Platform',
        'description': 'A gaming platform concept for browsing and playing games.',
        'full_overview': (
            'GameZone explores a modern interactive web hub for casual browser games. '
            'The design features game genre filtering, leaderboard cards, game showcase tiles, '
            'and responsive media components.'
        ),
        'category': 'Web Platform Concept',
        'tags': ['JavaScript', 'HTML5', 'CSS3'],
        'status': 'Platform Concept',
        'icon': 'fa-solid fa-gamepad',
        'art_class': 'art-gamezone',
        'accent_color': '#8b5cf6',
        'github_url': None,
        'demo_url': None,
    },
    {
        'slug': 'animal-classification',
        'title': 'Animal Classification – Machine Learning Project',
        'description': 'An animal-classification machine learning project.',
        'full_overview': (
            'An academic exploration of image classification using Python. '
            'Focuses on dataset preparation, image preprocessing, feature extraction, '
            'and evaluating model accuracy across distinct animal categories.'
        ),
        'category': 'Machine Learning',
        'tags': ['Python', 'Machine Learning', 'Data Preprocessing', 'Image Classification'],
        'status': 'ML Practical / Study',
        'icon': 'fa-solid fa-paw',
        'art_class': 'art-animal',
        'accent_color': '#10b981',
        'github_url': None,
        'demo_url': None,
    },
    {
        'slug': 'android-student-storage',
        'title': 'Android Student Data Storage – Android Practical',
        'description': 'An Android learning project related to student data storage.',
        'full_overview': (
            'An Android Studio practical coursework project focused on persistent local data handling. '
            'Demonstrates SQLite database helper operations, record insertion, querying, and updating '
            'student records on Android devices.'
        ),
        'category': 'Mobile Practical',
        'tags': ['Android Studio', 'Java / Kotlin', 'SQLite', 'Android SDK'],
        'status': 'Coursework Practical',
        'icon': 'fa-solid fa-mobile-screen-button',
        'art_class': 'art-android-storage',
        'accent_color': '#f59e0b',
        'github_url': None,
        'demo_url': None,
    },
]
