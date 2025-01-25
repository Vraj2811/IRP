
# Resume Generator Python Script

This Python script generates a customizable PDF resume. It allows users to input their personal data, work experience, education, and skills, as well as customize the font size, font color, and background color of the resume. The script uses the `argparse` library for command-line arguments and `FPDF` for creating the PDF file.

## Requirements

Before running the script, ensure you have the following dependencies installed:

- `fpdf`: A library for creating PDF documents in Python.

```bash
pip install fpdf
```

## Script Overview

### Functions

1. **`generate_resume(data, font_size, font_color, background_color, output_file="resume.pdf")`**
   - Generates the resume PDF with the given data, font size, font color, background color, and output file name.
   
2. **`hex_to_rgb(hex_color)`**
   - Converts a hex color code to an RGB tuple.
   
3. **`color_to_rgb(color)`**
   - Converts a color name or hex code to an RGB tuple. Supports predefined color names like "black", "white", "red", etc.

4. **`get_user_input()`**
   - Collects the user's input for the resume (name, contact information, work experience, education, skills) in interactive mode.

5. **`main()`**
   - Parses command-line arguments, handles the logic for interactive mode, and generates the resume.

### Command-Line Arguments

- `--font-size`: Set the font size for the resume text (default: 14).
- `--font-color`: Set the font color using a name or hex format (e.g., "black", "#000000") (default: "black").
- `--background-color`: Set the background color using a name or hex format (e.g., "white", "#FFFFFF") (default: "white").
- `--interactive`: Use interactive mode to input resume data.

### Example Usage

To generate a resume with a specific font size, font color, and background color:

```bash
python generate_resume.py --font-size 16 --font-color "#0000FF" --background-color "yellow"
```

To use interactive mode:

```bash
python generate_resume.py --font-size 16 --font-color "#0000FF" --background-color "yellow" --interactive
```

This will prompt you for the required details (name, contact information, work experience, education, skills) to create the resume.

## Sample Resume Data

If not using interactive mode, the script uses the following default data:

- **Name**: Olivia Wilson
- **Contact**: +123-456-7890 | hello@reallygreatsite.com
- **Address**: 123 Anywhere St., Any City
- **Website**: www.reallygreatsite.com
- **Work Experience**:
  - **Company**: Borcelle Studio
    - **Title**: Marketing Manager & Specialist
    - **Details**:
      - Led the development and implementation of marketing strategies resulting in a 20% increase in brand visibility.
      - Successfully launched and managed multiple cross-channel campaigns.
  - **Company**: Fauget Studio
    - **Title**: Marketing Manager & Specialist
    - **Details**:
      - Developed and executed targeted marketing campaigns resulting in a 25% increase in lead generation.
      - Implemented SEO strategies improving website traffic by 30%.
- **Education**:
  - 2029 - 2030: Borcelle University, Master of Business Management
  - 2025 - 2029: Borcelle University, Bachelor of Business Management (GPA: 3.8/4.0)
- **Skills**: Project Management, Public Relations, Teamwork, Time Management, Leadership, Effective Communication, Critical Thinking
