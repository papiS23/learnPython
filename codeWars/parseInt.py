def parse_int(string):
    nums = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
        'ten' : 10,
        'eleven' : 11,
        'twelve' : 12,
        'thirteen' : 13,
        'fourteen' : 14,
        'fifteen' : 15,
        'sixteen' : 16,
        'seventeen' : 17,
        'eighteen' : 18,
        'nineteen' : 19,
        'twenty' : 20,
        'thirty' : 30,
        'fourty' : 40,
        'fifty' : 50,
        'sixty' : 60,
        'seventy' : 70,
        'eighty' : 80,
        'ninety' : 90,
        'hundred' : 100,
        'thousand' : 1000,
        'milion' : 1000000
    }
    result = 0
    strNums = string.split()
    for i in range(len(strNums)-1):
        if strNums[i+1] == 'hundred' or strNums[i+1] == 'thousand':
            if '-' in strNums[i]:
                tempNum = nums[strNums[i].split()[0]] + nums[strNums[i].split()[1]]
            else:
                tempNum = nums[strNums[i]]
            result += tempNum * nums[strNums[i+1]]
    return result



##TODO: dokonczyc to gowno

print(parse_int('seven hundred thousand'))