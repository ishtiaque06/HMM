#The HMM class takes in a sequence of observations and returns the most likely sequence of events that led to the observations made. 

from FSA import *
from FST import *

class HMM():
    def __init__(self, set_of_states, transition_probabilities, observation_likelihoods, sequence_of_observations, starting_observation_probabilities):
        self.set_of_states = set_of_states # Set of states. Analogous to the alphabet of an FSA. It is a list. 
        self.transition_probabilities = transition_probabilities # Dictionary. The key will be the starting and ending state as a tuple and the value will be the probability. 
        self.observation_likelihoods = observation_likelihoods # Dictionary. The key will be the observation and the state and value will be the probability of the observation caused by the state.
        self.start_state = None #These are set to None and will be updated according to the states as provided by the user.
        self.end_state = None #These are set to None and will be updated according to the states as provided by the user.  
        self.sequence_of_observations = sequence_of_observations #The sequence of observations as input by the user. It is a string.
        self.starting_observation_probabilities = starting_observation_probabilities #This is a dictionary. The key is the state that the sequence is most likely to start in and the value is the probability of that happening.

    def check_string_validity(self, string, alphabet): #this function checks whether the observations as defined by the user appear in the possible observation list, which is also defined by the user.
        index = 0
        print string
        print alphabet
        while index < len(string):
            if isinstance(alphabet, dict):
                for observation, hidden_state in alphabet.keys():
                    if string[index] == observation:
                        is_valid = True
                        break
                    else:
                        is_valid = False
            elif isinstance(alphabet, list):
                if string[index] in alphabet:
                    is_valid = True
                else:
                    is_valid = False
            index = index + 1
        return is_valid
    def get_state_sequence_prob(self, sequence_of_states): #Takes in a sequence of states as a string. In the ice cream example, that would be something like "HCCHCHCHCHCCHCHCH"
        if self.check_string_validity(sequence_of_states, self.set_of_states) == True: #this checks if the string has only charactes that belong to the set of states defined. 
            index = 0
            print sequence_of_states
            initial_sequence_probability = max(self.starting_observation_probabilities.values()) #This is the probability of starting at a certain state. 
            while index < (len(sequence_of_states)-1):
                
                self.start_state = sequence_of_states[index]
                self.end_state = sequence_of_states[index+1]
                print self.transition_probabilities[self.start_state, self.end_state]
                initial_sequence_probability = initial_sequence_probability * self.transition_probabilities[self.start_state, self.end_state]
                index = index + 1
            print initial_sequence_probability
        else: 
            return "The states do not match the ones defined in the set of states."
    #I realised a bit late that a bit more work into multiplying the probabilities was required. Also this only multip

    def Viterbi(self): #, self.sequence_of_observations, self.observation_likelihoods
        if self.check_string_validity(self.sequence_of_observations, self.observation_likelihoods) == True: #sequence of observations is a string. observation_likelihoods is a dictionary.
            index_of_sequence_of_observations = 0
            sequence_of_states = ''
            list_of_probabilities = [] #This temporarily stores the list of probabilities of an event happening and chooses the highest probable event between the elements of that list. 
            while index_of_sequence_of_observations < len(self.sequence_of_observations): #This iterates through the sequence of observations.
                for (key, value) in self.observation_likelihoods.items(): #While in an observation, it searches for the most likely state that could've caused that observation.
                    if self.sequence_of_observations[index_of_sequence_of_observations] in key:
                        list_of_probabilities.append(self.observation_likelihoods[key])
                        maximum_probability = max(list_of_probabilities) #This line chooses the most probable state that made the event take place. 
                list_of_probabilities = [] #This resets the list of probabilities for the next observation. 
                for key, value in self.observation_likelihoods.items(): #This part finds out the exact state that caused the observation. Note: it takes into account twice
                                                                        #if two states have the same probability of causing two different observations.
                    if value == maximum_probability and key[0] == self.sequence_of_observations[index_of_sequence_of_observations]:
                        sequence_of_states += key[1]
                index_of_sequence_of_observations += 1
            self.get_state_sequence_prob(sequence_of_states) #after it gets the sequence of states that's the most likely to cause the observation, it calls the get_state_sequence_prob function
                                                             # to find out the total probabilitiy of that sequence of events happening. 
        else:
            print "The sequence of observations is invalid."


def ice_cream_problem():
    Sample_HMM = HMM(['H', 'C', ' '], {(' ', 'H'): 0.8, (' ', 'C'): 0.2, ('H', 'H'): 0.7, ('H', 'C'): 0.3, ('C', 'C'): 0.6, ('C', 'H'): 0.4},
                     {('1', 'H'): 0.2, ('2', 'H'): 0.4, ('3', 'H'): 0.4, ('1', 'C'): 0.5, ('2', 'C'): 0.4, ('3', 'C'): 0.1}, '313', {'H': 0.8, 'C': 0.2})
    Sample_HMM.Viterbi()

ice_cream_problem()


