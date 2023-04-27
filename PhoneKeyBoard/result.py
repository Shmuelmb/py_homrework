def phoneKeyBoard(digits):
    numAndLetters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if not digits:
        return []
    result = ['']
    for digit in digits:
        letters = numAndLetters[digit]
        new_result = []
        for letter in letters:
            for combination in result:
                new_result.append(combination + letter)
        result = new_result
    return result


print(phoneKeyBoard('8924'))
