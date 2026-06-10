import argparse
from exercises import ex1

def run_ex1():
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    ex1.plot_home_away_goals(data)
    print("Ejercicio 1 completado.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ex", type=int, required=True, help="Ejercicio a ejecutar (1-7)")
    args = parser.parse_args()

    if args.ex == 1:
        run_ex1()
    else:
        print("Ejercicio no implementado todavía.")

if __name__ == "__main__":
    main()
