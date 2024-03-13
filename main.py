from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Generate master page
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=22)
    # Set text color to gray color
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Add lines which should be 10mm apart from each other
    for j in range(20, 298, 10):
        pdf.line(10, j, 200, j)

    # Add Footer for master page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # Generate child pages
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Add Footer for child pages
        # Added h=12, because there is no Header in child pages
        pdf.ln(265 + 12)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # Add lines which should be 10mm apart from each other
        for j in range(20, 298, 10):
            pdf.line(10, j, 200, j)

pdf.output("output.pdf")


































