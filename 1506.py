'''def strcounter(s): # O (N*M) = 36
    for sym in set(s): # set - функция приведения к множеству
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1
        print(sym,count)
strcounter('abcnra')

def strcounter(s): # O (N^2) = 36
    for sym in s:
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1
        print(sym,count)
strcounter('abcnra')'''

a = input('Введите слово на проверку: ').lower()
def f(a):
    b = a[::-1].lower()
    if b == a:
        print(True)
    else:
        print(False)
