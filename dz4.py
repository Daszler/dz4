# Напишите функцию для транспонирования матрицы
def matrix(start_matrix:list[list[int]]) -> list[list[int]]:
    new_matrix=[]
    for row in range(len(start_matrix[0])):
        new_matrix.append(list())
        for elem in range(len(start_matrix)):
            new_matrix[row].append(start_matrix[elem][row])
    return new_matrix


def PRINT(mass:list[list[int]])->None:
    for row in mass:
        for elem in row:
            print(elem, end=' ')
        print()



if __name__=='__main__':
    st_matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Исходная матрица:")
    PRINT(st_matrix)
    print("Результирующая матрица:")
    PRINT(matrix(st_matrix))

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def function(**kwargs)->dict:
    res_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ == None:
            value = str(value)
        res_dict[value] = key
    return res_dict


if __name__=='__main__':
    print(function(first=1,second="слово",third=(1,2,3,4,6,8),fourth={1,2,3,4,6,8},fifth=[10,4,2,3,6,8],sixth=""))

"""Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список."""





"""Используем int тк есть условие кратности 50"""


import decimal
def bank()->bool:
    flag=1

    global SCORE
    tmp_score=SCORE
    global COUNT
    COUNT+=1
    print("Операция №: "+ str(COUNT))
    tmp_score=Million(tmp_score)
    operation = question()

    if operation == "1":
        cash = cash_check()
        SCORE=add_cash(cash,tmp_score,COUNT)
        flag=1

    elif operation == "2":
        cash = cash_check()
        SCORE=give_cash(cash,SCORE,COUNT)
        flag=1
    elif operation == "3":
        print(f"Ваши операции:{operations}")
        flag=0
    else:
        print("Введите 1,2 или 3")
        bank()
    return flag

def question()->int:
    operation = input("Введите номер действия 1-пополнить, 2-снять, 3-выйти: ")
    return operation

def give_cash(cash:decimal,score:decimal,count:int)->decimal:
    global operations
    persent=give_cash_persent(cash)
    flag=proverka(cash,score,persent)
    if count%MAX_COUNT==0:
        tmp=score*EXTRA_PERSENT
        score_new=score+tmp
        minus=cash+persent
        score=score_new-minus
        operations.append(f"-{cash}")
    else:
        score = score - cash-persent
        operations.append(f"-{cash}")

    print(score)
    return score
def give_cash_persent(cash:decimal)->decimal:
    tmp_persent=cash*PERSENT
    if tmp_persent<=MIN_CASH:
        persent=MIN_CASH
    elif tmp_persent>=MAX_CASH:
        persent=MAX_CASH
    else:
        persent=tmp_persent
    return persent

def add_cash(cash:decimal,score:decimal,count:int)->decimal:
    global operations
    if count%MAX_COUNT==0:
        tmp=score*EXTRA_PERSENT
        score=score+tmp+cash
        operations.append(f"+{cash}")
    else:
        score = score + cash
        operations.append(f"+{cash}")

    print(score)
    return score

def cash_check()->decimal:
    while True:
        temp=int(input("Введите сумму: "))
        if not temp%MULT==0:
            print("Сумма должна быть кратна 50! ")
        else:
            cash=temp
            break
    return cash

def Million(score:decimal)->decimal:
    if score>MAX_SCORE:
        tmp=score-(score*RICH_PERSENT)
    else:
        tmp=score
    return tmp

def proverka(cash:decimal,score:int,persent:decimal)->bool:
    if score< (cash+persent):
        print("Нельзя снять больше,чем на карте!")
        global COUNT
        COUNT=COUNT-1
        bank()
    else:
        return True


if __name__=='__main__':
    global MULT
    MULT = 50
    global MIN_CASH
    MIN_CASH = 30
    global MAX_CASH
    MAX_CASH = 600
    global MAX_COUNT
    MAX_COUNT = 3
    global PERSENT
    PERSENT = 0.015
    global EXTRA_PERSENT
    EXTRA_PERSENT = 0.03
    global RICH_PERSENT
    RICH_PERSENT = 0.1
    global MAX_SCORE
    MAX_SCORE = 5_000_000
    COUNT = 0
    global SCORE
    SCORE = 0
    global operations
    operations=[]



    bank_q = bank()
    while bank_q != 0:
        bank()
        bank_q = bank()
    if bank_q == 0:
        print("сумма= " + str(SCORE))


"""Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце."""


def function(data:list[str])->list[str]:
    temp = []
    for i in range(len(data)):
        if data[i][-1:]=="s" and len(data[i])!=1:
            temp.append(data[i])
            data[i] = None

    for i in range (len(temp)):
        data.append(temp[i])

    return data


if __name__=='__main__':
    new_data=["s", "task", "song", "parts", "friends", "374586940","qwertys","123"]
    print(function(new_data))