from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from PIL import Image
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('OpenSans', 'OpenSans-CondBold.ttf'))
pdfmetrics.registerFont(TTFont('Deca', 'decalotype.extrabold.ttf'))
import csv
import os

# Data CSV
data_file = "assets/ListNama.csv"
# Create folder untuk menyimpan data sertifikat pada folder
FolderSertifikat = 'FolderSertifikat/'
if not os.path.exists(FolderSertifikat):
    os.makedirs(FolderSertifikat)

# Generate Sertifikat
def generate_certificate(number, name, part, pdf_file_name):
    sertif = canvas.Canvas(pdf_file_name, pagesize=landscape(A4))
    width, height = A4
    # Background dan Design sertifikat/pdf file
    image_path = "assets/designsertif.png"
    sertif.drawImage(image_path,0,0,width=height,height=width)
    # No Sertifikat
    sertif.setFont('OpenSans',16)
    sertif.setFillColor('white')
    sertif.drawCentredString(height/2,410,'No: '+number+'/Certificate/Test/2021')
    # Nama peserta
    sertif.setFont('Deca',36)
    sertif.setFillColor('white')
    sertif.drawCentredString(height/2,320,name)
    # Part/sebagai
    sertif.setFont('Helvetica-Bold',28)
    sertif.setFillColor('white')
    sertif.drawCentredString(height/2,260,part)
    sertif.showPage()
    sertif.save()

# Generate data peserta dari CSV
def main(data_file):
    attendee_data = csv.reader(open(data_file,'r'))
    for row in attendee_data:
        number = row[0]
        name = row[1]
        part = row[2]
        code = row[3]
        pdf_file_name = FolderSertifikat + code + '.pdf'
        generate_certificate(number, name, part, pdf_file_name)

main(data_file)
