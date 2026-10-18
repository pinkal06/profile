"""
Django Admin Configuration for Pinkal Rathod Personal Portfolio.
Provides a secure, beginner-friendly administration dashboard for:
- SiteProfile (Owner profile & contact details)
- Education (Academic records & qualifications)
- Skill (Technical competencies)
- Project (Coursework practicals & application projects)
- Certificate (Credentials & achievements)
- Experience (Fresher & career readiness records)
- SocialLink (Verified external links)
- ContactMessage (Inquiries received from Phase 6 contact form - staff only)
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteProfile,
    Education,
    Skill,
    Project,
    Certificate,
    Experience,
    SocialLink,
    ContactMessage,
)

# Admin Interface Customization
admin.site.site_header = "Pinkal Rathod — Portfolio Administration"
admin.site.site_title = "Pinkal Rathod Admin Portal"
admin.site.index_title = "Portfolio Content Management & Database Dashboard"


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'professional_title', 'location', 'phone', 'personal_email', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'professional_title', 'personal_email', 'academic_email', 'location')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Profile Identity', {
            'fields': ('name', 'professional_title', 'is_active')
        }),
        ('Verified Contact Details', {
            'fields': ('location', 'phone', 'personal_email', 'academic_email')
        }),
        ('Biographies & Introductions', {
            'fields': (
                'short_intro',
                'biography',
                'bio_intro',
                'bio_programming',
                'bio_web_mobile',
                'bio_database_ml',
            ),
            'classes': ('collapse',),
            'description': 'Modular narrative sections used across Hero and About Me pages.'
        }),
        ('Resume Presentation Statements', {
            'fields': ('professional_summary', 'career_objective'),
            'description': 'Used in public resume web page and dynamic PDF export.'
        }),
        ('Media & Files', {
            'fields': ('profile_image', 'resume_file'),
            'description': 'Optional custom uploads. Leave blank to use default static photo and dynamic PDF.'
        }),
        ('Audit Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'degree', 
        'institution', 
        'qualification_type', 
        'study_period', 
        'score_display_col', 
        'display_order', 
        'is_published'
    )
    list_filter = ('qualification_type', 'is_published', 'start_year', 'passing_year')
    search_fields = ('degree', 'institution', 'department', 'description')
    list_editable = ('display_order', 'is_published')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('display_order', '-created_at')

    fieldsets = (
        ('Academic Institution & Qualification', {
            'fields': ('institution', 'degree', 'department', 'qualification_type')
        }),
        ('Timing & Period', {
            'fields': ('study_period', 'start_year', 'end_year', 'passing_year', 'semester')
        }),
        ('Verified Scores & Performance', {
            'fields': ('cgpa', 'percentage', 'percentile_rank'),
            'description': 'Input authentic numbers without symbols (e.g. 7.73, 63.38, 78.35).'
        }),
        ('Details & Publication', {
            'fields': ('description', 'display_order', 'is_published')
        }),
        ('System Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Academic Score')
    def score_display_col(self, obj):
        return obj.score_display or "—"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency_label', 'display_order', 'is_published', 'icon_preview')
    list_filter = ('category', 'is_published')
    search_fields = ('name', 'description', 'proficiency_label')
    list_editable = ('display_order', 'is_published', 'proficiency_label')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('category', 'display_order', 'name')

    fieldsets = (
        ('Skill Details', {
            'fields': ('name', 'category', 'proficiency_label', 'description')
        }),
        ('Visual Styling', {
            'fields': ('icon_class', 'color_class'),
            'description': 'Font Awesome icon class (e.g. fa-brands fa-flutter) and CSS tag class.'
        }),
        ('Visibility & Ordering', {
            'fields': ('display_order', 'is_published')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Icon')
    def icon_preview(self, obj):
        if obj.icon_class:
            return format_html('<i class="{}" style="font-size: 1.2rem;"></i>', obj.icon_class)
        return "—"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'category', 
        'status', 
        'is_featured', 
        'is_published', 
        'display_order', 
        'has_github_col', 
        'has_demo_col'
    )
    list_filter = ('status', 'category', 'is_featured', 'is_published')
    search_fields = ('title', 'short_description', 'detailed_description', 'technologies')
    list_editable = ('status', 'is_featured', 'is_published', 'display_order')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('display_order', '-created_at')

    fieldsets = (
        ('Project Core Information', {
            'fields': ('title', 'slug', 'category', 'status', 'technologies')
        }),
        ('Descriptions & Overview', {
            'fields': ('short_description', 'detailed_description'),
            'description': 'Short description is shown on project cards; detailed description on modal/detail view.'
        }),
        ('Visual Artwork & Media', {
            'fields': ('image', 'icon', 'art_class', 'accent_color'),
            'description': 'Artwork classes map to responsive CSS cards (e.g. art-retiyamarket, art-veloria).'
        }),
        ('Repository & Live Demo Links', {
            'fields': ('github_url', 'live_demo_url'),
            'description': 'Strictly optional. Leave blank if in development or not deployed.'
        }),
        ('Publishing Controls', {
            'fields': ('display_order', 'is_featured', 'is_published')
        }),
        ('Audit Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(boolean=True, description='GitHub')
    def has_github_col(self, obj):
        return bool(obj.github_url)

    @admin.display(boolean=True, description='Live Demo')
    def has_demo_col(self, obj):
        return bool(obj.live_demo_url)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date', 'display_order', 'is_published')
    list_filter = ('is_published', 'issue_date')
    search_fields = ('title', 'issuing_organization', 'credential_id', 'description')
    list_editable = ('display_order', 'is_published')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('display_order', '-issue_date', '-created_at')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'employment_type', 'is_current', 'display_order', 'is_published')
    list_filter = ('employment_type', 'is_current', 'is_published')
    search_fields = ('role', 'organization', 'description')
    list_editable = ('display_order', 'is_published')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('display_order', '-created_at')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'label', 'url', 'display_order', 'is_active')
    list_filter = ('platform', 'is_active')
    search_fields = ('label', 'url')
    list_editable = ('display_order', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('display_order', 'id')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Staff-only inbox for inquiries submitted through the future Phase 6 contact form.
    Message content and sender info are READ-ONLY to ensure record authenticity.
    Only `is_read` status can be toggled by staff.
    """
    list_display = ('subject', 'name', 'email', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Message Status', {
            'fields': ('is_read', 'created_at')
        }),
        ('Sender Information (Read-Only)', {
            'fields': ('name', 'email')
        }),
        ('Inquiry Content (Read-Only)', {
            'fields': ('subject', 'message')
        }),
    )

    def has_add_permission(self, request):
        # Prevent manual creation of fake messages in the admin
        return False

    actions = ['mark_as_read', 'mark_as_unread']

    @admin.action(description="Mark selected messages as Read")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Mark selected messages as Unread")
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
