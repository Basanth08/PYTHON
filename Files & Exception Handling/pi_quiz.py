def pi_tester():
    # The pi value upto 100 decimals in the given question is:
    value_of_pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    #initializing
    correct_digit = 0
    maximum_digits = min(len(value_of_pi), 100)

    for i in range(maximum_digits):
        input_promt = input("Enter the digits in a sequence that matches the value of pi:")
        digit_exp = value_of_pi[i]

        if input_promt == digit_exp:
            correct_digit = correct_digit + 1
        else:

def display_score(score):
    if score >= 0 and score <= 4:
        title_is = "PI Neophyte"
    elif score >= 5 and score <= 9:
        title_is = "PI Novice"
    elif score >= 10 and score <= 24:
        title_is = "PI Journeyman"
    elif score >= 25 and score <= 49:
        title_is = "PI Enthusiast"
    elif score >= 50 and score <= 96:
        title_is = "PI Connoisseur"
    elif score >= 97 and score <= 100:
        title_is = "PI Expert"
    else:
        title_is = "PI Imposter (this state is only reachable if there is an error in the code)"
    
 

def main():
   


 if __name__ == "__main__":
    main()