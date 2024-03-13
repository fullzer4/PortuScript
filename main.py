import sys
import re

def interpret_visualg(statement, variables, in_variable_declaration=False):
    statement = statement.lower()

    match = re.match(r'^escreva\((.*)\)$', statement)
    if match:
        args = match.group(1).split(',')
        output = ""
        for arg in args:
            arg = arg.strip()
            if arg in variables:
                output += str(variables[arg]) + " "
            else:
                output += arg + " "
        print(output.strip())
        return
    
    tokens = statement.split()

    keyword = tokens[0]

    if keyword == "algoritimo":
        pass
    elif keyword == "inicio":
        in_variable_declaration = False
    elif keyword == "fim":
        pass
    elif keyword == "var":
        in_variable_declaration = True
        for var_name in tokens[1:]:
            variables[var_name.split(',')[0]] = None
    elif keyword == "escreva":
        print(" ".join(tokens[1:]))
    elif keyword == "leia":
        var_name = tokens[1]
        if var_name not in variables:
            print(f"ERRO: Variavel {var_name} nao declarada.")
            return
        value = input("Entre o valor de {}: ".format(var_name))
        variables[var_name] = int(value)
    elif keyword == "enquanto":
        condition = " ".join(tokens[1:])
        while eval(condition):
            for sub_statement in iter_statements():
                interpret_visualg(sub_statement, variables, in_variable_declaration)
                condition = " ".join(tokens[1:])
    else:
        if in_variable_declaration:
            for var_name in tokens[0:]:
                variables[var_name.split(',')[0]] = None
        else:
            print("Comando desconhecido:", statement)

def iter_statements():
    while True:
        statement = input("digite FIM para acabar a execucao ou continue: ")
        if statement == "fim":
            break
        yield statement

def interpret_file(filename):
    variables = {}
    try:
        with open(filename, 'r') as file:
            in_variable_declaration = False
            for statement in file:
                interpret_visualg(statement.strip(), variables, in_variable_declaration)
                if "var" in statement.lower():
                    in_variable_declaration = True
    except FileNotFoundError:
        print("Arquivo não encontrado:", filename)

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.vg>")
        return

    filename = sys.argv[1]
    interpret_file(filename)

if __name__ == "__main__":
    main()
