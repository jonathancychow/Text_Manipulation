import math
word_tens = {}
word_tens[2] = 'twenty'
word_tens[3] = 'thirty'
word_tens[4] = 'forty'
word_tens[5] = 'fifty'
word_tens[6] = 'sixty'
word_tens[7] = 'seventy'
word_tens[8] = 'eighty'
word_tens[9] = 'ninety'

word = {}
word[1] = 'one'
word[2] = 'two'
word[3] = 'three'
word[4] = 'four'
word[5] = 'five'
word[6] = 'six'
word[7] = 'seven'
word[8] = 'eight'
word[9] = 'nine'
word[10] = 'ten'
word[11] = 'eleven'
word[12] = 'twelve'
word[13] = 'thirteen'
word[14] = 'fourteen'
word[15] = 'fifteen'
word[16] = 'sixteen'
word[17] = 'seventeen'
word[18] = 'eighteen'
word[19] = 'nineteen'


def num_letter_sum(number):
    sum_answer = 0
    n = 1
    while n <= number:
    # the following will hold from 99 to 1
        if n >19:
            # number below 100
            # math.floor(n / 10) * 10
            if n % (math.floor(n / 10) * 10) >0: # divied by 20,30,40
                # between 9 and 1
                sum_answer = sum_answer + len(word[n % (math.floor(n / 10)*10)])
            else:
                # 10
                sum_answer = sum_answer + len(word_tens[math.floor(n/10)])


        if n<=19:
            # Able to find from 19 to 1
            sum_answer = sum_answer + len(word[n])

        n += 1
    return sum_answer

# one hundred
num_letter_sum(36)