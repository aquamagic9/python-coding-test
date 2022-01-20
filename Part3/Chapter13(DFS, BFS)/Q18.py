from collections import deque

#문자열 분리 => 균형잡힌 괄호 문자열, 나머지 문자열 반환
def separate(inp):
    open_p = 0
    close_p = 0
    for parentheses in inp:
        if parentheses == '(':
            open_p += 1
        elif parentheses == ')':
            close_p += 1
        if open_p == close_p:
            return inp[0:open_p + close_p], inp[open_p + close_p:len(inp)]

#올바른 괄호 문자열인지 반환
def is_correct(inp):
    stk = deque()
    for parentheses in inp:
        if parentheses == '(':
            stk.append('(')
        elif parentheses == ')':
            if len(stk) == 0:
                return False
            stk.pop()
    if len(stk):
        return False
    return True


def func(inp):
    if inp == '':
        return ''
    balanced, remained = separate(inp)
    if is_correct(balanced):
        return balanced + func(remained);
    else:
        #앞, 뒤 1칸씩 자르기
        balanced = balanced[1:len(balanced) - 1]
        # 괄호 뒤집기
        balanced = balanced.replace('(', '*')
        balanced = balanced.replace(')', '(')
        balanced = balanced.replace('*', ')')
        return '(' + func(remained) + ')' + balanced


inp = input()
print(func(inp))
