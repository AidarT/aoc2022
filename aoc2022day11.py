import re
import math

with open('C:/Users/User/Documents/input.txt') as f:
    my_input = list(map(lambda a: a.split('\n'), f.read().split('\n\n')))
f.close()

class monkey:
    def __init__(self, num):
        self.num = int(num)
        self.items = []
        self.new = []
        self.test_div = -1
        self.test_true = -1
        self.test_false = -1
        self.inspected = 0
        self.throw = []
        
    def pullItems(self, items):
        self.items += items
        
    def operationInit(self, op):
        self.new += op
        
    def testDiv(self, div):
        self.test_div = int(div)
        
    def testTrue(self, num_true): 
        self.test_true = int(num_true)
        
    def testFalse(self, num_false):
        self.test_false = int(num_false)    
        
    def inspect(self):
        for item in self.items:
            self.inspected += 1
            if self.new[1] == "old":
                if self.new[0] == "*":
                    w_level = int(item) * int(item)
                elif self.new[0] == "+":
                    w_level = int(item) + int(item)
            elif self.new[0] == "*":
                w_level = int(item) * int(self.new[1])
            elif self.new[0] == "+":
                w_level = int(item) + int(self.new[1])
            w_level = math.floor(w_level / 3)
            if w_level % self.test_div == 0:
                self.throw.append([self.test_true, w_level])
            else:
                self.throw.append([self.test_false, w_level])
        self.items = []
        
    def inspect2(self):
        for item in self.items:
            self.inspected += 1
            if self.new[1] == "old":
                if self.new[0] == "*":
                    w_level = int(item) * int(item)
                elif self.new[0] == "+":
                    w_level = int(item) + int(item)
            elif self.new[0] == "*":
                w_level = int(item) * int(self.new[1])
            elif self.new[0] == "+":
                w_level = int(item) + int(self.new[1])
            if w_level % self.test_div == 0:
                self.throw.append([self.test_true, w_level])
            else:
                self.throw.append([self.test_false, w_level])
        self.items = []
        
monkeys = []
for m in my_input:
    for line in m:
        if line.find('Monkey') != -1:
            m_temp = monkey(re.findall(r'\d+', line)[0])            
            monkeys.append(m_temp)
        if line.find('items') != -1:
            monkeys[-1].pullItems(re.findall(r'\d+', line))
        if line.find('Operation') != -1:
            monkeys[-1].operationInit(line.split('old ')[1].split(' '))
        if line.find('Test') != -1:
            monkeys[-1].testDiv(re.findall(r'\d+', line)[0])
        if line.find('true') != -1:
            temp = re.findall(r'\d+', line)[0]
            monkeys[-1].testTrue(re.findall(r'\d+', line)[0])
        if line.find('false') != -1:
            monkeys[-1].testFalse(re.findall(r'\d+', line)[0])

for i in range(0,20):
    for m in monkeys:
        m.inspect()
        for num, item in m.throw:
            monkeys[num].pullItems([item])
        m.throw = []

part1 = sorted([m.inspected for m in monkeys])
part1 = part1[-1] * part1[-2]

monkeys = []
for m in my_input:
    for line in m:
        if line.find('Monkey') != -1:
            m_temp = monkey(re.findall(r'\d+', line)[0])
            monkeys.append(m_temp)
        if line.find('items') != -1:
            monkeys[-1].pullItems(re.findall(r'\d+', line))
        if line.find('Operation') != -1:
            monkeys[-1].operationInit(line.split('old ')[1].split(' '))
        if line.find('Test') != -1:
            monkeys[-1].testDiv(re.findall(r'\d+', line)[0])
        if line.find('true') != -1:
            temp = re.findall(r'\d+', line)[0]
            monkeys[-1].testTrue(re.findall(r'\d+', line)[0])
        if line.find('false') != -1:
            monkeys[-1].testFalse(re.findall(r'\d+', line)[0])

for i in range(0,10000):
    for m in monkeys:
        m.inspect2()
        for num, item in m.throw:
            monkeys[num].pullItems([item])
        m.throw = []

part2 = sorted([m.inspected for m in monkeys])
part2 = part1[-1] * part1[-2]

print(str(part1) + " " + str(part2))