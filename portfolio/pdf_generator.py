"""
Pinkal Rathod Portfolio – Professional PDF Resume Generator
Generates an ATS-friendly, clean, elegant A4 PDF resume using ReportLab.
Uses only verified personal information without fabricated entries or broken links.
"""

import io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    KeepTogether,
)

# Brand Color Palette
COLOR_NAVY = colors.HexColor('#0B1220')
COLOR_BLUE = colors.HexColor('#1A56DB')
COLOR_SLATE = colors.HexColor('#334155')
COLOR_MUTED = colors.HexColor('#64748B')
COLOR_BORDER = colors.HexColor('#CBD5E1')
COLOR_BG_LIGHT = colors.HexColor('#F8FAFC')


def create_resume_pdf_buffer(personal_info, education_list, skills_list, projects_list):
    """
    Generates a high-quality, ATS-optimized A4 PDF resume for Pinkal Rathod
    and returns an in-memory BytesIO buffer containing the PDF bytes.
    """
    buffer = io.BytesIO()

    # Document setup: A4 with 36pt (0.5 inch) margins for maximum clean printable area
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=32,
        bottomMargin=32,
    )

    styles = getSampleStyleSheet()

    # Custom Typography Styles
    title_style = ParagraphStyle(
        'ResumeTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=COLOR_NAVY,
        spaceAfter=2,
    )

    subtitle_style = ParagraphStyle(
        'ResumeSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=COLOR_BLUE,
        spaceAfter=6,
    )

    contact_style = ParagraphStyle(
        'ResumeContact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=COLOR_SLATE,
    )

    section_heading_style = ParagraphStyle(
        'ResumeSectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=COLOR_NAVY,
        spaceBefore=8,
        spaceAfter=2,
    )

    body_style = ParagraphStyle(
        'ResumeBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=COLOR_SLATE,
    )

    bullet_style = ParagraphStyle(
        'ResumeBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=COLOR_SLATE,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2,
    )

    bold_item_style = ParagraphStyle(
        'ResumeBoldItem',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=COLOR_NAVY,
    )

    meta_style = ParagraphStyle(
        'ResumeMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=COLOR_MUTED,
    )

    story = []

    # ====================================================
    # 1. HEADER SECTION
    # ====================================================
    story.append(Paragraph(personal_info['name'].upper(), title_style))
    story.append(Paragraph(personal_info['title'].upper(), subtitle_style))

    contact_line1 = (
        f"<b>Location:</b> {personal_info['location']} &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"<b>Phone:</b> {personal_info['phone']} &nbsp;&nbsp;|&nbsp;&nbsp; "
        f"<b>Email:</b> {personal_info['personal_email']}"
    )
    contact_line2 = f"<b>Academic Email:</b> {personal_info['academic_email']}"
    if personal_info.get('linkedin_url'):
        contact_line2 += f" &nbsp;&nbsp;|&nbsp;&nbsp; <b>LinkedIn:</b> {personal_info['linkedin_url']}"

    story.append(Paragraph(contact_line1, contact_style))
    story.append(Paragraph(contact_line2, contact_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_BLUE, spaceBefore=4, spaceAfter=8))

    # ====================================================
    # 2. CAREER OBJECTIVE
    # ====================================================
    story.append(Paragraph("CAREER OBJECTIVE", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=1, spaceAfter=4))
    story.append(Paragraph(personal_info['career_objective'], body_style))
    story.append(Spacer(1, 6))

    # ====================================================
    # 3. PROFESSIONAL SUMMARY
    # ====================================================
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=1, spaceAfter=4))
    story.append(Paragraph(personal_info['professional_summary'], body_style))
    story.append(Spacer(1, 6))

    # ====================================================
    # 4. TECHNICAL SKILLS
    # ====================================================
    story.append(Paragraph("TECHNICAL SKILLS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=1, spaceAfter=4))

    skills_table_data = []
    for skill_grp in skills_list:
        cat_para = Paragraph(f"<b>{skill_grp['category']}:</b>", bold_item_style)
        items_para = Paragraph(", ".join(skill_grp['skills']), body_style)
        skills_table_data.append([cat_para, items_para])

    skills_table = Table(skills_table_data, colWidths=[150, 373])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 6))

    # ====================================================
    # 5. PROJECTS
    # ====================================================
    story.append(Paragraph("PROJECTS", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=1, spaceAfter=4))

    for proj in projects_list:
        proj_elements = []
        proj_header = f"<b>{proj['title']}</b>"
        tech_line = f"<i>Technologies: {proj['technologies']}</i>"

        proj_elements.append(Paragraph(proj_header, bold_item_style))
        proj_elements.append(Paragraph(tech_line, meta_style))
        proj_elements.append(Spacer(1, 2))

        for pt in proj['points']:
            proj_elements.append(Paragraph(f"&bull;&nbsp; {pt}", bullet_style))

        proj_elements.append(Spacer(1, 4))
        story.append(KeepTogether(proj_elements))

    story.append(Spacer(1, 4))

    # ====================================================
    # 6. EDUCATION
    # ====================================================
    story.append(Paragraph("EDUCATION", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=1, spaceAfter=4))

    edu_table_data = []
    for edu in education_list:
        inst_para = Paragraph(f"<b>{edu['institution']}</b>", bold_item_style)
        deg_para = Paragraph(f"{edu['degree']} ({edu['period']})", body_style)

        score_text = ""
        if 'cgpa' in edu and edu['cgpa']:
            score_text = f"<b>CGPA:</b> {edu['cgpa']}"
        elif 'percentage' in edu and edu['percentage']:
            score_text = f"<b>Percentage:</b> {edu['percentage']}"
            if 'percentile_rank' in edu and edu['percentile_rank']:
                score_text += f" | <b>PR:</b> {edu['percentile_rank']}"

        score_para = Paragraph(score_text, body_style) if score_text else Paragraph("", body_style)

        edu_table_data.append([
            inst_para,
            deg_para,
            score_para
        ])

    edu_table = Table(edu_table_data, colWidths=[200, 180, 143])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 6))

    # ====================================================
    # 7. WORK EXPERIENCE
    # ====================================================
    story.append(Paragraph("WORK EXPERIENCE", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=1, spaceAfter=4))
    story.append(Paragraph(f"<b>{personal_info['work_experience']['role']}</b>", bold_item_style))
    story.append(Paragraph(personal_info['work_experience']['details'], body_style))
    story.append(Spacer(1, 6))

    # ====================================================
    # 8. LANGUAGES
    # ====================================================
    story.append(Paragraph("LANGUAGES", section_heading_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=COLOR_BORDER, spaceBefore=1, spaceAfter=4))
    story.append(Paragraph(", ".join(personal_info['languages']), body_style))

    # Build document
    doc.build(story)
    buffer.seek(0)
    return buffer
