import json
from lab3_5 import print_result
from lab3_3 import Unique
from lab3_1 import field
from lab3_2 import gen_random
from lab3_6 import cm_timer_1

path = 'C:/Users/nikar/Desktop/data_light.json'

#with open(path) as f:
#    data = json.load(f)

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name')))


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    gen_salary = list(gen_random(len(arg), 100000, 200000))
    work_and_salary = list(zip(arg, gen_salary))
    return list(map(lambda x: x[0] + ', зарплата ' + str(x[1]) + ' руб', work_and_salary))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))