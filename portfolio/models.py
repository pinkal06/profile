"""
Portfolio Database Models for Pinkal Rathod Personal Portfolio.
Defines structured, secure, and maintainable Django ORM models for:
- SiteProfile: Primary owner information (single active profile)
- Education: Verified academic qualifications and records
- Skill: Technical competencies categorized by domain
- Project: Coursework practicals and application projects
- Certificate: Academic/professional certifications (empty initially)
- Experience: Verified role/experience status (fresher focus)
- SocialLink: External verified profiles and links
- ContactMessage: Storage for incoming messages (staff admin only)
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify


class SiteProfile(models.Model):
    """
    Stores primary profile information for Pinkal Rathod.
    Enforces a single active primary profile at any given time.
    """
    name = models.CharField(max_length=120, default='Pinkal Rathod')
    professional_title = models.CharField(
        max_length=200, 
        default='ASPIRING FLUTTER DEVELOPER | BCA STUDENT'
    )
    location = models.CharField(max_length=150, default='Ahmedabad, Gujarat, India')
    phone = models.CharField(max_length=30, default='7861040487')
    personal_email = models.EmailField(default='pinkalrathod2007@gmail.com')
    academic_email = models.EmailField(default='240130510053.cs@gujaratvidyapith.org')
    
    biography = models.TextField(
        blank=True,
        help_text="Primary comprehensive biography narrative."
    )
    short_intro = models.TextField(
        blank=True,
        help_text="Brief tagline or hero statement."
    )
    bio_intro = models.TextField(blank=True, help_text="Greeting and academic context.")
    bio_programming = models.TextField(blank=True, help_text="Programming languages focus.")
    bio_web_mobile = models.TextField(blank=True, help_text="Mobile & Web engineering focus.")
    bio_database_ml = models.TextField(blank=True, help_text="Database and ML coursework focus.")

    career_objective = models.TextField(
        blank=True,
        help_text="Career goal statement for resume and public showcase."
    )
    professional_summary = models.TextField(
        blank=True,
        help_text="Executive summary for resume presentation."
    )

    profile_image = models.ImageField(
        upload_to='profile/', 
        blank=True, 
        null=True,
        help_text="Uploaded profile photo (falls back to static image if blank)."
    )
    resume_file = models.FileField(
        upload_to='resumes/', 
        blank=True, 
        null=True,
        help_text="Optional custom static resume PDF. If not uploaded, dynamic ReportLab generation is used."
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Designates this as the active public portfolio profile."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Site Profile'
        verbose_name_plural = 'Site Profiles'

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"{self.name} — {self.professional_title} [{status}]"

    def save(self, *args, **kwargs):
        """Ensure only one profile is active at a time."""
        if self.is_active:
            # Set all other profiles to inactive
            SiteProfile.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)


class Education(models.Model):
    """
    Stores verified academic qualifications.
    Supports decimal CGPA, percentage, and percentile rankings without empty claims.
    """
    QUALIFICATION_TYPES = [
        ('bca', 'Undergraduate Degree (BCA)'),
        ('12th', 'Higher Secondary (12th Science)'),
        ('10th', 'Secondary School (10th SSC)'),
        ('other', 'Other Qualification'),
    ]

    institution = models.CharField(max_length=200, help_text="Name of the university, college, or board.")
    degree = models.CharField(max_length=200, help_text="Degree or certificate name (e.g. BCA, 12th Science).")
    department = models.CharField(max_length=150, blank=True, help_text="e.g. Computer Science, Science Stream.")
    qualification_type = models.CharField(
        max_length=50, 
        choices=QUALIFICATION_TYPES, 
        default='bca'
    )
    study_period = models.CharField(
        max_length=100, 
        help_text="e.g. '2025 – Present' or 'Passing Year: 2024'"
    )
    start_year = models.PositiveIntegerField(blank=True, null=True)
    end_year = models.PositiveIntegerField(blank=True, null=True)
    passing_year = models.PositiveIntegerField(blank=True, null=True)
    semester = models.CharField(blank=True, max_length=50, help_text="Current semester note, e.g. 'Semester 4'")
    
    # Numeric performance fields with exact decimal precision
    cgpa = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        blank=True, 
        null=True,
        help_text="Grade point average (e.g. 7.73)"
    )
    percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        blank=True, 
        null=True,
        help_text="Score percentage (e.g. 63.38 or 69.50)"
    )
    percentile_rank = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        blank=True, 
        null=True,
        help_text="Percentile rank (e.g. 78.35)"
    )

    description = models.TextField(blank=True, help_text="Educational focus or notable coursework.")
    display_order = models.PositiveIntegerField(default=0, help_text="Display order on the page (lower appears first).")
    is_published = models.BooleanField(default=True, help_text="Set to False to hide this record from public pages.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Education Record'
        verbose_name_plural = 'Education Records'
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f"{self.degree} — {self.institution} ({self.study_period})"

    @property
    def score_display(self):
        """Returns human-readable verified academic score string."""
        if self.cgpa:
            sem = f" ({self.semester})" if self.semester else " (after Sem 4)"
            return f"CGPA: {self.cgpa}{sem}"
        if self.percentage and self.percentile_rank:
            return f"{self.percentage}% (PR: {self.percentile_rank})"
        if self.percentage:
            return f"{self.percentage}%"
        return ""

    @property
    def period(self):
        return self.study_period

    @property
    def status(self):
        if self.qualification_type == 'bca' or not self.passing_year:
            return 'Currently Pursuing'
        return 'Completed'

    @property
    def icon(self):
        if self.qualification_type == 'bca':
            return 'fa-solid fa-graduation-cap'
        elif self.qualification_type == '12th':
            return 'fa-solid fa-school'
        return 'fa-solid fa-award'

    @property
    def marks(self):
        return self.score_display



class Skill(models.Model):
    """
    Stores technical skills categorized by functional domain.
    Editable in Django Admin without fabricated proficiency percentages.
    """
    CATEGORY_CHOICES = [
        ('Programming Languages', 'Programming Languages'),
        ('Web Development', 'Web Development'),
        ('Mobile Development', 'Mobile Development'),
        ('Backend Framework', 'Backend Framework'),
        ('Database Technologies', 'Database Technologies'),
        ('Tools', 'Tools & Tooling'),
    ]

    name = models.CharField(max_length=100, help_text="e.g. Flutter, Dart, Python, Django, MySQL")
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES)
    description = models.CharField(
        max_length=255, 
        blank=True, 
        help_text="Brief practical application note (e.g. 'Widget trees, reactive UI')."
    )
    proficiency_label = models.CharField(
        max_length=60, 
        blank=True, 
        help_text="Verified status badge (e.g. 'Core Focus', 'Primary Focus', 'Basic Knowledge')."
    )
    icon_class = models.CharField(
        max_length=80, 
        blank=True, 
        default='fa-solid fa-code', 
        help_text="Font Awesome icon class (e.g. 'fa-brands fa-flutter')."
    )
    color_class = models.CharField(
        max_length=50, 
        blank=True, 
        default='tech-python', 
        help_text="CSS badge styling class (e.g. 'tech-flutter', 'tech-django')."
    )
    display_order = models.PositiveIntegerField(default=0, help_text="Display order within category.")
    is_published = models.BooleanField(default=True, help_text="Uncheck to hide from public view.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['category', 'display_order', 'name']

    def __str__(self):
        return f"{self.name} [{self.category}]"

    @property
    def icon(self):
        return self.icon_class

    @property
    def focus(self):
        return self.description

    @property
    def status(self):
        return self.proficiency_label


class Project(models.Model):
    """
    Stores coursework, application prototypes, and practical software projects.
    Distinguishes planned vs in-progress vs completed status without exaggeration.
    """
    STATUS_CHOICES = [
        ('planned', 'Planned / Concept'),
        ('in_progress', 'In Progress / Coursework'),
        ('completed', 'Completed'),
    ]

    CATEGORY_CHOICES = [
        ('Mobile Application', 'Mobile Application'),
        ('Web Application', 'Web Application'),
        ('Web Platform Concept', 'Web Platform Concept'),
        ('Machine Learning', 'Machine Learning'),
        ('Mobile Practical', 'Mobile Practical'),
    ]

    title = models.CharField(max_length=200, help_text="Full project title.")
    slug = models.SlugField(max_length=220, unique=True, help_text="URL-friendly identifier.")
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES, default='Web Application')
    short_description = models.TextField(help_text="Concise 1-2 sentence card summary.")
    detailed_description = models.TextField(blank=True, help_text="Comprehensive overview of architecture & features.")
    
    technologies = models.CharField(
        max_length=255, 
        help_text="Comma-separated technologies (e.g. 'Flutter, Dart, MySQL')."
    )
    status = models.CharField(
        max_length=30, 
        choices=STATUS_CHOICES, 
        default='in_progress',
        help_text="Current development stage. Never mark as completed without verified evidence."
    )
    
    # Visual and styling fields
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    icon = models.CharField(max_length=60, default='fa-solid fa-laptop-code')
    art_class = models.CharField(max_length=60, blank=True, default='art-default')
    accent_color = models.CharField(max_length=30, blank=True, default='#4F7CFF')

    # External links (strictly optional - no fake links)
    github_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Leave blank if repository is private or in active coursework."
    )
    live_demo_url = models.URLField(
        blank=True, 
        null=True, 
        help_text="Leave blank if live deployment is not active."
    )

    display_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False, help_text="Highlight on homepage preview.")
    is_published = models.BooleanField(default=True, help_text="Uncheck to keep project private in drafts.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def tags_list(self):
        """Returns list of trimmed technology strings."""
        if not self.technologies:
            return []
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    @property
    def tags(self):
        return self.tags_list

    @property
    def description(self):
        return self.short_description

    @property
    def demo_url(self):
        return self.live_demo_url


class Certificate(models.Model):
    """
    Stores certificates and credentials.
    Allowed to remain empty until authentic certificates are earned and uploaded.
    """
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=150, blank=True)
    credential_url = models.URLField(blank=True, null=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
        ordering = ['display_order', '-issue_date', '-created_at']

    def __str__(self):
        return f"{self.title} — {self.issuing_organization}"


class Experience(models.Model):
    """
    Stores verified work or internship experience.
    Strictly documents fresher status seeking Flutter opportunities without fabricated employers.
    """
    EMPLOYMENT_TYPES = [
        ('fresher', 'Fresher / Entry-Level'),
        ('internship', 'Internship'),
        ('academic', 'Academic / Coursework Project'),
        ('full_time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]

    role = models.CharField(max_length=150, default='Fresher | Flutter Mobile App Development')
    organization = models.CharField(max_length=150, blank=True, help_text="Company or institution (leave blank if fresher).")
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES, default='fresher')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(help_text="Detailed responsibilities or career readiness description.")
    is_current = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Experience Record'
        verbose_name_plural = 'Experience Records'
        ordering = ['display_order', '-created_at']

    def __str__(self):
        org = f" at {self.organization}" if self.organization else ""
        return f"{self.role}{org}"


class SocialLink(models.Model):
    """
    Stores external social profile URLs and contact destinations.
    Validates URL format; keeps unconfigured links inactive.
    """
    PLATFORM_CHOICES = [
        ('LinkedIn', 'LinkedIn'),
        ('GitHub', 'GitHub'),
        ('Email', 'Email'),
        ('Portfolio', 'Portfolio Website'),
        ('Other', 'Other Platform'),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, default='LinkedIn')
    label = models.CharField(max_length=100, help_text="e.g. 'Pinkal Rathod on LinkedIn'")
    url = models.CharField(
        max_length=300, 
        help_text="Destination web URL (https://...) or email link (mailto:...)"
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Social Link'
        verbose_name_plural = 'Social Links'
        ordering = ['display_order', 'id']

    def clean(self):
        if self.url and not (self.url.startswith('http://') or self.url.startswith('https://') or self.url.startswith('mailto:')):
            raise ValidationError({'url': 'URL must begin with https://, http://, or mailto:'})

    def __str__(self):
        return f"{self.platform}: {self.label}"


class ContactMessage(models.Model):
    """
    Stores contact form submissions (ready for Phase 6).
    Messages are private and visible exclusively to staff in Django Admin.
    NEVER exposed on public endpoints.
    """
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False, help_text="Mark if an administrator has reviewed this inquiry.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages (Admin Only)'
        ordering = ['-created_at']

    def __str__(self):
        read_badge = "Read" if self.is_read else "NEW"
        return f"[{read_badge}] {self.subject} — {self.name} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"
