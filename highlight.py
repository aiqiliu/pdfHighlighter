import pdfquery

pdf = pdfquery.PDFQuery("test.pdf")

pdf.load()
x0 = 0
x1 = 0
x2 = 0
x3 = 0
#pageNum = pdf.doc.catalog['Pages'].resolve()['Count'] #get number of pages
# print (pageNum)

label = pdf.pq('LTTextLineHorizontal:contains("is")')

# x0 = float(label.attr('x0'))
# y0 = float(label.attr('y0'))
# x1 = float(label.attr('x1'))
# y1 = float(label.attr('y1'))

# box = [x0, y0, x1, y1]

#results = []
#print(box)

locate = pdf.pq('LTTextLineHorizontal:in_bbox("72.0, 548.456, 372.81, 571.256")').text() 
#print(locate)
search ='LTTextLineHorizontal:contains("is")'
print(search)

def getCoordinates(label):
	x0 = float(label.attr('x0'))
	y0 = float(label.attr('y0'))
	x1 = float(label.attr('x1'))
	y1 = float(label.attr('y1'))

	box = [x0,x1,x2,x3]
	return box

cells = pdf.extract ([
	('with_formatter', 'text'),
	('with_parent','LTPage[page_index="0"]'),
    ('cell', search)

	])

# #[cell.text.encode('utf-8').strip() for cell in cells['cells']]
#print(cells)
# label2 = pdf.pq('LTTextLineHorizontal:contains("ssme techniques can be")')
# x00 = float(label.attr('x0'))
# y00 = float(label.attr('y0'))
# x10 = float(label.attr('x1'))
# y10 = float(label.attr('y1'))

# box2 = [x00, y00, x10, y10]
# print(box2)


# exact = pdf.extract([
#      ('with_parent','LTPage[page_index="0"]'),
#      ('real life challenges', ':in_bbox("72.0, 358.456, 530.71, 374.428")') # only matches elements on page 1
#  ])

# locate = pdf.pq('LTTextLineHorizontal:in_bbox("72.0, 358.456, 530.71, 374.428")').text() 
# print(locate)
# LTPage[page_index = 1]