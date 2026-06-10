import argparse
from exercises import ex1
from exercises import ex2
from exercises import ex3


def run_ex1():
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    ex1.plot_home_away_goals(data)
    print("Ejercicio 1 completado.")


def run_ex2():
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    stats = ex2.compute_goal_stats(data)
    print("Estadísticas de goles:", stats)
    ex2.plot_total_goals_histogram(data)
    print("Ejercicio 2 completado.")


def run_ex3():
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    stats = ex3.compute_team_stats(data)
    print(stats)
    ex3.plot_team_wins(stats)
    print("Ejercicio 3 completado.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ex", type=int, required=True, help="Ejercicio a ejecutar (1-7)")
    args = parser.parse_args()

    if args.ex == 1:
        run_ex1()
    elif args.ex == 2:
        run_ex2()
    elif args.ex == 3:
        run_ex3()
    else:
        print("Ejercicio no implementado todavía.")


if __name__ == "__main__":
    main()

