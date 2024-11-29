import cv2
import numpy as np


def grabcut_binarization(image):
    # Convert image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create a mask image, initialized to probable background
    mask = np.zeros(image.shape[:2], np.uint8)

    # Define initial rectangle for GrabCut
    height, width = image.shape[:2]
    rect = (10, 10, width - 20, height - 20)

    # GrabCut's background and foreground models
    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    # Apply GrabCut algorithm
    cv2.grabCut(image_rgb, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    # Convert the mask to binary where the probable foreground is white
    bin_mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Multiply the mask with the image to get a clean binary image
    binary_image = image * bin_mask[:, :, np.newaxis]

    return binary_image


def align_image(image):
    # Use GrabCut to binarize the image
    binary_image = grabcut_binarization(image)

    # Convert the binary image to grayscale
    gray = cv2.cvtColor(binary_image, cv2.COLOR_BGR2GRAY)

    # Apply threshold to enhance contours
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour that can be approximated to a rectangle
    largest_contour = None
    max_area = 0

    for contour in contours:
        # Approximate contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check if it has 4 corners (a rectangle) and if it's the largest contour
        if len(approx) == 4:
            area = cv2.contourArea(approx)
            if area > max_area:
                max_area = area
                largest_contour = approx

    # If no contour is found, return the original image
    if largest_contour is None:
        print("No document found!")
        return image

    # Get the four points of the largest contour
    pts = largest_contour.reshape(4, 2)

    # Order the points to be: top-left, top-right, bottom-right, bottom-left
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]  # Top-left
    rect[2] = pts[np.argmax(s)]  # Bottom-right
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]  # Top-right
    rect[3] = pts[np.argmax(diff)]  # Bottom-left

    # Calculate the width and height of the new image
    (tl, tr, br, bl) = rect
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)

    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))

    # Destination points for the perspective transform (homography)
    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")

    # Compute the homography matrix and apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    aligned = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return aligned


def resize_image(image, width=500):
    # Calculate the ratio of the new width to the old width
    ratio = width / float(image.shape[1])
    dim = (width, int(image.shape[0] * ratio))

    # Resize the image
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return resized


def process_document(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Align the image to be facing up
    aligned_image = align_image(image)

    # Resize the output to have a width of 500 pixels
    resized_image = resize_image(aligned_image, width=500)

    # Save the processed image
    cv2.imwrite(output_path, resized_image)
    print(f"Processed image saved to: {output_path}")


# Example usage
# image_path = 'scew doc.png'  # Input image path
image_path = 'scanned-form.jpg'
output_path = 'output_document.jpg'  # Output image path
process_document(image_path, output_path)

