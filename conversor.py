import sys


def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    if len(sys.argv) != 3:
        print("Uso: python3 conversor.py <valor> <C|F>")
        sys.exit(1)

    valor = float(sys.argv[1])
    unidad = sys.argv[2].upper()

    if unidad == "C":
        print(f"{valor}C = {celsius_a_fahrenheit(valor)}F")
    elif unidad == "F":
        print(f"{valor}F = {fahrenheit_a_celsius(valor)}C")
    else:
        print("Unidad no reconocida. Usa 'C' o 'F'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
