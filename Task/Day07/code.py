# Quiz Game

import random
import time


question_bank = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 12", "C) 15", "D) 9"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Fe", "D) Hg"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "How many continents are there?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    }
]

selected_questions = random.sample(question_bank, 5)

score = 0


print("📌 Welcome to the Quiz Game! 🧠❓\n")

for i, q in enumerate(selected_questions, 1):
    print(f"Question {i}: {q['question']}")
    for option in q["options"]:
        print(option)

    start_time = time.time()


    answer = None
    while time.time() - start_time < 10:
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer in ["A", "B", "C", "D"]:
            break
        print("Invalid input! Please enter A, B, C, or D.")

    if answer is None:
        print("⏳ Time's up! No answer recorded.\n")
    elif answer == q["answer"]:
        print("✅ Correct! 🎉\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is {q['answer']}.\n")

print(f"🎯 Final Score: {score}/5")