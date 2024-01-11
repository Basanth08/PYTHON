import timing
def hash_first_char(a_string):
    if not a_string:
        return 0
    return ord(a_string[0])

def hash_sum(a_string):
    total = 0
    for char in a_string:
        total = total + ord(char)
    return total

def hash_positional_sum(a_string):
    total = 0
    pow = len(a_string)-1
    for char in a_string:
        total = total + ord(char) * 31 ** pow
        pow = pow - 1
    return total

def build_collision_counter(hash_func):
    collision_counter = {}
    with open('data/long_line_words.txt') as file:
        for line in file:
            hash = hash_func(line.strip())
            if hash in collision_counter:
                collision_counter[hash] += 1
            else:
                collision_counter[hash] = 1
    return collision_counter

def hash_test(collision_counter, hash_func):
    print("Hash Function:", hash_func.__name__)
    total_collisions = 0
    tot_line = 0
    for hash_code in collision_counter:
        count = collision_counter[hash_code]
        total_collisions += count - 1
        tot_line += count
    maximum_collisions = 0
    for count in collision_counter:
        if count > maximum_collisions:
            maximum_collisions = count
    print("Maximum collisions:", maximum_collisions)
    num_unique_hashes = 0
    for hash_code in collision_counter:
        num_unique_hashes += 1
    spread = num_unique_hashes / tot_line
    print("Spread in %:", round(spread * 100, 2))

def main():
    s1 = "Hello  People"
    s2 = "Basanth Varaganti"
    hash1 = hash_first_char(s1)
    hash2 = hash_first_char(s2)
    print(hash1)
    print(hash2)
    hash3 = hash_sum(s1)
    hash4 = hash_sum(s2)
    print(hash3)
    print(hash4)
    s3 = "abcd"
    s4 = "bdca"
    hash5 = hash_positional_sum(s3)
    hash6 = hash_positional_sum(s4)
    print(hash5)
    print(hash6)
    hash_funcs = [hash, hash_first_char, hash_sum, hash_positional_sum]
    for func in hash_funcs:
        collisions = build_collision_counter(func)
    hash_test(collisions, func)
    print()

if __name__ == "__main__":
    main()