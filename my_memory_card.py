from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer,wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ans.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    ans.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if ans.text() == 'Ответить':
        show_result()
    else:
        show_question()


def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    text3.setText(q.right_answer)
    show_question()

def show_correct(res):
    text2.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Правильных:', main_win.score)
        print('Рейтинг правильных ответов:',main_win.score/main_win.total*100)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)
    main_win.total += 1
    print('Всего:', main_win.total)

def click_ok():
    if ans.text() == 'Ответить':
        check_answer()
    else:
        next_question()

app = QApplication([])
main_win = QWidget()
main_win.cur_question = -1
main_win.setWindowTitle('Memory Card')
lb_question = QLabel('Какой национальности не существует?')
ans = QPushButton('Ответить')
btn_answer1 = QRadioButton('Энцы       ')
btn_answer2 = QRadioButton('Чулымцы')
btn_answer3 = QRadioButton('Смурфы')
btn_answer4 = QRadioButton('Алеуты')
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
RadioGroupBox = QGroupBox('Варианты ответов')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)
RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат теста')
#text1 = QLabel('Самый сложный вопрос в мире!')
text2 = QLabel('Правильно/Неправильно')
text3 = QLabel('Правильный ответ')
#ans_button = QPushButton('Следующий вопрос')
layout_ans6 = QVBoxLayout()
layout_ans6.addWidget(text2, alignment=Qt.AlignLeft)
layout_ans6.addWidget(text3, alignment=Qt.AlignCenter)

AnsGroupBox.setLayout(layout_ans6)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line2.addWidget(AnsGroupBox, alignment=Qt.AlignCenter)
layout_line1.addWidget(lb_question, alignment = Qt.AlignCenter)
layout_line2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layout_line3.addWidget(ans, alignment = Qt.AlignCenter)
AnsGroupBox.hide()
layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1)
layout_main.addLayout(layout_line2)
layout_main.addLayout(layout_line3)
ans.clicked.connect(click_ok)
questions_list = []
q1 = Question('Какой город изображен на современной российской купюре 1000 рублей?', 'Ярославль', 'Москва', 'Хабаровск', 'Архангельск')
q2 = Question('Сколько человек живет на планете Земля?', 'Около 7,5 млрд', 'Около 12 млрд', 'Около 10 млрд', 'Около 3 млрд')
q3 = Question('Человек состоит из воды на...', '65-75%', '90%', '60%','53%')
q4 = Question('С какой страной Россия не имеет границ?', 'Таджикистан', 'Норвегия','Грузия','КНДР')
q5 = Question('Самый большой штат США - это?','Аляска','Калифорния','Техас','Аризона')
q6 = Question('Статуя Свободы в Нью-Йорке была подарена...', 'Францией', 'никем','Бразилией','Китаем')
q7 = Question('В какой стране живет больше всего людей?','Китай','Россия','США','Бразилия')
q8 = Question('В какой стране больше одной столицы?','ЮАР','США','Россия','Китай')
q9 = Question('Назовите столицу Европейского Союза?', 'Брюссель','Вена', 'Париж', 'Кельн')
q10 = Question('В каком году была разрушена Берлинская стена?','1989','1992','1987','1993')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
questions_list.append(q10)
q = Question('фывф', 'sdasda','gfdgfd', 'dsaasd', 'sdasd')
main_win.score = 0
main_win.total = 0
next_question()
main_win.setLayout(layout_main)
main_win.show()
app.exec_()