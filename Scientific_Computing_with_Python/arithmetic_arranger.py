def arithmetic_arranger(problems, should_show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    top_num = []
    operator = []
    bottom_num = []

    # Sort into separate lists
    for problem in problems:
        if '/' in problem:
            return "Error: Operator must be '+' or '-'."
    
        current_problem = problem.split(' ')

        if len(current_problem[0]) > 4 or len(current_problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            int(current_problem[0])
            int(current_problem[2])
        except:
            return "Error: Numbers must only contain digits."

        top_num.append(current_problem[0])
        operator.append(current_problem[1])
        bottom_num.append(current_problem[2])

    #Build out the strings
    top_str = ''
    middle_str = ''
    bottom_str = ''
    answer_str = ''
    DIVIDING_SPACES = ' '*4

    for i in range(len(problems)):
        top_num_str = top_num[i]
        bottom_num_str = bottom_num[i]
        top_num_int = int(top_num_str)
        bottom_num_int = int(bottom_num_str)
        num_top_digits = len(top_num_str)
        num_bottom_digits = len(bottom_num_str)
        char_per_prob_line = max(num_top_digits,num_bottom_digits) + 2

        top_str += ' '*(char_per_prob_line-num_top_digits)
        top_str += top_num[i]

        middle_str += operator[i]
        middle_str += ' '*(char_per_prob_line-1-num_bottom_digits)
        middle_str += bottom_num[i]

        bottom_str += '-'*char_per_prob_line

        if should_show_answers:
            if operator[i] == '+':
                answer = top_num_int + bottom_num_int
            else:
                answer = top_num_int - bottom_num_int
            answer_str += ' '*(char_per_prob_line-len(str(answer)))
            answer_str += str(answer)

        if i < len(problems)-1:
            top_str += DIVIDING_SPACES
            middle_str += DIVIDING_SPACES
            bottom_str += DIVIDING_SPACES
            if should_show_answers:
                answer_str += DIVIDING_SPACES


    
    top_str += '\n'
    middle_str += '\n'

    if should_show_answers:
        bottom_str += '\n'
        return top_str + middle_str + bottom_str + answer_str
    else:
        return top_str + middle_str + bottom_str