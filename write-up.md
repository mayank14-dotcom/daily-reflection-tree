# Daily Reflection Tree – Design Document

## 1. Objective
The goal of this project is to design a deterministic reflection system that helps users reflect on their day through structured decision-making, without using any AI at runtime.

---

## 2. Core Idea
I designed the system around three psychological axes:

1. Locus of Control (Victim vs Victor mindset)
2. Contribution vs Entitlement
3. Perspective (Self vs Others)

These axes help a user understand how they approached their day mentally and behaviorally.

---

## 3. Design Approach
I followed a top-down approach:

- First defined the three axes of reflection
- Then created questions for each axis
- Then mapped each answer to a deterministic next step
- Finally added reflections that summarize the user’s mindset

---

## 4. Question Design Philosophy
All questions are:
- Simple and conversational
- Easy to answer after a long day
- Designed to reveal mindset, not test knowledge

Each option represents a distinct psychological state to avoid ambiguity.

---

## 5. Branching Logic
The system is fully deterministic:
- Every answer leads to a fixed next node
- No randomness or AI is used
- Same input always produces same reflection path

---

## 6. AI Usage
AI tools were used only during brainstorming and structuring ideas. Final decisions on wording, structure, and branching logic were refined manually to ensure clarity and correctness.

---

## 7. Improvements
If extended further, I would:
- Add deeper branching per axis
- Introduce micro-action suggestions at the end
- Improve personalization of reflections
