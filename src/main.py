import argparse
from exercises import ex1
from exercises import ex2
from exercises import ex3
from exercises import ex4
from exercises import ex5
from exercises import ex6


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


def run_ex4():
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    season_stats = ex4.compute_goals_by_season(data)
    print(season_stats)
    ex4.plot_goals_by_season(season_stats)
    print("Ejercicio 4 completado.")


def run_ex5():
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    corr = ex5.compute_correlations(data)
    print(corr)
    ex5.plot_correlation_heatmap(corr)
    print("Ejercicio 5 completado.")


def run_ex6():
    data = ex1.load_and_eda("data/LaLiga_Matches.csv")
    model, real, predicted = ex6.train_regression_model(data)
    print("Modelo entrenado. Coeficientes:", model.coef_)
    ex6.plot_regression_results(real, predicted)
    print("Ejercicio 6 completado.")


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
    elif args.ex == 4:
        run_ex4()
    elif args.ex == 5:
        run_ex5()
    elif args.ex == 6:
        run_ex6()
    else:
        print("Ejercicio no implementado todavía.")


if __name__ == "__main__":
    main()



