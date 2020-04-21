from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet



def generate_report(attatchment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attatchment)
    report_title = Paragraph(title, styles["h1"])
    report_paragraph = Paragraph(paragraph,styles["BodyTest"])
    empty_line = Spacer(1, 20)
    report.build([report_title,empty_line,report_paragraph])
