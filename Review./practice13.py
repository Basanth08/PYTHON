def recursive_func(n, k=3, result=None):
    if result is None:
        result = []
    if k > n:
        return result
    elif k % 3 == 0 and k % 5 != 0:
        result.append(k)
    elif k % 5 == 0 and k % 3 != 0:
        result.append(k)
    return recursive_func(n, k + 1, result)

def helper(array, word):
    for element in array:
        if element == word:
            return True
    return False

def find_words(filename, letter, number):
    words = []
    with open(filename) as f:
        unique = 0
        for word in f.read().lower().split():
            if word[0] == letter and not helper(words, word):
                words.append(word) 
                unique += 1
                if unique == number:
                    return words
        while len(words) < number:
            words.append(None)
    return words

def calendar_month(weekday, num_days):
    calendar = []
    for _ in range(weekday):
        calendar.append(["  "] * 7)

    day = 1
    while day <= num_days:
        week = []
        for _ in range(7):
            if day > num_days:
                week.append("  ")
            else:
                if day < 10:
                    day_str = '0' + str(day)
                else:
                    day_str = str(day)
                week.append(day_str)
                day += 1
        calendar.append(week)
    return calendar


def main():
    print(recursive_func(9))
    print(find_words("atotc.txt", "a", 2))
    print(find_words("atotc.txt", "b", 3))
    print(find_words("atotc.txt", "k", 8))
    print(calendar_month(2, 31)) 
    print(calendar_month(6, 31)) 
if __name__ == "__main__":
    main()
