class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number} {current_question.q_text} (True/False) ?")
        self.check_answer(response, current_question.q_answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Check if the answer is right or false"""
        if user_answer.lower() == correct_answer.lower():
            print('You got it right! ')
            self.score += 1
        else:
            print('You got it wrong')
        print(f"The correct answer is {correct_answer}")
        print(f'Your score is {self.score} / {self.question_number} ')