import pdfquery

pdf = pdfquery.PDFQuery("test.pdf")

pdf.load()

label = pdf.pq('LTTextLineHorizontal:contains("real life challenges")')

box = [label.attr('x0'), label.attr('y0'), label.attr('x1'), label.attr('y1')]

print(box)
