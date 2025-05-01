# 🧠 Hanoi Helper 2.0 – Stage 1: Unsorted Tower of Hanoi Solver

**Author:** Mohit Agrawal  
**Project:** Hanoi Helper 2.0  
**Stage 1:** Solving the puzzle with arbitrary (unsorted) initial disk configuration via Python simulation

---

## 📌 Problem Statement

The traditional **Tower of Hanoi** puzzle assumes disks are initially sorted (smallest on top, largest at bottom) on one tower.  
In **Hanoi Helper 2.0**, we generalize the problem:  
➡️ **The disks can initially be in any order** on Tower A.  
➡️ The goal is still to move all disks to **Tower B in sorted order**, using **Tower C as auxiliary**, while obeying the classic rules:

### ✅ Tower of Hanoi Rules
- Only **one disk** may be moved at a time.
- You can only move the **top disk** from any tower.
- A larger disk **cannot be placed on top of a smaller** disk.
- Disks may be moved freely between Towers A, B, and C as long as rules are followed.

---

## 🚀 What This Program Does

This Python script simulates a **recursive backtracking algorithm** that:
1. Takes any initial disk order (e.g., `[3, 4, 0, 2, 1]`) on Tower A.
2. Explores all **valid move sequences** using DFS with visited state tracking.
3. Outputs a **step-by-step move list** that transforms the unsorted stack on Tower A into a sorted stack on Tower B.

---

## 🛠️ Technologies & Concepts Used

| Component       | Details |
|----------------|---------|
| Language        | Python 3.8+ |
| Algorithm       | Depth-First Search (DFS) with backtracking |
| Data Structures | Dictionaries, Lists, Sets |
| Problem Space   | Explores all valid transitions of disk configurations |
| Complexity      | Time: `O(3^n)` worst-case (like original Hanoi), space-optimized with visited state cache |

---

## 🧪 Sample Run

```bash
$ python unsorted_hanoi_solver.py
