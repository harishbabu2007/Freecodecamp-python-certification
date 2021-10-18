def arithmetic_arranger(problems, print_out=False):
    #Rule
    if len(problems) > 5:
        return "Error: Too many problems."
    #Rule

    output = ["","","",""]


    #lexification
    term_array = []

    for i in range(len(problems)):
        term_array.append(problems[i].split(" "))
    #lexification

    #main_Logic
    for i in range(len(term_array)):
        term1 = term_array[i][0]
        operator = term_array[i][1]
        term2 = term_array[i][2]

        # Rules
        if operator!='+':
            if operator!='-':  
                return "Error: Operator must be '+' or '-'."

        try:
            test_t1 = int(term1)
            test_t2 = int(term2)
        except:
            return "Error: Numbers must only contain digits."

        if len(term1)>4 or len(term2)>4:
            return "Error: Numbers cannot be more than four digits."
        #Rules

        n_term1 = int(term1)
        n_term2 = int(term2)

        result = ""

        if operator == "+":
            result = str(n_term1+n_term2)
        elif operator == "-":
            result = str(n_term1-n_term2)

        max_len = max(len(term1), len(term2))

        result_len = 2+max_len

        for i in range(result_len-len(term1)):
            term1 = " " + term1

        for i in range(result_len-len(term2)-1):
            term2 = " " + term2

        term2 = operator + term2

        border = ""

        for i in range(result_len):
            border = "-" + border

        for i in range(len(border)-len(result)):
            result = " " + result

        spaces = "    "

        if i == len(problems):
            spaces = ""

        output[0] = output[0] + term1 + spaces
        output[1] = output[1] + term2 + spaces
        output[2] = output[2] + border + spaces

        if print_out == True:
            output[3] = output[3] + result + spaces
    #main_Logic


    final_string = ""

    for i in output:
        if i!="":
            final_string = final_string + i[0:len(i)-4] + "\n";
            
    final_string = final_string[0:len(final_string)-1]

    return final_string


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))

def test():
    return arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)
