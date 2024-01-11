def slices(lyric):
    # Append the characters of the lyric to a list
    char_list = list(lyric)
    
    # Initialize variables to keep track of word boundaries
    start = 0
    end = 0
    
    for i in range(len(char_list)):
        # Check if the character is a space
        if char_list[i] == ' ':
            # Slice and print the word using the indices
            word = char_list[start:end]
            if word:  # Check if it's not an empty word (e.g., consecutive spaces)
                print(''.join(word))
            # Update the start index to the next character
            start = i + 1
        end = i + 1  # Update the end index for the next character
    
    # Slice and print the last word (or the only word if there are no spaces)
    word = char_list[start:end]
    if word:
        print(''.join(word))

# Replace this string with your favorite lyric or quote (without leading/trailing spaces)
lyric = "This is a sample lyric or quote"
slices(lyric)
