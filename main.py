import random

drivers = {
    'Max Verstappen': {'team': 'Red Bull', 'skill': 95},
    'Sergio Perez': {'team': 'Red Bull', 'skill': 85},
    'Lewis Hamilton': {'team': 'Mercedes', 'skill': 92},
    'George Russell': {'team': 'Mercedes', 'skill': 88},
    'Charles Leclerc': {'team': 'Ferrari', 'skill': 90},
    'Carlos Sainz Jr.': {'team': 'Ferrari', 'skill': 87},
    'Fernando Alonso': {'team': 'Aston Martin', 'skill': 85},
    'Lance Stroll': {'team': 'Aston Martin', 'skill': 78},
    'Lando Norris': {'team': 'McLaren', 'skill': 89},
    'Oscar Piastri': {'team': 'McLaren', 'skill': 88},
    'Esteban Ocon': {'team': 'Alpine', 'skill': 79},
    'Pierre Gasly': {'team': 'Alpine', 'skill': 80},
    'Valtteri Bottas': {'team': 'Alfa Romeo', 'skill': 79},
    'Zhou Guanyu': {'team': 'Alfa Romeo', 'skill': 78},
    'Kevin Magnussen': {'team': 'Haas', 'skill': 78},
    'Nico Hulkenberg': {'team': 'Haas', 'skill': 79},
    'Yuki Tsunoda': {'team': 'AlphaTauri', 'skill': 77},
    'Daniel Ricciardo': {'team': 'AlphaTauri', 'skill': 80},
    'Alexander Albon': {'team': 'Williams', 'skill': 81},
    'Logan Sargeant': {'team': 'Williams', 'skill': 75}
}

reliability_factor = {
    'Red Bull': 92,
    'Mercedes': 90,
    'Ferrari': 89,
    'Aston Martin': 84,
    'McLaren': 90,
    'Alpine': 82,
    'Alfa Romeo': 75,
    'Haas': 78,
    'AlphaTauri': 80,
    'Williams': 76
}

weather_conditions = ["dry", "wet"]
track_type = ["high-speed", "technical"]

driver_standings = {driver: 0 for driver in drivers}
constructor_standings = {team: 0 for team in reliability_factor}       
points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1] 

def simulate_qualifying():
    qualifying_results = []
    for driver, stats in drivers.items():
        base_perfomance = stats["skill"]
        team_reliability = reliability_factor[stats["team"]]
        track_bonus = random.randint(-5, 5)
        weather_penalty = random.randint(-10, 0) if random.choice(
            weather_conditions) == "wet" else 0
        qualifying_score = base_perfomance + \
            team_reliability / 10 + track_bonus + weather_penalty
        qualifying_results.append((driver, qualifying_score))
    qualifying_results.sort(key=lambda x: x[1], reverse=True)
    return [driver for driver, score in qualifying_results]


def simulate_race(qualifying_results):
    race_results = []
    for i, driver in enumerate(qualifying_results):
        base_performance = drivers[driver]["skill"]
        reliability_roll = random.randint(0, 100)
        if reliability_roll > reliability_factor[drivers[driver]["team"]]:
            print(f"{driver} had a machnical failure!")
            continue
        race_bonus = random.randint(-10, 10)
        weather_penalty = random.randint(-10, 0) if random.choice(weather_conditions) == "wet" else 0
        race_score = base_performance + race_bonus + weather_penalty - i*2
        race_results.append((driver, race_score))
    race_results.sort(key=lambda x:x[1], reverse=True)
    return[driver for driver, score in race_results]


def update_standings(race_results):
   for i, driver in enumerate(race_results[:10]):
      driver_standings[driver] += points[i] 
      constructor_standings[drivers[driver]["team"]] += points[i] 


def save_standings():
   with open("standings.txt" , "w") as file:
      file.write("Drivers Standings:\n")
      sorted_drivers = sorted(driver_standings.items(), key=lambda x: x[1], reverse=True)
      for i, (driver, pts) in enumerate(sorted_drivers, 1):
            file.write(f"{i}. {driver}: {pts} points\n")
            
      file.write("\nConstructor Standings:\n")
      sorted_teams = sorted(constructor_standings.items(), key=lambda x: x[1], reverse=True)
      for i, (team, pts) in enumerate(sorted_teams, 1):
            file.write(f"{i}. {team}: {pts} points\n")
   print("Standings saved to standings.txt\n")      


def display_standings():
    print("\n--- Driver Standings ---")
    sorted_drivers = sorted(driver_standings.items(), key=lambda x: x[1], reverse=True)
    for i, (driver, pts) in enumerate(sorted_drivers, 1):
        print(f"{i}. {driver}: {pts} points")

    print("\n--- Constructor Standings ---")
    sorted_teams = sorted(constructor_standings.items(), key=lambda x: x[1], reverse=True)
    for i, (team, pts) in enumerate(sorted_teams, 1):
        print(f"{i}. {team}: {pts} points")


def predict_race_weekend():
  print("\n--- Qualifying Results ---")
  qualifying_results = simulate_qualifying()
  for i, driver in enumerate(qualifying_results, 1):
    print(f"{i}. {driver}")

  print("\n--- Race Results ---") 
  race_results = simulate_race(qualifying_results)
  for i, driver in enumerate(race_results, 1):
    print(f"{i}. {driver}")

  update_standings(race_results)
  print(f"\nwinner: {race_results[0]}")

  display_standings()
  save_standings()

def main():
    while True:
        predict_race_weekend()
        cont = input("Run another race weekend simulation? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Exiting the predictor.")
            break

main()

