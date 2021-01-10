import random
import time
import csv
import datetime

def get_min_max_pair():
    while True:
        a_min = input("min of first value: ")
        if a_min.isdigit():
            break

    while True:
        a_max = input("max of first value: ")
        if a_max.isdigit() and int(a_max) >= int(a_min):
            break

    while True:
        b_min = input("min of second value: ")
        if b_min.isdigit():
            break

    while True:
        b_max = input("max of second value: ")
        if b_max.isdigit() and int(b_max) >= int(b_min):
            break

    return a_min, a_max, b_min, b_max

def multiply():
    a_min, a_max, b_min, b_max = get_min_max_pair()

    score = 0
    time_start = time.time()

    for i in range(int(num_qns)):
        a = random.randint(int(a_min), int(a_max))
        b = random.randint(int(b_min), int(b_max))
        ans = input("qn " + str(i + 1) + ": " + str(a) + " * " + str(b) + ": ")
        if ans.isdigit():
            if int(ans) == int(a * b):
                score = score + 1
            else:
                print("correct ans: " + str(a * b))
        else:
            print("correct ans: " + str(a * b))

    return score, time_start


def addition():
    a_min, a_max, b_min, b_max = get_min_max_pair()

    score = 0
    time_start = time.time()

    for i in range(int(num_qns)):
        a = random.randint(int(a_min), int(a_max))
        b = random.randint(int(b_min), int(b_max))
        ans = input("qn " + str(i + 1) + ": " + str(a) + " + " + str(b) + ": ")
        if ans.isdigit():
            if int(ans) == (a + b):
                score = score + 1
        else:
            print("correct ans: " + str(a + b))

    return score, time_start


def division():
    print("first value is the dividend, second value is the divisor")
    dividend_min, dividend_max, divisor_min, divisor_max = get_min_max_pair()

    score = 0

    print("enter answers as [quotient]r[remainder]")
    print("e.g. 6 / 2 : 3r0 || 5 / 2 : 2r1")

    time.sleep(1.5)
    time_start = time.time()

    for i in range(int(num_qns)):
        dividend = random.randint(int(dividend_min), int(dividend_max))
        divisor = random.randint(int(divisor_min), int(divisor_max))
        quotient = dividend // divisor
        remainder = dividend % divisor
        answer = str(quotient) + "r" + str(remainder)
        user_ans = input("qn " + str(i + 1) + ": " + str(dividend) + " / " + str(divisor) + ": ")
        if user_ans == answer:
            score += 1
        else:
            print("correct ans: " + answer)

    return score, time_start


if __name__ == "__main__":
    user = input("enter name of user: ")
    
    operations = ["M", "A", "D"]
    print("enter M for multiplication")
    print("enter A for addition")
    print("enter D for division")
    
    # to check if valid mode
    while True:
        mode = input("mode: ")
        if mode in operations:
            break

    while True:
        num_qns = input("number of questions: ")
        if num_qns.isdigit():
            break

    # generating the questions
    if mode == "M":
        score, time_start = multiply()
    elif mode == "A":
        score, time_start = addition()
    elif mode == "D":
        score, time_start = division()

    # calculating the time
    duration = time.time() - time_start
    ave_time = str(round(duration / int(num_qns), 2)) + "s/qn"

    # printing the stats
    print("score: " + str(score))
    print("time taken: " + str(round(duration, 2)) + " seconds")
    print("average time taken: " + ave_time)

    # write result to file
    with open(user + ".csv", 'a', newline="") as csvfile:
        results = csv.writer(csvfile)
        results.writerow([str(datetime.datetime.now()), mode, str(score) + "/" + str(num_qns), ave_time])
