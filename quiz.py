print("Velkommen til Quiz!\n")

questions = [
    {
        "question": "Hva er hovedstaden i Norge?",
        "answer": "oslo"
    },
    {
        "question": "Hva er 5 + 7?",
        "answer": "12"
    },
    {
        "question": "Hvilket språk brukes i Python?",
        "answer": "programmering"
    }
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ").lower()
    
    if user_answer == q["answer"]:
        print("Riktig!\n")
        score += 1
    else:
        print("Feil!\n")

print(f"Du fikk {score} av {len(questions)} riktige!")
