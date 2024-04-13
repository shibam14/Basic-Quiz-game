class Question:
  def __init__(self, prompt, options, correct_option):
      self.prompt = prompt
      self.options = options
      self.correct_option = correct_option

  def display_options(self):
      for i, option in enumerate(self.options):
          print(f"{i + 1}. {option}")

  def check_answer(self, user_answer):
      return user_answer.lower() == self.correct_option.lower()


def run_quiz(questions):
  score = 0
  for question in questions:
      print(question.prompt)
      question.display_options()
      user_answer = input("Enter your answer (1, 2, 3, ...): ")
      if question.check_answer(user_answer):
          print("Correct!\n")
          score += 1
      else:
          print("Incorrect!\n")

  print(f"Quiz completed! Your final score is: {score}/{len(questions)}")


def main():
  # Define your questions here
  question1 = Question("What is the capital of France?",
                       ["1. Paris", "2. Rome", "3. Madrid"],
                       "1")
  question2 = Question("Which planet is known as the Red Planet?",
                       ["1. Earth", "2. Mars", "3. Venus"],
                       "2")
  question3 = Question("What is the powerhouse of the cell?",
                       ["1. Nucleus", "2. Mitochondria", "3. Ribosome"],
                       "2")

  # Customize the quiz by adding or removing questions
  questions = [question1, question2, question3]

  print("Welcome to the Quiz Game!\n")
  run_quiz(questions)


if __name__ == "__main__":
  main()

      
             
   

        
      