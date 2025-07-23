from browser import document, window


QUESTIONS = {
    0: ('Delphi', 1, 'Хотите много зарабатывать?'),
    1: (2, 6, 'Вы тупой?'),
    2: (3, 5, 'Вы инженер?'),
    3: ('C', 4, 'У вас есть ноги?'),
    4: ('C++', 'Java', 'Они вам нужны?'),
    5: ('MatLab', 'Fortran', 'Вам больше 50?'),
    6: (7, 10, 'Очень?'),
    7: (8, 'Python', 'Вы насмотрелись<br>уроков ХАУДИ ХО?'),
    8: (9, 'C#', 'Вам нравится Windows?'),
    9: ('Perl', 'Swift', 'Вы пи**р?'),
    10: ('PHP', 11, 'У вас есть друзья?'),
    11: ('Ruby', 'JavaScript', 'Они тоже тупые?'),
}


state = {'question': 0}
message_element = document['message']
buttons_tab = document['buttons']
button_no = document['button_no']
button_yes = document['button_yes']
reset_tab = document['reset_tab']
button_reset = document['button_reset']


def answer(index):
    question = QUESTIONS[state['question']]
    value = question[index]

    if isinstance(value, int):
        state['question'] = value
        message_element.innerHTML = QUESTIONS[state['question']][2]
        return

    buttons_tab.style.display = 'none'
    reset_tab.style.display = 'table-row'
    message_element.innerHTML = f'Ваш язык: {value}!'


button_no.bind('click', lambda event: answer(0))
button_yes.bind('click', lambda event: answer(1))
button_reset.bind('click', lambda event: window.location.reload())

message_element.textContent = QUESTIONS[state['question']][2]
