import pdfquery

pdf = pdfquery.PDFQuery("/Users/aiqi/Desktop/pdfHighlighter/tests/samples/25.pdf")

pdf.load(7)
label = pdf.pq('LTTextLineHorizontal:contains("the most remarkable things")')

box = [float(label.attr('x0')), float(label.attr('y0')), float(label.attr('x1')), float(label.attr('y1'))]

box
