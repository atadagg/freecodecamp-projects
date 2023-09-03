def arithmetic_arranger(L, display=False):

    if len(L) > 5:
        return("Error: Too many problems.")

    first_operand_list = []
    second_operand_list = []
    operator_list = []
    total_list = []
    space_list = []
    arranged_output = ""
    answer = ""

    for i in range(len(L)):
        equation = L[i]
        equation = equation.split() # split the equation into a list

        if len(equation[0]) > 4 or len(equation[2]) > 4:
            return ("Error: Numbers cannot be more than four digits.")

        if equation[1] == "+":
            try:
                current_total = int(equation[0]) + int(equation[2])
                total_list.append(current_total)
            except:
                return("Error: Numbers must only contain digits.")

            current_space = max(len(equation[0]), len(equation[2])) + 2
            space_list.append(current_space)
            
            first_operand_list.append(int(equation[0]))
            second_operand_list.append(int(equation[2]))

            operator_list.append("+")

        elif equation[1] == "-":            
            try:                                                        # this try here is to determine if the numbers are made of digits or not
                current_total = int(equation[0]) - int(equation[2]) 
                total_list.append(current_total)
            except:
                return("Error: Numbers must only contain digits.")

            current_space = max(len(equation[0]), len(equation[2])) + 2
            space_list.append(current_space)

            first_operand_list.append(int(equation[0]))
            second_operand_list.append(int(equation[2]))

            operator_list.append("-")
        else:
            return("Error: Operator must be '+' or '-'.")


    

    for i in range(len(first_operand_list)):
        arranged_output += (" " * (space_list[i]-len(str(first_operand_list[i]))) + f"{first_operand_list[i]}" + "    ") # print the spaces and first operands

    arranged_output = arranged_output.rstrip()
    arranged_output += "\n"
    for i in range(len(second_operand_list)):
        arranged_output += (operator_list[i] + " " * (space_list[i] - len(str(second_operand_list[i])) - 1) + f"{second_operand_list[i]}" + "    ")


    arranged_output = arranged_output.rstrip()
    arranged_output += "\n"
    for i in range(len(space_list)):
        arranged_output += ("-" * space_list[i] + "    ")

    arranged_output = arranged_output.rstrip()
    print(arranged_output)

    for i in range(len(total_list)):
        answer += (" " * (space_list[i] - len(str(total_list[i]))) + f"{total_list[i]}" + "    ")

    answer = answer.rstrip()
    if display:
      print(answer)
      arranged_output = arranged_output + "\n" + answer

    return arranged_output

