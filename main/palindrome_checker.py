from collections import deque

# specifies that 's' is the accepted parameter that should be a string (str), and also shows the function should return a bool (-> bool)
def is_palindrome(s: str) -> bool:
    # convert string to lower case
    s_lower = s.lower()

    # empty list for alpha numerical characters
    alpha_num_char = []

    # iterate over each lower case letter

    for char in s_lower:
        # check if each letter is alpha numerical
        if char.isalnum():
            # append alpha numerical char to list
            alpha_num_char.append(char)

    # join characters in list into a single string
    cleaned_s = ''.join(alpha_num_char) # the '' makes it so characters are directly concatenated as opposed to ' '

    # initialize queue
    queue = deque(cleaned_s)

    # check if string is palindrome

    while len(queue) > 1:
        front = queue.popleft()
        back = queue.pop()
        if front != back:
            return False
    return True

