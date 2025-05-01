import cv2
import numpy as np

def extract_disk_order(image_path):
    # Read image
    image = cv2.imread(image_path)
    output = image.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold the image
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by size and aspect ratio (assuming disks are roughly elliptical)
    disks = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area > 500:  # minimum area threshold
            disks.append((y + h // 2, w, (x, y, w, h)))  # center Y used for sorting

    # Sort disks by vertical position (top to bottom)
    disks.sort(key=lambda d: d[0])

    # Sort by width to assign disk numbers (0 = smallest, 4 = largest)
    widths = sorted([w for _, w, _ in disks])
    disk_width_to_id = {w: idx for idx, w in enumerate(sorted(widths))}

    # Final disk order from top to bottom
    disk_order = []
    for _, w, box in disks:
        disk_id = disk_width_to_id[w]
        disk_order.append(disk_id)
        # Optional: draw rectangles and labels
        x, y, bw, bh = box
        cv2.rectangle(output, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
        cv2.putText(output, f'Disk {disk_id}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    print("Extracted Disk Order (Top to Bottom):", disk_order)

    # Show debug image
    cv2.imshow("Detected Disks", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return disk_order

# Example usage
if __name__ == "__main__":
    image_path = "towerA.jpg"  # Replace with your image
    order = extract_disk_order(image_path)
