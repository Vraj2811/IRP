import argparse
from fpdf import FPDF

def generate_resume(data, font_size, font_color, background_color, output_file="resume.pdf"):
    pdf = FPDF()
    pdf.add_page()  # Ensure the page is added before setting the background

    # Set background color
    pdf.set_fill_color(*color_to_rgb(background_color))
    pdf.rect(0, 0, pdf.w, pdf.h, style='F')

    # Set font color and size
    pdf.set_text_color(*color_to_rgb(font_color))
    pdf.set_font('Arial', size=font_size)

    # Set margins
    pdf.set_left_margin(10)
    pdf.set_right_margin(20)

    # Add header
    pdf.set_font('Arial', 'B', size=font_size + 10)
    pdf.cell(0, 10, txt=data['name'], ln=True, align='C')

    # Contact information
    pdf.set_font('Arial', 'B', size=font_size)
    pdf.cell(0, 10, txt="Contact", ln=True, align='L')
    pdf.set_font('Arial', size=font_size - 2)
    pdf.cell(0, 10, txt=data['contact'], ln=True)
    pdf.cell(0, 10, txt=data['address'], ln=True)
    pdf.cell(0, 10, txt=data['website'], ln=True)
    pdf.ln(5)

    # Work Experience
    pdf.set_font('Arial', 'B', size=font_size)
    pdf.cell(0, 10, txt="Work Experience", ln=True)
    pdf.set_font('Arial', size=font_size - 2)
    for exp in data['work_experience']:
        pdf.cell(0, 10, txt=f"{exp['date']} - {exp['company']}", ln=True)
        pdf.cell(0, 10, txt=exp['title'], ln=True)
        for detail in exp['details']:
            pdf.multi_cell(0, 10, txt=f"- {detail}")
        pdf.ln(3)

        # Add a new page if the content is too long
        if pdf.get_y() > 250:  # Adjust this value depending on your needs
            pdf.add_page()
            pdf.set_fill_color(*color_to_rgb(background_color))  # Maintain the background color
            pdf.rect(0, 0, pdf.w, pdf.h, style='F')

    # Education
    pdf.set_font('Arial', 'B', size=font_size)
    pdf.cell(0, 10, txt="Education", ln=True)
    pdf.set_font('Arial', size=font_size - 2)
    for edu in data['education']:
        pdf.cell(0, 10, txt=edu, ln=True)
    pdf.ln(10)

    # Skills
    pdf.set_font('Arial', 'B', size=font_size)
    pdf.cell(0, 10, txt="Skills", ln=True)
    pdf.set_font('Arial', size=font_size - 2)
    pdf.multi_cell(0, 10, txt=", ".join(data['skills']))

    # Save the PDF
    pdf.output(output_file)
    print(f"Resume saved as {output_file}")

def hex_to_rgb(hex_color):
    """Convert a hex color to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def color_to_rgb(color):
    """Convert a color name or hex code to an RGB tuple."""
    colors = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "gray": (128, 128, 128),
        "orange": (255, 165, 0),
        "purple": (128, 0, 128),
        "brown": (165, 42, 42),
        "pink": (255, 192, 203),
        "lime": (0, 255, 0),
        "navy": (0, 0, 128),
        "teal": (0, 128, 128),
        "gold": (255, 215, 0),
        "silver": (192, 192, 192),
        "beige": (245, 245, 220),
        "maroon": (128, 0, 0)
    }
    if color.lower() in colors:
        return colors[color.lower()]
    return hex_to_rgb(color)

def get_user_input():
    """Prompt the user for resume data or use defaults."""
    name = input("Enter your name (default: Olivia Wilson): ") or "Olivia Wilson"
    contact = input("Enter your contact info (default: +123-456-7890 | hello@reallygreatsite.com): ") or "+123-456-7890 | hello@reallygreatsite.com"
    address = input("Enter your address (default: 123 Anywhere St., Any City): ") or "123 Anywhere St., Any City"
    website = input("Enter your website (default: www.reallygreatsite.com): ") or "www.reallygreatsite.com"

    print("\nEnter work experiences (leave blank to skip):")
    work_experience = []
    while True:
        date = input("- Enter work period (e.g., 2020 - 2022): ")
        if not date:
            break
        company = input("  Enter company name: ")
        title = input("  Enter job title: ")
        details = []
        print("  Enter details (leave blank to finish):")
        while True:
            detail = input("    Detail: ")
            if not detail:
                break
            details.append(detail)
        work_experience.append({"date": date, "company": company, "title": title, "details": details})

    print("\nEnter education (leave blank to skip):")
    education = []
    while True:
        edu = input("- Enter education details (e.g., 2020 - 2024: XYZ University, B.Sc. in CS): ")
        if not edu:
            break
        education.append(edu)

    skills = input("Enter skills (comma-separated, default: Project Management, Public Relations, Teamwork): ")
    skills = skills.split(", ") if skills else ["Project Management", "Public Relations", "Teamwork"]

    return {
        "name": name,
        "contact": contact,
        "address": address,
        "website": website,
        "work_experience": work_experience,
        "education": education,
        "skills": skills
    }

def main():
    parser = argparse.ArgumentParser(description="Generate a customizable resume PDF.")
    parser.add_argument('--font-size', type=int, default=14, help="Font size for the text.")
    parser.add_argument('--font-color', type=str, default="black", help="Font color by name or hex format (e.g., #000000).")
    parser.add_argument('--background-color', type=str, default="white", help="Background color by name or hex format (e.g., #FFFFFF).")
    parser.add_argument('--interactive', action='store_true', help="Use interactive mode to input data.")

    args = parser.parse_args()

    if args.interactive:
        data = get_user_input()
    else:
        data = {
            "name": "Olivia Wilson",
            "contact": "+123-456-7890 | hello@reallygreatsite.com",
            "address": "123 Anywhere St., Any City",
            "website": "www.reallygreatsite.com",
            "work_experience": [
                {"date": "2030 - Present", "company": "Borcelle Studio", "title": "Marketing Manager & Specialist",
                 "details": [
                     "Led the development and implementation of comprehensive marketing strategies that resulted in a 20% increase in brand visibility and a 15% growth in sales within the first year.",
                     "Successfully launched and managed multiple cross-channel campaigns, including digital marketing, social media, and traditional advertising, resulting in improved customer acquisition and retention rates."
                 ]},
                {"date": "2025 - 2029", "company": "Fauget Studio", "title": "Marketing Manager & Specialist",
                 "details": [
                     "Developed and executed targeted marketing campaigns, resulting in a 25% increase in lead generation.",
                     "Implemented SEO strategies that improved website traffic by 30%, enhancing online visibility and positioning the company."
                 ]}
            ],
            "education": [
                "2029 - 2030: Borcelle University, Master of Business Management",
                "2025 - 2029: Borcelle University, Bachelor of Business Management (GPA: 3.8/4.0)"
            ],
            "skills": ["Project Management", "Public Relations", "Teamwork", "Time Management", "Leadership", "Effective Communication", "Critical Thinking"]
        }

    generate_resume(data, args.font_size, args.font_color, args.background_color)

if __name__ == "__main__":
    main()
