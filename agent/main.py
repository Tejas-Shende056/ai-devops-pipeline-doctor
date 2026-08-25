import os

def main():
    failed_run_id = os.getenv("FAILED_RUN_ID")
    repo_name = os.getenv("REPO_NAME")

    print(f"--- AI DEVOPS DOCTOR TRIGGERED ---")
    print(f"Repository: {repo_name}")
    print(f"Failed CI Run ID: {failed_run_id}")
    print("Agent is ready to fetch logs next!")

if __name__ == "__main__":
    main()