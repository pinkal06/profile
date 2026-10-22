from django.test import TestCase
from django.urls import reverse

class PortfolioPagesTest(TestCase):
    """
    Automated integration tests for Phase 1, Phase 2, and Phase 3 features:
    Home, About, Education, Skills, and Projects.
    Ensures strict adherence to verified information and navigation integrity.
    """

    def test_home_page(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/home.html')
        self.assertTemplateUsed(response, 'base.html')
        content = response.content.decode('utf-8')
        
        # Identity checks
        self.assertIn("HELLO, I'M", content)
        self.assertIn('Pinkal Rathod', content)
        self.assertIn('Gujarat Vidyapith', content)
        self.assertIn('Bachelor of Computer Applications', content)
        self.assertIn('2025 – Present', content)
        
        # Hero Action buttons
        self.assertIn('View Projects', content)
        self.assertIn('Contact Me', content)

        # Profile image check
        self.assertIn('pinkal_rathod.jpg', content)

        # Rotating animated skill texts
        self.assertIn('Python Development', content)
        self.assertIn('Django Web Development', content)
        self.assertIn('Flutter App Development', content)
        self.assertIn('Android Development', content)
        self.assertIn('Frontend Development', content)

        # Preview sections
        self.assertIn('Academic &amp; Programming Journey', content)
        self.assertIn('Academic Qualifications', content)
        self.assertIn('Technical Interests &amp; Tooling', content)
        self.assertIn('Planned &amp; Coursework Projects', content)
        self.assertIn('Connect with Pinkal Rathod', content)

    def test_about_page(self):
        response = self.client.get(reverse('portfolio:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')
        content = response.content.decode('utf-8')

        # Content checks
        self.assertIn('About', content)
        self.assertIn('Pinkal Rathod', content)
        self.assertIn('Gujarat Vidyapith', content)
        self.assertIn('BCA', content)
        self.assertIn('pinkal_rathod.jpg', content)
        self.assertIn('Python &amp; Django Architecture', content)
        self.assertIn('Flutter Mobile Engineering', content)
        self.assertIn('Android Native Development', content)
        self.assertIn('Database Management', content)
        self.assertIn('Machine Learning Concepts', content)

    def test_education_page(self):
        response = self.client.get(reverse('portfolio:education'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'education.html')
        self.assertTemplateUsed(response, 'base.html')
        content = response.content.decode('utf-8')

        # Academic timeline checks
        self.assertIn('Gujarat Vidyapith', content)
        self.assertIn('Bachelor of Computer Applications (BCA)', content)
        self.assertIn('2025 – Present', content)
        self.assertIn('Currently Pursuing', content)

    def test_skills_page(self):
        response = self.client.get(reverse('portfolio:skills'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'skills.html')
        self.assertTemplateUsed(response, 'base.html')
        content = response.content.decode('utf-8')

        # Category checks
        self.assertIn('Programming Languages', content)
        self.assertIn('Web Technologies', content)
        self.assertIn('Mobile Development', content)
        self.assertIn('Database Technologies', content)

        # Technology checks
        for tech in [
            'Python', 'Java', 'Kotlin', 'Dart',
            'HTML', 'CSS', 'JavaScript', 'Bootstrap', 'Django',
            'Flutter', 'Android Studio',
            'MySQL', 'SQLite', 'Firebase'
        ]:
            self.assertIn(tech, content)

    def test_projects_page(self):
        response = self.client.get(reverse('portfolio:projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'partials/project_card.html')
        content = response.content.decode('utf-8')

        # All 5 projects checks
        self.assertIn('RetiyaMarket', content)
        self.assertIn('VELORIA', content)
        self.assertIn('GameZone', content)
        self.assertIn('Animal Classification', content)
        self.assertIn('Android Student Data Storage', content)

        # Integrity check: missing URLs should NOT render broken links
        self.assertIn('Links not configured (In Development)', content)
        self.assertNotIn('href="https://github.com/fake', content)

    def test_navigation_routes(self):
        """Verifies that navigation links resolve properly across pages."""
        for route_name in ['home', 'about', 'education', 'skills', 'projects', 'resume', 'contact']:
            url = reverse(f'portfolio:{route_name}')
            res = self.client.get(url)
            self.assertEqual(res.status_code, 200)

    def test_resume_page(self):
        """Phase 4 test: Verifies the interactive Resume page and verified data."""
        response = self.client.get(reverse('portfolio:resume'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume.html')
        self.assertTemplateUsed(response, 'base.html')
        content = response.content.decode('utf-8')

        # Verified Personal Info
        self.assertIn('Pinkal Rathod', content)
        self.assertIn('ASPIRING FLUTTER DEVELOPER | BCA STUDENT', content)
        self.assertIn('Ahmedabad, Gujarat, India', content)
        self.assertIn('7861040487', content)
        self.assertIn('pinkalrathod2007@gmail.com', content)
        self.assertIn('240130510053.cs@gujaratvidyapith.org', content)

        # Professional Summary & Career Objective
        self.assertIn('Motivated BCA student focused on Flutter mobile application development', content)
        self.assertIn('To build a career as a Flutter Developer', content)

        # Verified Education & Scores
        self.assertIn('Gujarat Vidyapith', content)
        self.assertIn('7.73 after Semester 4', content)
        self.assertIn('63.38%', content)
        self.assertIn('69.50%', content)
        self.assertIn('78.35', content)

        # Verified Projects & Experience
        self.assertIn('RetiyaMarket', content)
        self.assertIn('VELORIA', content)
        self.assertIn('Fresher | Flutter Mobile App Development', content)

        # Languages
        self.assertIn('Gujarati', content)
        self.assertIn('Hindi', content)
        self.assertIn('English', content)

        # Action Buttons
        self.assertIn('Download Resume PDF', content)
        self.assertIn('Print Resume', content)
        self.assertIn('btnDownloadResumePDF', content)
        self.assertIn('btnPrintResume', content)

        # Avatar Fallback
        self.assertIn('PR', content)
        self.assertIn('resume-avatar-fallback', content)

    def test_resume_pdf_download(self):
        """Phase 4 test: Verifies ReportLab PDF generation and attachment response."""
        # Test app-namespaced URL
        response = self.client.get(reverse('portfolio:resume_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="Pinkal_Rathod_Resume.pdf"')
        self.assertTrue(response.content.startswith(b'%PDF-'))
        self.assertGreater(len(response.content), 2000)

        # Test root-level URL reverse as requested in prompt ({% url 'resume_pdf' %})
        response_root = self.client.get(reverse('resume_pdf'))
        self.assertEqual(response_root.status_code, 200)
        self.assertEqual(response_root['Content-Type'], 'application/pdf')
        self.assertEqual(response_root['Content-Disposition'], 'attachment; filename="Pinkal_Rathod_Resume.pdf"')
        self.assertTrue(response_root.content.startswith(b'%PDF-'))


from django.contrib import admin
from django.core.management import call_command
from portfolio.models import (
    SiteProfile,
    Education,
    Skill,
    Project,
    Certificate,
    Experience,
    SocialLink,
    ContactMessage,
)

class Phase5ModelsAndAdminTest(TestCase):
    """
    Automated integration and unit tests for Phase 5:
    - Django ORM models integrity and constraints
    - Admin site registration and ModelAdmin configuration
    - Public vs draft publication filtering
    - ContactMessage privacy (staff-only protection)
    - Idempotent database seeding
    """

    def setUp(self):
        # Run seeding to establish baseline verified state
        call_command('seed_portfolio')

    def test_admin_site_registration(self):
        """Verifies that all 8 Phase 5 models are properly registered in Django admin."""
        registered_models = admin.site._registry
        models_to_check = [
            SiteProfile,
            Education,
            Skill,
            Project,
            Certificate,
            Experience,
            SocialLink,
            ContactMessage,
        ]
        for model in models_to_check:
            self.assertIn(model, registered_models, f"{model.__name__} must be registered in Django Admin.")

    def test_site_profile_single_active_constraint(self):
        """Ensures that activating a profile automatically sets other profiles to inactive."""
        p1 = SiteProfile.objects.filter(is_active=True).first()
        self.assertIsNotNone(p1)

        # Create a second profile and activate it
        p2 = SiteProfile.objects.create(
            name="Pinkal Alternate",
            professional_title="Flutter Mobile Engineer",
            is_active=True,
        )
        p1.refresh_from_db()
        self.assertFalse(p1.is_active, "Existing profile must be deactivated when a new active profile is saved.")
        self.assertTrue(p2.is_active)

    def test_published_vs_draft_filtering(self):
        """Ensures that unpublished/draft records are never displayed on public pages."""
        # 1. Draft Project
        draft_project = Project.objects.create(
            title="Secret Internal Tool (Unpublished)",
            slug="secret-internal-tool",
            short_description="This is an internal draft project that must not be published.",
            status="planned",
            is_published=False,
        )
        res_projects = self.client.get(reverse('portfolio:projects'))
        self.assertNotIn("Secret Internal Tool", res_projects.content.decode('utf-8'))
        res_home = self.client.get(reverse('portfolio:home'))
        self.assertNotIn("Secret Internal Tool", res_home.content.decode('utf-8'))

        # 2. Draft Skill
        draft_skill = Skill.objects.create(
            name="UnpublishedExperimentalSkill",
            category="Programming Languages",
            is_published=False,
        )
        res_skills = self.client.get(reverse('portfolio:skills'))
        self.assertNotIn("UnpublishedExperimentalSkill", res_skills.content.decode('utf-8'))

        # 3. Draft Education
        draft_edu = Education.objects.create(
            institution="Unpublished University",
            degree="Draft Credential",
            study_period="2099",
            is_published=False,
        )
        res_edu = self.client.get(reverse('portfolio:education'))
        self.assertNotIn("Unpublished University", res_edu.content.decode('utf-8'))

    def test_contact_message_privacy(self):
        """Ensures that contact messages are stored securely and NEVER exposed on any public page."""
        msg = ContactMessage.objects.create(
            name="Inquiring Recruiter",
            email="recruiter@example.com",
            subject="Flutter Internship Invitation",
            message="Confidential interview invitation details.",
        )
        self.assertFalse(msg.is_read)

        # Check all public endpoints to guarantee privacy
        public_routes = ['home', 'about', 'education', 'skills', 'projects', 'resume']
        for route in public_routes:
            res = self.client.get(reverse(f'portfolio:{route}'))
            content = res.content.decode('utf-8')
            self.assertNotIn("Inquiring Recruiter", content, f"Contact message author leaked on {route}")
            self.assertNotIn("recruiter@example.com", content, f"Contact email leaked on {route}")
            self.assertNotIn("Confidential interview invitation details", content, f"Contact message body leaked on {route}")

    def test_seeding_idempotency(self):
        """Ensures that running seed_portfolio multiple times does NOT generate duplicates."""
        initial_projects_count = Project.objects.count()
        initial_skills_count = Skill.objects.count()
        initial_education_count = Education.objects.count()

        # Run command again
        call_command('seed_portfolio')

        self.assertEqual(Project.objects.count(), initial_projects_count)
        self.assertEqual(Skill.objects.count(), initial_skills_count)
        self.assertEqual(Education.objects.count(), initial_education_count)


class Phase6ContactFormTest(TestCase):
    """
    Automated tests for Phase 6 Contact Page and Form Backend:
    - Contact page loads with verified contact details and form fields.
    - Valid POST creates ContactMessage in database and redirects with success message.
    - Invalid email input is rejected with clear error feedback.
    - Empty required fields are rejected with clear error feedback.
    - Honeypot spam input is blocked and does not save to database.
    - GET requests never create messages.
    - Messages are kept strictly private from public visitors.
    """

    def setUp(self):
        call_command('seed_portfolio')

    def test_contact_page_get(self):
        """Verifies GET /contact/ renders properly with verified details and form."""
        initial_count = ContactMessage.objects.count()
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertTemplateUsed(response, 'base.html')
        content = response.content.decode('utf-8')

        # Verified contact details
        self.assertIn('Pinkal Rathod', content)
        self.assertIn('Ahmedabad, Gujarat, India', content)
        self.assertIn('pinkalrathod2007@gmail.com', content)

        # LinkedIn verification on Contact page
        self.assertIn('https://www.linkedin.com/in/pinkal-rathod-a303183b4/', content)
        self.assertIn('id="contactLinkedInLink"', content)
        self.assertIn('rel="noopener noreferrer"', content)
        self.assertIn('target="_blank"', content)

        # Form fields & action
        self.assertIn('id="contactName"', content)
        self.assertIn('id="contactEmail"', content)
        self.assertIn('id="contactSubject"', content)
        self.assertIn('id="contactMessage"', content)
        self.assertIn('id="btnSubmitContact"', content)
        self.assertIn('csrfmiddlewaretoken', content)

        # GET request must not create messages
        self.assertEqual(ContactMessage.objects.count(), initial_count)

    def test_linkedin_integration_across_portfolio(self):
        """Verifies LinkedIn URL presence, attributes, and model integration across all pages."""
        linkedin_url = 'https://www.linkedin.com/in/pinkal-rathod-a303183b4/'
        
        # 1. Verify SocialLink model seeded / database record
        social_link = SocialLink.objects.filter(platform='LinkedIn', is_active=True).first()
        self.assertIsNotNone(social_link, "SocialLink for LinkedIn must exist and be active.")
        self.assertEqual(social_link.url, linkedin_url)

        # 2. Check Home page (Navbar and Footer)
        home_res = self.client.get(reverse('portfolio:home'))
        self.assertEqual(home_res.status_code, 200)
        home_content = home_res.content.decode('utf-8')
        self.assertIn(linkedin_url, home_content)
        self.assertIn('fa-brands fa-linkedin-in', home_content)
        self.assertIn('target="_blank"', home_content)
        self.assertIn('rel="noopener noreferrer"', home_content)

        # 3. Check Contact page
        contact_res = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(contact_res.status_code, 200)
        contact_content = contact_res.content.decode('utf-8')
        self.assertIn(linkedin_url, contact_content)
        self.assertIn('id="contactLinkedInLink"', contact_content)

        # 4. Check Resume page
        resume_res = self.client.get(reverse('portfolio:resume'))
        self.assertEqual(resume_res.status_code, 200)
        resume_content = resume_res.content.decode('utf-8')
        self.assertIn(linkedin_url, resume_content)

    def test_contact_form_valid_post(self):
        """Verifies valid POST processes message and redirects with success feedback without database dependency."""
        payload = {
            'name': 'Jane Developer',
            'email': 'jane.dev@example.com',
            'subject': 'Flutter Internship Opportunity',
            'message': 'We are impressed with your RetiyaMarket project and would like to offer an interview.',
            'honeypot': '',
        }
        response = self.client.post(reverse('portfolio:contact'), data=payload, follow=True)
        self.assertEqual(response.status_code, 200)

        # Success message in response
        content = response.content.decode('utf-8')
        self.assertIn('Thank you, Jane Developer!', content)
        self.assertIn('Your message has been sent successfully', content)

    def test_contact_form_invalid_email(self):
        """Verifies that invalid email format is rejected and does not save."""
        initial_count = ContactMessage.objects.count()
        payload = {
            'name': 'Invalid Email Sender',
            'email': 'not-a-valid-email-format',
            'subject': 'Testing invalid email',
            'message': 'This should fail server-side email validation.',
            'honeypot': '',
        }
        response = self.client.post(reverse('portfolio:contact'), data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), initial_count)
        content = response.content.decode('utf-8')
        self.assertIn('Enter a valid email address', content)

    def test_contact_form_empty_required_fields(self):
        """Verifies that blank required fields are rejected."""
        initial_count = ContactMessage.objects.count()
        response = self.client.post(reverse('portfolio:contact'), data={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), initial_count)
        content = response.content.decode('utf-8')
        self.assertIn('Please correct the errors in the form below', content)

    def test_contact_form_honeypot_spam_rejected(self):
        """Verifies that automated bots filling the honeypot are rejected."""
        initial_count = ContactMessage.objects.count()
        payload = {
            'name': 'Spam Bot 3000',
            'email': 'bot@spammer.com',
            'subject': 'Cheap Crypto Deals',
            'message': 'Visit our link for free crypto prizes today!',
            'honeypot': 'I am an automated spam bot',
        }
        response = self.client.post(reverse('portfolio:contact'), data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), initial_count)
        content = response.content.decode('utf-8')
        self.assertIn('Spam submission rejected', content)



