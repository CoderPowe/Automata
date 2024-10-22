import csv
class Machine:
    def __init__(self, states, alphabets, data, finalStates):
        self.table = data
        self.states = states
        self.alphabets = alphabets
        self.startState = states[0]
        self.finalStates = finalStates
    def test(self, input):
        currentState = self.startState
        for a in input:
            row = self.table[self.states.index(currentState)] 
            nextState = row[self.alphabets.index(a)+1]
            currentState = nextState
        return (currentState in self.finalStates)
if __name__ == "__main__":
        with open("table.csv", "r") as f:
            csv_data = csv.reader(f)
            data = list(csv_data) 
        states = []
        for row in data[1:]:
            states.append(row[0])
        finalStates = []
        for state in states:
            if state[0] == "*":
               finalStates.append(state[1:])
               states[states.index(state)] = state[1:]
        alphabets = data[0][1:]
        data = data[1:]
        machine = Machine(states, alphabets, data, finalStates)
        with open("input.txt", "r") as f:
            inputs = f.readlines()
        for input in inputs:
            mes = "Accepted" if machine.test(input[:len(input)-1]) else "Rejected"
            print(f"{input[:len(input)-1]} -> {mes}")