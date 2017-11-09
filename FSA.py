'''The FSA class takes in a string, the alphabet represented as a list to go with the string, states and the transition function which is represented as a dictionary.
    
'''
class FSA(): 
    def __init__(self, string, alphabet, set_of_states, initial_states, final_states, transition_function):
        #variable assignments to use throughout the class
        self.alphabet = alphabet
        self.set_of_states = set_of_states
        self.initial_states = initial_states
        self.final_states = final_states
        self.transition_function = transition_function
        self.string = string

    def check_string_validity(self): #This method checks if the characters in the string provided are present in the alphabet that's provided along with it.
        index = 0 #this index is used to iterate through the string to match every character with the alphabet provided.
        while index < len(self.string):
            if self.string[index] in self.alphabet: #Searches for the character in the alphabet provided
                index = index + 1
            else: #If the character is not found in the alphabet, the whole string provided is invalid in terms of the alphabet provided. 
                return False
        return True

    def transition(self): #This is the function which does the actual transition between states as given by the transition function provided in the input. 
        if self.check_string_validity() == True: #If the string matches the alphabet, then
            index = 0
            while index < len(self.string): #iterates through the string
                self.final_states = self.get_transition(self.initial_states, self.string[index]) #and calls the get_transition function to change the state of the FSA.
                self.initial_states = self.final_states #Updates the initial states to the latest state before the loop is iterated again. 
                index = index + 1 
            print self.final_states #After the looping is done, the function prints the ending state to the user. 
        else:
            print "Invalid string"
        
    def get_transition(self, state, symbol):
        return self.transition_function[state, symbol]

def demo_FSA(): #This demo returns 1 if the string has an odd number of a's.
    Sample_FSA = FSA('aaaabbbbbbbbbbbbbbbbaabbaaaaaaa', ['a', 'b'], [0, 1], 0, 1, {(0, 'a'): 1, (1, 'b'): 1, (1, 'a'): 0, (0, 'b'): 0})
    Sample_FSA.transition()

demo_FSA()