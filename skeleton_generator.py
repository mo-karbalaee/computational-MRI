import os
from pathlib import Path

# Base directory for the folder structure
base_dir = "CMRI"


# Function to create the multi-level folder structure
def create_folders(base_dir):
    # Create the base directory
    Path(base_dir).mkdir(parents=True, exist_ok=True)

    # Loop to create Lab01 to Lab10 folders
    for i in range(1, 11):
        lab_dir = Path(base_dir) / f"Lab{i:02d}"
        lab_dir.mkdir(parents=True, exist_ok=True)

        # Special case for Lab10 to create logs/exercise
        if i == 10:
            logs_dir = lab_dir / "logs" / "exercise"
            logs_dir.mkdir(parents=True, exist_ok=True)


# Run the function to create the folders
if __name__ == "__main__":
    create_folders(base_dir)
