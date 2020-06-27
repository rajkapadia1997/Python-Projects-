import PyPDF2
output = PyPDF2.PdfFileWriter()

with open('super.pdf', "rb") as mainfile:
    pdf = PyPDF2.PdfFileReader(mainfile)
    with open('wtr.pdf', "rb") as filehandle_watermark:
        Watermark = PyPDF2.PdfFileReader(filehandle_watermark).getPage(0)

        for i in range(pdf.getNumPages()):
            page = pdf.getPage(i)
            page.mergePage(Watermark)
            output.addPage(page)
            output.write(open('super.pdf','wb'))


