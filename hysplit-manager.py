import os
from pathlib import Path

class HYSPLITManager:
    def __init__(self, config):
        self.config = config

    def validate_environment(self):
        paths = [self.config.working_dir, self.config.storage_dir, self.config.meteo_dir, self.config.executable]
        for path in paths:
            if not Path(path).exists():
                raise FileNotFoundError(f"Required path not found: {path}")
        print("[HYSPLIT] Environment validated successfully.")

    def setup_working_directory(self):
        os.makedirs(self.config.storage_dir, exist_ok=True)
        print(f"[HYSPLIT] Working directory setup complete at {self.config.storage_dir}")
