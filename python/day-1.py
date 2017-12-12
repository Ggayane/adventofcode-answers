inputFile = __file__.replace('py', 'txt')

def getInput(fileName):
    with open(fileName) as f:
        return f.readline()

def captchaCalc():
    sum = 0
    input = getInput(inputFile)
    input += input[0]
    for i in range(len(input) - 1):
        if input[i] == input[i+1]:
            sum += int(input[i])
    return sum



print(captchaCalc())