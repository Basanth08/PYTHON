def make_letter_frequency(filename):
    freq = {}
    with open(filename) as f:
        for line in f:
            for char in line.lower():
                if ord(char) >= ord('a') and ord(char) <= ord('z'):
                    if char in freq:
                        freq[char] += 1
                    else:
                        freq[char] = 1
    return freq

def print_letter_frequency(freq):
    max = 0
    for value in freq:
        print(str(value) + " : " + str(freq[value]))
        if freq[value] > max:
            max = freq[value]
            max_key = value
    print("The most popular letter:", max_key,max)

def main():
    filename = 'data/alice.txt'
    freq = make_letter_frequency(filename)
    print_letter_frequency(freq)
    filename2 = 'data/rit_mission.txt'
    freq_dict = make_letter_frequency(filename2)
    print(freq_dict)
if __name__ == "__main__":
  main()