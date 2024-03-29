class FiniteStateAutomaton:
    def __init__(self):
        self.current_state = 'start'

    def transition(self, input_symbol):
        if self.current_state == 'start':
            if input_symbol == 'a':
                self.current_state = 'state_a'
            else:
                self.current_state = 'start'
        elif self.current_state == 'state_a':
            if input_symbol == 'b':
                self.current_state = 'final_state'
            else:
                self.current_state = 'start'
        elif self.current_state == 'final_state':
            self.current_state = 'start'

    def recognize_string(self, input_string):
        for symbol in input_string:
            self.transition(symbol)

        return self.current_state == 'final_state'


def main():
    automaton = FiniteStateAutomaton()
    input_string = input("Enter a string to check if it ends with 'ab': ")

    if automaton.recognize_string(input_string):
        print("The string ends with 'ab'.")
    else:
        print("The string does not end with 'ab'.")

if __name__ == "__main__":
    main()
