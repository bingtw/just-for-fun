
def get_new_input(input_str, max_count, count, start_index):

    if count >= max_count:
        return input_str

    if (start_index + 1) >= len(input_str):
        # all character had been traversed
        # remove the last characters at right hand side
        remaining_count = max_count - count
        final_index = len(input_str) - remaining_count
        return input_str[:final_index]

    current_char = input_str[start_index]
    next_char = input_str[start_index + 1]
    if current_char < next_char:
        # remove current index char
        input_str = input_str[:start_index] + input_str[start_index + 1:]
        count = count + 1
    else:
        # bypass current index char since it's greater that next one
        start_index = start_index + 1
    return get_new_input(input_str, max_count, count, start_index)

if __name__ == '__main__':
    print('haha')
    input_str = input('Please input a number: ')
    print('Your input:', input_str)
    max_delete_count = 3
    input_str = get_new_input(input_str, max_delete_count, 0, 0)

    print('Final Result:', input_str)

