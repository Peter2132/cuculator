import math

def summa (first, second):

    return first + second

def sub (first, second):

    return first - second

def mult (first, second):

    return first * second

def div (first, second):

    return first / second

def calc(first, second, oper):

    result = None

    if oper == '+':

        result = summa(first, second)

    elif oper == '-':

        result = sub(first, second)

    elif oper == '*':

        result = mult(first, second)

    elif oper == '/':

        if (second == 0):

            print('Ошибка!')

            return

        result = div(first, second)

    elif oper == '%':

        result = first / second * 100

    elif oper == '**':

        result = first ** second
    
    elif oper == '√':
        
        result = math.sqrt(first)

    elif oper == '!':

        result = math.factorial(first)
    
    elif oper == 'sin':

        result = math.sin(first)

    elif oper == 'cos':

        result = math.cos(first)
    
    elif oper == 'tan':

        result = math.tan(first)

    else:

        print('Такого действия не существует!')

    return result

def operation():

    mes = input('Выберите операцию (Введите +, -, *, /, %, **, √, !, sin, cos, tan):\n '

     '+ - сложение двух чисел\n'

     '- - вычитание двух чисел\n'

     '* - умножение двух чисел\n'

      '/ - деление двух чисел\n'

       '% - процент первого числа от второго\n'

       '** - возведение первого числа в степень второго\n'
                
     '√ - квадратный корень первого числа\n'
                
     '! - факториал первого числа\n'
                
      'sin - синус первого числа\n'
                
      'cos - косинус первого числа\n'
                
      'tan - тангенс первого числа\n')       

    if mes == '+':

        print('Вы выбрали сумму')

    elif mes == '-':

        print('Вы выбрали разность')

    elif mes == '*':

        print('Вы выбрали умножение')

    elif mes == '/':

        print('Вы выбрали деление')

    elif mes == '%':

        print('Вы выбрали нахождение процента первого числа от второго')

    elif mes == '**':

        print('Вы выбрали возведение в степень')

    elif mes == '√':

        print('Вы выбрали квадратный корень первого числа')
    
    elif mes == '!':

        print('Вы выбрали факториал первого числа')

    elif mes == 'sin':

        print('Вы выбрали синус первого числа')

    elif mes == 'cos':

        print('Вы выбрали косинус первого числа')

    elif mes == 'tan':

        print('Вы выбрали тангес первого числа')
    
    correct_operations = ['+', '-', '*', '/', '%', '**', '√', '!', 'sin', 'cos', 'tan']

    while mes not in correct_operations:

        print('Выбранной операции не существует!')

        mes = input()
    return mes

def run():

    try:

        first = int(input('Введите первое число: '))

    except ValueError:

        first = int(input('Такого числа не существует!'))

    try:

        second = int(input('Введите второе число: '))

    except ValueError:

        second = int(input('Такого числа не существует!'))

    op = operation()

    result = calc(first, second, op)

    print(f'Результат: {result}')

progam_is_running = True

while(progam_is_running):

    run()

    answer = input('Работать дальше?\n'' Введите r если да , если нет Enter: ')

    if answer != 'r':

        progam_is_running = False