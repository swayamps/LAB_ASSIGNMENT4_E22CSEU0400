class CricketMatch:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class CricketMatchTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def list_matches_by_team(self, team):
        for match in self.matches:
            if team in [match.team1, match.team2]:
                print(f"Location: {match.location}, Team 1: {match.team1}, Team 2: {match.team2}, Timing: {match.timing}")

    def list_matches_by_location(self, location):
        for match in self.matches:
            if match.location == location:
                print(f"Team 1: {match.team1}, Team 2: {match.team2}, Timing: {match.timing}")

    def list_matches_by_timing(self, timing):
        for match in self.matches:
            if match.timing == timing:
                print(f"Location: {match.location}, Team 1: {match.team1}, Team 2: {match.team2}")

def main():
    match_table = CricketMatchTable()

    match_table.add_match(CricketMatch("Mumbai", "India", "Sri Lanka", "DAY"))
    match_table.add_match(CricketMatch("Delhi", "England", "Australia", "DAY-NIGHT"))
    match_table.add_match(CricketMatch("Chennai", "India", "South Africa", "DAY"))
    match_table.add_match(CricketMatch("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    match_table.add_match(CricketMatch("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    match_table.add_match(CricketMatch("Delhi", "India", "Australia", "DAY"))

    print("Search options:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        team = input("Enter the team name: ")
        match_table.list_matches_by_team(team)
    elif choice == 2:
        location = input("Enter the location: ")
        match_table.list_matches_by_location(location)
    elif choice == 3:
        timing = input("Enter the timing: ")
        match_table.list_matches_by_timing(timing)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()