import pysplit
from .config import HYSPLITConfig, TrajectoryConfig

class TrajectoryGenerator:
    def __init__(self, hysplit_config: HYSPLITConfig, traj_config: TrajectoryConfig):
        self.hysplit_config = hysplit_config
        self.traj_config = traj_config

    def generate(self):
        print("[PySPLIT] Starting bulk trajectory generation...")
        pysplit.generate_bulktraj(
            self.traj_config.basename,
            str(self.hysplit_config.working_dir),
            str(self.hysplit_config.storage_dir),
            str(self.hysplit_config.meteo_dir),
            self.traj_config.years,
            self.traj_config.months,
            self.traj_config.hours,
            self.traj_config.altitudes,
            self.traj_config.location,
            self.traj_config.runtime,
            monthslice=self.traj_config.monthslice,
            get_reverse=self.traj_config.get_reverse,
            get_clipped=self.traj_config.get_clipped,
        )
        print("[PySPLIT] Trajectories generated successfully.")
