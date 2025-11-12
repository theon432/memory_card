from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout, QGroupBox
from random import shuffle

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')
main_win.move(700,300)
main_win.resize(400,200)

Questions = {
    '0':{
        'text':'Государственный язык Бразилии',
        'answers':['Португальский','Испанский','Английский','Бразильский'] 
        },
    '1':{
        'text':'Выберите перевод слова "переменная"',
        'answers':['variation','variable','changing','variant'] 
        },
    '2':{
        'text':'Хороший?',
        'answers':['Да','Нет','Да нет наверное','Возможно-частично'] 
        }
}

Answers = [1,2,4]

#ТЫ ВОТ ЭТО ДЕЛАЕШЬ >:((((
#Я ЗНАю

question_nums = list(range(0,len(Questions)))

for i in range(len(question_nums)):
    question_nums[i] = str(question_nums[i])
shuffle(question_nums)

were_on = 0

text = QLabel('В каком году канал получил <<золотую кнопку>> от YouTube')
ans_butt = QPushButton('Ответить')

box = QGroupBox('Варианты')

button_1 = QRadioButton('2005')
button_2 = QRadioButton('2010')
button_3 = QRadioButton('2015')
button_4 = QRadioButton('2020')

buttons = [button_1,button_2,button_3,button_4]

group_layout = QHBoxLayout()
left_layout = QVBoxLayout()
center_layout = QVBoxLayout()
right_layout = QVBoxLayout()

left_layout.addWidget(button_1)
left_layout.addWidget(button_2)
right_layout.addWidget(button_3)
right_layout.addWidget(button_4)

group_layout.addLayout(left_layout)
group_layout.addLayout(center_layout)
group_layout.addLayout(right_layout)
box.setLayout(group_layout)


main_layout = QVBoxLayout()
main_layout.addWidget(text, alignment=Qt.AlignCenter)
main_layout.addWidget(box)
main_layout.addWidget(ans_butt, alignment=Qt.AlignCenter)

main_win.setLayout(main_layout)



ans_false_true = QLabel('Правильно/Неправильно')
ans_correct_ans = QLabel('Правильный ответ')
ans_blank = QLabel('')

left_layout.addWidget(ans_false_true)
center_layout.addWidget(ans_correct_ans)
right_layout.addWidget(ans_blank)

ans_false_true.hide()
ans_correct_ans.hide()
ans_blank.hide()

SCORE = 0



def reset_buttons():
        button_1.setAutoExclusive(False)
        button_1.setChecked(False)
        button_1.setAutoExclusive(True)

        button_2.setAutoExclusive(False)
        button_2.setChecked(False)
        button_2.setAutoExclusive(True)

        button_3.setAutoExclusive(False)
        button_3.setChecked(False)
        button_3.setAutoExclusive(True)

        button_4.setAutoExclusive(False)
        button_4.setChecked(False)
        button_4.setAutoExclusive(True)

def show_results():
    if ans_false_true.isHidden():
        global were_on

        ans_false_true.show()
        ans_correct_ans.show()
        ans_blank.show()
        button_1.hide()
        button_2.hide()
        button_3.hide()
        button_4.hide()
        ans_butt.setText('Следующий вопрос')

        right_answer = Answers[int(question_nums[were_on])]

        print(right_answer)

        ans_correct_ans.setText(buttons[right_answer-1].text())

        if get_answer() == right_answer:
            ans_false_true.setText('Правильно!')
            global SCORE
            SCORE += 1
        else:
            ans_false_true.setText('Неправильно!')
        reset_buttons()


        were_on += 1

    else:
        if were_on >= len(question_nums):
            finale()
            return 0
        update_question()
        ans_false_true.hide()
        ans_correct_ans.hide()
        ans_blank.hide()
        button_1.show()
        button_2.show()
        button_3.show()
        button_4.show()
        ans_butt.setText('Ответить')
        

def get_answer():
    if button_1.isChecked():
        return 1
    if button_2.isChecked():
        return 2
    if button_3.isChecked():
        return 3
    if button_4.isChecked():
        return 4

def update_question():
    a = Questions[question_nums[were_on]]

    text.setText(a['text'])
    button_1.setText(a['answers'][0])
    button_2.setText(a['answers'][1])
    button_3.setText(a['answers'][2])
    button_4.setText(a['answers'][3])

def CLOSE_IT():
    main_win.close()

def finale():
    ans_false_true.hide()
    ans_correct_ans.hide()
    ans_blank.hide()
    box.hide()

    button_1.hide()
    button_2.hide()
    button_3.hide()
    button_4.hide()

    text.setText(f'Вы ответили на {SCORE} вопрос(ов) из {len(question_nums)}. Ваш счёт: {int(SCORE/len(question_nums)*100)}')
    ans_butt.clicked.disconnect(show_results)
    ans_butt.clicked.connect(CLOSE_IT)
    ans_butt.setText('Закрыть')


    
# ans_butt.clicked.connect(check_ans)
ans_butt.clicked.connect(show_results)

update_question()

main_win.show()
app.exec_()