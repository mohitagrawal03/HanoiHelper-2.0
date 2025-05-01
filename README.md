# 🧠 Hanoi Helper 2.0 – Solving Unsorted Tower of Hanoi with AI-Powered Vision

**Author:** Mohit Agrawal  
**Project:** Honors Project – *Hanoi Helper 2.0*  
**Institution:** RCOEM, Dept. of Electronics Engineering  

---

## 📌 Problem Statement

The classic **Tower of Hanoi** puzzle starts with disks arranged in sorted order (smallest on top) on a single tower.  
In **Hanoi Helper 2.0**, we challenge this assumption:

- Disks may be **initially in any random order** on **Tower A**.
- The goal is to move them to **Tower B in sorted order**, using **Tower C as auxiliary**, while following standard Hanoi rules:

### ✅ Hanoi Puzzle Rules
- Move only **one disk at a time**.
- Only the **top disk** of any tower can be moved.
- A disk **cannot be placed on top of a smaller disk**.
- Use Towers A, B, and C freely as long as the rules are followed.

---

## 🔍 Project Structure

### ✅ Stage 1 – Algorithmic Solver (`unsorted_hanoi_solver.py`)
A Python implementation of a **DFS + backtracking** algorithm that:
- Accepts **any arbitrary order** of disks on Tower A.
- Uses legal moves to sort and transfer them to Tower B.
- Tracks visited states to avoid cycles.
- Outputs a complete **step-by-step move sequence**.

#### Sample Input:
```python
initial_state = {
    'A': [3, 4, 0, 2, 1],  # Top to bottom
    'B': [],
    'C': []
}
```

#### Sample Output:
```text
Move disk 1 from A to C
Move disk 2 from A to B
...
All disks sorted on Tower B: [0, 1, 2, 3, 4]
```

---

### 🧠 Stage 2 – AI Image Detection (`disk_order_detector.py`)
This module uses **OpenCV** to process an image of **Tower A** and determine the **initial disk order** automatically:

- Detects disks by contour analysis.
- Measures disk widths to assign IDs (Disk 0 = smallest, Disk 4 = largest).
- Returns disk order (top to bottom), e.g., `[2, 0, 1, 3, 4]`.

#### Example:
```python
order = extract_disk_order("towerA.jpg")
# Output: Extracted Disk Order (Top to Bottom): [3, 1, 0, 2, 4]
```

#### Technologies:
- **OpenCV**
- Thresholding + Contour Detection
- Disk size estimation via bounding box width

---

## ⚙️ Requirements

Install dependencies using pip:
```bash
pip install opencv-python numpy
```

---

## 🧠 Future Stages

### ⚙️ Stage 3 – Hardware Integration *(Coming Soon)*
The physical version will include:
- **Camera** for image capture
- **Raspberry Pi** for image processing + logic
- **Arduino Uno** + **Servo motors** to physically move disks
- Full automation of unsorted Hanoi solving

---

## 📂 Files Included

| File                     | Description |
|--------------------------|-------------|
| `unsorted_hanoi_solver.py` | Python algorithm for unsorted Hanoi solving |
| `disk_order_detector.py`   | AI-based disk order extractor using OpenCV |
| `README.md`                | Project documentation |
| `images/`                  | Folder for sample input images |

---

## ✅ Result & Conclusion

The system successfully:
- Reads the initial disk arrangement from a real-world image.
- Computes a legal move sequence to solve the puzzle.
- Demonstrates integration of **AI + Algorithm + Hardware (planned)**.

This project aims to bridge theory with practice, making classical puzzles more interactive and AI-integrated.
