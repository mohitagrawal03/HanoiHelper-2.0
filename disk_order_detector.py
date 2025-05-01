import cv2
import numpy as np

def extract_disk_order(image_path):
    image = cv2.imread(image_path)
    output = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    disks = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area > 500:
            disks.append((y + h // 2, w, (x, y, w, h)))

    disks.sort(key=lambda d: d[0])

    widths = sorted([w for _, w, _ in disks])
    disk_width_to_id = {w: idx for idx, w in enumerate(sorted(widths))}

    disk_order = []
    for _, w, box in disks:
        disk_id = disk_width_to_id[w]
        disk_order.append(disk_id)
        x, y, bw, bh = box
        cv2.rectangle(output, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
        cv2.putText(output, f'Disk {disk_id}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    print("Extracted Disk Order (Top to Bottom):", disk_order)

    cv2.imshow("Detected Disks", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return disk_order

# Example usage
if __name__ == "__main__":
    image_path = "towerA.jpg"
    order = extract_disk_order(image_path)
