from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget , QHBoxLayout , QLabel , QVBoxLayout ,QButtonGroup, QGroupBox, QRadioButton , QPushButton, QLabel)
from random import shuffle
from random import randint , shuffle

class Question():
    def __init__(self, question, right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии' , 'Португальский', 'Английский', 'Испанский' ,'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий'))
question_list.append(Question('Национальная хижина якутов','Ураса','ирта','Иглу','Хата'))

app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

window = QWidget()
window.setWindowTitle('memo Card')# присвание название

'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основана Москва?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_1 = QRadioButton('1147')

rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QHBoxLayout()
Layout_ans3 = QHBoxLayout()
Layout_ans2.addWidget(rbtn_1) # два ответа в первы столбец
Layout_ans2.addWidget(rbtn_2)
Layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
Layout_ans3.addWidget(rbtn_4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3) # разместим столбцы в одной строке

RadioGroupBox.setLayout(Layout_ans1) #ГОТОВА ПАНЕЛЬ С ОТВЕТАМИ

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('Ответ будет тут!')

Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(Layout_res)

Layout_line1 = QHBoxLayout() # вопрос
Layout_line2 = QHBoxLayout() # варианты ответов или результат теста
Layout_line3 = QHBoxLayout() # конопка ответить

Layout_line1.addWidget(lb_Question,alignment=(Qt.AlignCenter|Qt.AlignVCenter))
Layout_line2.addWidget(RadioGroupBox)
Layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()


Layout_line3.addStretch(1)  #для добавления пространства между элементами 
Layout_line3.addWidget(btn_OK , stretch=2)
Layout_line3.addStretch(1)

Layout_card = QVBoxLayout()

Layout_card.addLayout(Layout_line1 , stretch=2)
Layout_card.addLayout(Layout_line2 , stretch=8)
Layout_card.addStretch(1)
Layout_card.addLayout(Layout_line3, stretch=1)
Layout_card.addStretch(1)
Layout_card.setSpacing(5)

def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2 , rbtn_3 , rbtn_4]

def ask(q: Question):
    '''функция записывает значение вопроса и ответов в соответствующие виджеты , при этом варианты ответов распределяются случаным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()   

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score =+ 1
        print('Статистика\n-Всего вопросов:',window.total,'\n-Правильных ответов:', window.score)
        print('Рейтинг:',(window.score/window.total*100), '%')

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():          
            show_correct('Неверно!')
            print('Рейтинг:',(window.score/window.total*100), '%')


def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов:',window.total,'\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()    


def test():
    '''временная функция , которая позвляет нажатием на кнопку вызывать по очереди show_result()  либо show_question()'''
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

window = QWidget()
window.setLayout(Layout_card)
window.setWindowTitle('Memo card')
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()
window.resize(400,300)
window.show()
app.exec()

