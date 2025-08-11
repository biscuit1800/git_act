import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description="Get recent GitHub activity")
    parser.add_argument("username", help="GitHub username")
    args = parser.parse_args()

    try:
        r = requests.get(url=f"https://api.github.com/users/{args.username}/events")

        if r.status_code == 200:
            data = r.json()
            if not data:
                print("No public activity for this user.")
                return
            counts = {}

            for d in data:
                login = d.get("actor", {}).get("login", "unknown")
                event_type = d.get("type", "unknown")
                repo_name = d.get("repo", {}).get("name", "unknown")

                key = (login, event_type, repo_name)

                if key in counts:
                    counts[key] += 1
                else:
                    counts[key] = 1

            for (login, event_type, repo_name), count in counts.items():
                print(f"{count} - {login} - {event_type} - {repo_name}")

        elif r.status_code == 404:
            print("User not found.")
        elif r.status_code == 403:
            print("GitHub API rate limit exceeded.")
        else:
            print(f"An error occurred. Status code: {r.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to GitHub API: {e}")
