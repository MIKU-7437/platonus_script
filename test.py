class Question:
    def __init__(self, question, answers, correct_answers, answers_i=""):
        # Initialize question text and image
        if isinstance(question, list):
            self.question_text = question[0]
            self.question_img = question[1] if len(question) > 1 else ""
        elif isinstance(question, str):
            self.question_text = question
            self.question_img = ""
        correct_answers_new = correct_answers
        if type(correct_answers)==list:
            pass
        else:
            correct_answers_new = [int(correct_answers)]
        if answers_i:
            answers_i = answers_i.split(',')
            answers_full = []
            for i in range(len(answers_i)):
                answers_full.append([answers[i], answers_i[i], 1 if i+1 in correct_answers_new else 0])  
            self.answers = answers_full
        else:
            answers_full = []
            for i in range(len(answers)):
                answers_full.append([answers[i], "", 1 if (i+1 in correct_answers_new) else 0])  
            self.answers = answers_full  # Handling empty image URLs

        # Initialize correct answers list

q1 = Question("вопрос без картинки", ["1 ответ", "2 ответ", "3 ответ"], 1)
q2 = Question(["вопрос c картинкой", "question_image.jpg"], ["1 ответ", "2 ответ", "3 ответ"], [2, 3], "question_image.jpg,question_image.jpg,question_image.jpg")
questions = [q1, q2]
for q in questions:
    print(q.question_text, q.question_img)
    print(q.answers)
