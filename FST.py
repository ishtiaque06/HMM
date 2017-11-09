'''The FST class takes in a string and returns the corresponding output string based on the function that changes the input string to the output string. The function
is also provided by the user.
'''
class FST():
    def __init__(self, string, input_alphabet, output_alphabet, set_of_states, initial_states, final_states, transition_function):
        self.input_string = string #input string as provided by the user
        self.output_string = '' #output string corresponding to the input string
        self.input_alphabet = input_alphabet #input alphabet as provided by the user
        self.output_alphabet = output_alphabet #output alphabet as provided by the user
        self.set_of_states = set_of_states #set of possible states the FST can have
        self.initial_states = initial_states #initial states as input by the user
        self.final_states = final_states #final states as defined by the user
        self.transition_function = transition_function #transition function provided by the user, assuming it is in a dictionary form of the format as described in class.

    def check_string_validity(self): #this function iterates through the input string and decides whether all the characters in the string appear in the alphabet defined.
        index = 0
        while index < len(self.input_string):
            if self.input_string[index] in self.input_alphabet:
                is_valid = True
                index = index + 1
            else:
                return False
        return True

    def transition(self): #This is the transition function itself, which calls upon the get_transition function updates the state of the FST and the output string with the values returned by the get_transition function.
        if self.check_string_validity() == True:
            index = 0
            while index < len(self.input_string):
                self.output_string += self.get_transition(self.initial_states, self.input_string[index])[0]
                self.final_states = self.get_transition(self.initial_states, self.input_string[index])[1]
                self.initial_states = self.final_states
                index = index + 1
            print self.output_string, ", ", self.final_states #After the final state and the output string is ready, it prints those two to the user. 
        else:
            print "Invalid string"

    def get_transition(self, state, symbol): #this get_transition function takes in a state and symbol as key for a dictionary and outputs the state and symbol as the value. 
        transition_relation = self.transition_function
        return transition_relation[state, symbol]

def demo_FST():#This demo changes a in a string to b and b to a
    Sample_FST = FST('aaabbbbbbabababababababababaaaa', ['a', 'b'], ['a', 'b'], [0, 1], 0, 1, {(0,'b'): ('a',0), (0,'a'): ('b',1), (1,'a'): ('b',1), (1,'b'): ('a',1)})
    Sample_FST.transition()

demo_FST()