class Parser:
    def __init__(self, input_str):
        self.tokens = input_str.split()
        self.current_token = None
        self.index = 0

    def parse(self):
        self.current_token = self.tokens[self.index]
        self.index += 1
        self.E()

        if self.current_token == '$':
            print("Input successfully parsed.")
        else:
            print("Error: Invalid input.")

    def match(self, expected_token):
        if self.current_token == expected_token:
            if self.index < len(self.tokens):
                self.current_token = self.tokens[self.index]
                self.index += 1
            else:
                self.current_token = '$'  
        else:
            print(f"Error: Expected {expected_token} but found {self.current_token}.")
            exit()

    def E(self):
        self.T()
        if self.current_token == '+':
            self.match('+')
            self.E()

    def T(self):
        self.F()
        if self.current_token == '*':
            self.match('*')
            self.T()

    def F(self):
        if self.current_token == '(':
            self.match('(')
            self.E()
            self.match(')')
        elif self.current_token.isdigit():
            self.match(self.current_token)
        else:
            print("Error: Invalid input.")
            exit()


input_str = input("Enter an arithmetic expression (e.g., '3 + (4 * 5)'):\n")
input_str += ' $'  

parser = Parser(input_str)
parser.parse()
