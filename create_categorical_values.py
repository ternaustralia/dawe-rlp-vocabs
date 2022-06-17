from pathlib import Path

from src import api

path = Path("vocab_files/categorical_collections")


if __name__ == "__main__":
    api.categorical_values.write_all(path)
