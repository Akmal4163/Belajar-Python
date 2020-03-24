# mendefinisikan fungsi
def function():
    print('this is function')


# memanggil fungsi
function()
function()
function()
function()
function()


def whitespace1():
    print('=' * 50)


whitespace1()


# membuat fungsi sederhana
def colors():
    print("yellow", "blue", "red", "green", "violet", "white", "black")


def colorgrading():
    print('the colors is')
    colors()


whitespace1()


def voices():
    print('abcdefghij')


def prices():
    voices()
    print('the voices prices is 20000')


# arguments function
print('arguments function')


def totalprices(idr):
    voices()
    prices = 2000
    totalprices = idr * prices
    print('this prices', idr, 'is', totalprices)


totalprices(200)
totalprices(0.5)
whitespace1()

colorgrading()
whitespace1()


# input fungsi dengan argumen
def totalcolorgrading(kg):
    colorgrading()
    color = 2000
    totalcolor = kg * color
    print('total color is', kg, 'color is', totalcolor)


totalcolorgrading(4)
totalcolorgrading(10)
totalcolorgrading(5.5)
# function with arguments
whitespace1()


def students(name):
    print('the student name is', name)


students('mario')


# fungsi dengan keyword arguments
def teachers(name, study):
    print('the name of teachers is:', name, )
    if name is 'bob':
        print('he teaches:', study)
    elif name is 'lisa':
        print('she teaches:', study)
    else:
        print("we don't found this name")


teachers(name='bob', study='science')
teachers(name='lisa', study='art')


def znumbers(numbers, command):
    print('numbers searching', numbers)
    for numbers in znumbers:
        print('numbers searching')
        if numbers is 20:
            print('you found a match numbers', numbers)
    if command is 'search':
        print('please wait')


znumbers(numbers=20, command='search')


def result(argumen1):
    print('the result is', argumen1*2)


result(34)
def luas_segitiga(alas, tinggi):
    luas = (alas*tinggi) /2
    print('segitiga ini luasnya adalah:',luas)
luas_segitiga(alas='34', tinggi='56')
print(luas_segitiga)