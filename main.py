import requests
import argparse
import json

# Function to fetch user events from GitHub API
def fetch_github_activity(username):
    url = f'https://api.github.com/users/{username}/events/public'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to fetch data for user {username}.")
        return None

    return response.json()

# Function to format and display the events
def display_activity(events):
    if not events:
        print("No recent activities found.")
        return

    print(f"\nRecent Activities:")
    for event in events:
        event_type = event.get('type')
        created_at = event.get('created_at')
        repo_name = event.get('repo', {}).get('name')
        actor = event.get('actor', {}).get('login')
        
        print(f"\nEvent Type: {event_type}")
        print(f"Created At: {created_at}")
        print(f"Repository: {repo_name}")
        print(f"User: {actor}")
        print('-' * 50)

# Main function to handle CLI input and output
def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub user's recent activities")
    parser.add_argument("username", nargs="?", help="GitHub username to fetch activities for")
    args = parser.parse_args()

    # If username is not provided as an argument, prompt for input
    username = args.username
    if not username:
        username = input("Enter the GitHub username: ").strip()

    if not username:
        print("Error: A GitHub username must be provided.")
        return

    print(f"\nFetching activities for GitHub user: {username}")
    
    events = fetch_github_activity(username)
    display_activity(events)

if __name__ == '__main__':
    main()
