const captcha = (input) => {
    const inputArray = [...input, input[0]];
    return inputArray.reduce((sum, val, i) => {
        if (parseInt(inputArray[i]) === parseInt(inputArray[i+1])) {
            return parseInt(val) + sum;
            }
        return sum;
    }, 0);
};