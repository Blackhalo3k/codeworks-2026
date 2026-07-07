# QUIZ made by Odom

score = 0

questions = [
    {
        "question": "1. Do Pineapples belong on pizza?",
        "options": [
            "A: Heck yea!",
            "B: HECK NO",
            "C: I mean..kinda?",
            "D: You deserve Jail Time."
        ],
        "answer": "C"
    },

    {
        "question": "2. Who is the main character of Demon Slayer (Kimetsu No Yaiba)?",
        "options": [
            "A: Tanjiro Kamado",
            "B: Gonpachiro Kamaboko",
            "C: That one guy with the Black and Green Haori",
            "D: All of The Above"
        ],
        "answer": "D"
    },

    {
        "question": "3. Who is the Leader of the Phantom Thieves in Persona 5?",
        "options": [
            "A: Ren Amamiya",
            "B: Akira Kurusu",
            "C: You Name Him",
            "D: All Of The Above"
        ],
        "answer": "D"
    },

    {
        "question": "4. What's the capital of France?",
        "options": [
            "A: Paris",
            "B: Belgium",
            "C: Wales",
            "D: Japan"
        ],
        "answer": "A"
    }
]

print("===== Welcome to my Quiz! =====\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    response = input("Enter your answer (A, B, C, or D): ").strip().upper()

    if response == q["answer"]:
        print("Correctamundo!")
        score += 1
    else:
        print(f"WRONNNGGG! The correct answer was {q['answer']}.")

    print("=" * 40)

print(f"\nYour Final Score: {score}/{len(questions)}")