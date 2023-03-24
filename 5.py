def inverter_string(string):
    # Encontrar o tamanho da string
    tamanho = len(string)

    # Inverter a string
    for i in range(tamanho // 2):
        temp = string[i]
        string[i] = string[tamanho - i - 1]
        string[tamanho - i - 1] = temp

    return string


def main():
    string = input("Digite uma string: ")

    string_invertida = inverter_string(list(string))

    print("Sua string invertida: ", ''.join(string_invertida))


if __name__ == '__main__':
    main()
