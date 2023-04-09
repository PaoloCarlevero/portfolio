from src.Stack import Stack
import re

class Dijkstra:

    def __init__(self):
        self.values_stack = Stack()
        self.operators_stack = Stack()
        self.operator_precedence = {'+': 0, '-': 0, '*': 1, '/': 1}  
        
    
    def solve(self, expression: str):

        items = re.findall(r'[+-/*//()]|\d+', expression)

        for item in items:
            if item.isnumeric():
                self.values_stack.push(item)
            elif item == '(':
                self.operators_stack.push('(')
            elif item == ')':
                while True:
                    operator = self.operators_stack.pop()
                    if operator == '(':
                        break
                    first_num = self.values_stack.pop()
                    second_num = self.values_stack.pop()
                    self.values_stack.push(eval(f'{second_num}{operator}{first_num}'))
            else:
                while (     self.operators_stack.is_full
                        and not self.operators_stack.top == '('
                        and self.operator_precedence[item] <= self.operator_precedence[self.operators_stack.top]
                    ):
                    operator = self.operators_stack.pop()
                    first_num = self.values_stack.pop()
                    second_num = self.values_stack.pop()
                    self.values_stack.push(eval(f'{second_num}{operator}{first_num}'))
                self.operators_stack.push(item)

        while not self.operators_stack.is_empty:
            operator = self.operators_stack.pop()
            first_num = self.values_stack.pop()
            second_num = self.values_stack.pop()
            self.values_stack.push(eval(f'{second_num}{operator}{first_num}'))

        return self.values_stack.pop()