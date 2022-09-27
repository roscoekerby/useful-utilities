# https://github.com/jsvine/pdfplumber
# (original pdfplumber code above)
# import pdfplumber (must have installed pdfplumber: pip3 install pdfplumber)
import pdfplumber

# set page bounds for splitting the page (x1 = 0.5 means to split page into a left and right)
x0 = 0    # Distance of left side of character from left side of page.
x1 = 0.5  # Distance of right side of character from left side of page.
y0 = 0  # Distance of bottom of character from bottom of page.
y1 = 1  # Distance of top of character from bottom of page.

all_content = [] # blank list (no content yet)
f = 'file.pdf' # replace with pdf name

with pdfplumber.open(f) as pdf:
    for i, page in enumerate(pdf.pages): # loop through all pdf pages
        width = page.width # gets page width
        height = page.height # gets page height

        # Crop pages
        left_bbox = (x0 * float(width), y0 * float(height), x1 * float(width), y1 * float(height))
        page_crop = page.crop(bbox = left_bbox)
        left_text = page_crop.extract_text()

        right_bbox = (0.5 * float(width), y0 * float(height), 1 * float(width), y1 * float(height))
        page_crop = page.crop(bbox = right_bbox)
        right_text = page_crop.extract_text()
        page_context = '\n'.join([left_text, right_text])
        all_content.append(page_context)
        
        print(page_context)
       	# can pipe to another file to see it using '>' command in Linux
