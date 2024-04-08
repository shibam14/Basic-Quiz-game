# Basic-Quiz-game
class question:
    def __init__(self,prompt,options,correct_option):
        self.prompt=prompt
        self.options=options
        self.correct_option=correct_option
        def display_options(self):
            for i, option in enumerate(self.options):
                print(f"{i+1}.{option}")
                def check_answer(self,user_answer):
                    return user_answer.lower == self.correct_option.lower()
                def run_quiz(options):
                    score=0
                    for question in questions:
                        print(question.prompt)
                        question.display_options()
        user_answer=input("Enter your answer(1,2,3,....):")
        if question.check_answer(user_answer):
            print("correct!/n")
            esle:
            print("Incorrect!/n")
            print(f"quiz completed!your final score is:{score}/{len(questions)}")
            def main():
                question1=Question("What is the colour of grass?"["1.Green" "2. Red" "3.white"]"1")
                question2=Question("what is the colour of sky?"["1.Blue" "2.green" "3.Red"]"1")
                question3=Question("Whta is the color of apple?"["1.Blue" "2.Red" "3.Green"]"2")
                questions=[question1,question2,question3]
                print("Welcome to quiz game\n")
                run_quiz(question)
if __name__=="__main__":
    main()
