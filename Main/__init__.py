    
class differenceEquation:
    def __init__(self, inputCoeffs, outputCoeffs):
        self.inputCoeffs = inputCoeffs
        self.outputCoeffs = outputCoeffs
        self.oldInputs = [0 for i in range(len(inputCoeffs)-1)]
        self.oldOutputs = [0 for i in range(len(outputCoeffs))]
    
    def stepList(self, inputList):
        outputs = []
        for inp in inputList:
            outputs.append(self.step(inp))
        return outputs
    
    def step(self, inp):
        result = 0
        
        #print
        #print "Stepping with input = %i" % inp
        #print "Old Inputs: %r" % self.oldInputs
        #print "Old Outputs: %r" % self.oldOutputs
        
        for i in range(len(self.inputCoeffs)):
            if(i == 0):
                result = result + self.inputCoeffs[i] * inp
            else:
                result = result + self.inputCoeffs[i] * self.oldInputs[i-1]
                
        for i in range(len(self.outputCoeffs)):
            result = result + self.outputCoeffs[i] * self.oldOutputs[i]
        
        if(len(self.oldInputs) > 0):
            temp = [0 for i in range(len(self.oldInputs))]
            temp[0] = inp
            for i in range(1, len(self.oldInputs)):
                temp[i] = self.oldInputs[i-1]
            self.oldInputs = temp
        
        if(len(self.oldOutputs) > 0):
            temp = [0 for i in range(len(self.oldOutputs))]
            temp[0] = result
            for i in range(1, len(self.oldOutputs)):
                temp[i] = self.oldOutputs[i-1]
            self.oldOutputs = temp
        
        return result

dif = differenceEquation([0, 1], [1, 1])
print dif.stepList([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])

