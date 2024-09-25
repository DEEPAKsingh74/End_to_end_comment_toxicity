# entity

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataLoadingConfig:
	zip_file_path: Path
	destination_dir: Path