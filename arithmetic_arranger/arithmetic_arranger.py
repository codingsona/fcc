""" Class and Functions"""
'''Created a function for the arithmetic arrangement. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.'''
def arithmetic_arranger(problems, status=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    line_a = ''
    line_b = ''
    line_c = ''
    line_d = ''

    '''Iterating through problems and splitting them'''
    for i, problem in enumerate(problems):
        n1, op, n2 = problem.split()
        l1, l2 = len(n1), len(n2)

        '''Situations that will return an error:'''
        if op not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if not (n1.isdigit() and n2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if l1 > 4 or l2 > 4:
            return 'Error: Numbers cannot be more than four digits.'

        spacing = max(l1, l2)
        result = int(n1) + int(n2) if op == '+' else int(n1) - int(n2)

        line_a = line_a + n1.rjust(spacing + 2)
        line_b = line_b + op + n2.rjust(spacing + 1)
        line_c = line_c + ''.rjust(spacing + 2, '-')
        line_d = line_d + str(result).rjust(spacing + 2)

        '''According to the README.md ,there should be four spaces between each problem.'''
        if i < len(problems) - 1:
            line_a += '    '
            line_b += '    '
            line_c += '    '
            line_d += '    '

    # print(status)
    if status:
        arranged_problems = line_a + '\n' + line_b + '\n' + line_c + '\n' + line_d
    else:
        arranged_problems = line_a + '\n' + line_b + '\n' + line_c
    return arranged_problems
