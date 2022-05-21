import inquirer

def questionMenu():
    questions = [
        inquirer.List(
            "menu",
            message="Choice what do you want to do...",
            choices=[
                ("1. Show candidates", "1"),
                ("2. Number of votes cast", "2"),
                ("3. Number of votes by gender", "3"),
                ("4. Number of votes by candidates", "4"),
                ("5. Percent of votes sorted by candidates", "5"),
                ("6. Quit", "6")
            ],
            carousel=True
        )
    ]
    choice = inquirer.prompt(questions)
    return choice['menu']