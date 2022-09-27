# https://github.com/jsvine/pdfplumber
# (original pdfplumber code above)
# import pdfplumber, os, sys (must have installed pdfplumber: pip3 install pdfplumber, os, sys)
import os
import pdfplumber
import sys

pdf_count = 1 # number of pdfs extracted
input_directory_name = 'input' # change to the directory that contains pdfs for extraction
#extract_name = 'extract_name' # change to name for extracts

output_directory_name = 'output'

for input_file_name in os.listdir(input_directory_name):
	# Set page bounds for splitting the page (x1 = 0.5 means to split page into a left and right)
	x0 = 0    # Distance of left side of character from left side of page.
	x1 = 0.5  # Distance of right side of character from left side of page.
	y0 = 0  # Distance of bottom of character from bottom of page.
	y1 = 1  # Distance of top of character from bottom of page.

	all_content = []
	with pdfplumber.open('./' + input_directory_name + '/' + input_file_name) as pdf:
	    for i, page in enumerate(pdf.pages):
	    	width = page.width # gets page width
	    	height = page.height # gets page height
	    	left_bbox = (x0 * float(width), y0 * float(height), x1 * float(width), y1 * float(height))
	    	page_crop = page.crop(bbox = left_bbox)
	    	left_text = page_crop.extract_text()
	    	right_bbox = (0.5 * float(width), y0 * float(height), 1 * float(width), y1 * float(height))
	    	page_crop = page.crop(bbox = right_bbox)
	    	right_text = page_crop.extract_text()
	    	page_context = '\n'.join([left_text, right_text])
	    	all_content.append(page_context)
	    	
	    	print(page_context)
	    	
	    	with open(output_directory_name + '/' + input_file_name + '_text_' + str(pdf_count), 'x') as f:
	    		print(page_context, file = f)
	    		pdf_count = pdf_count + 1

