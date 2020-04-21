from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet



def generate_report(attatchment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attatchment)
    report_title = Paragraph(title, styles["h1"])
    report_paragraph = Paragraph(paragraph,styles["BodyTest"])
    report.build([report_title,report_paragraph])
