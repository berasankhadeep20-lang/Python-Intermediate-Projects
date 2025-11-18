#a program creating a priemere league table in binary file taking user input for team names and points goals for and against and calculating goal difference and displaying the table sorted by points and goal difference
import struct
import os
import operator
import pickle
from collections import namedtuple
Team = namedtuple('Team', ['name', 'points', 'goals_for', 'goals_against', 'goal_difference'])
def get_team_data():
    name = input("Enter team name: ")
    points = int(input("Enter points: "))
    goals_for = int(input("Enter goals for: "))
    goals_against = int(input("Enter goals against: "))
    goal_difference = goals_for - goals_against
    return Team(name, points, goals_for, goals_against, goal_difference)
def save_team_data(filename, team):
    with open(filename, 'ab') as f:
        pickle.dump(team, f)
def load_team_data(filename):
    teams = []
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            while True:
                try:
                    team = pickle.load(f)
                    teams.append(team)
                except EOFError:
                    break
    return teams
def display_table(teams):
    teams_sorted = sorted(teams, key=operator.attrgetter('points', 'goal_difference'), reverse=True)
    print(f"{'Team':<40}{'Points':<10}{'Goals For':<12}{'Goals Against':<15}{'Goal Difference':<15}")
    print("="*92)
    for team in teams_sorted:
        print(f"{team.name:<40}{team.points:<10}{team.goals_for:<12}{team.goals_against:<15}{team.goal_difference:<15}")
def main():
    filename = 'premier_league_table.dat'
    while True:
        choice = input("Do you want to add a team? (y/n): ").lower()
        if choice == 'y':
            team = get_team_data()
            save_team_data(filename, team)
        else:
            break
    teams = load_team_data(filename)
    display_table(teams)
if __name__ == "__main__":
    main()