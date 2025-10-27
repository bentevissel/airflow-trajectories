from pathlib import Path
from airflow_mappings.config import HYSPLITConfig, TrajectoryConfig
from airflow_mappings.hysplit_manager import HYSPLITManager
from airflow_mappings.trajectory_generator import TrajectoryGenerator

def main():
    hysplit_conf = HYSPLITConfig(
        working_dir=Path("C:/hysplit4/working"),
        storage_dir=Path("C:/trajectories/colgate"),
        meteo_dir=Path("E:/gdas")
    )

    traj_conf = TrajectoryConfig(
        basename="colgate",
        years=[2007, 2011],
        months=[1, 8],
        hours=[11, 17, 23],
        altitudes=[500, 1000, 1500],
        location=(42.82, -75.54)
    )

    manager = HYSPLITManager(hysplit_conf)
    manager.validate_environment()
    manager.setup_working_directory()

    generator = TrajectoryGenerator(hysplit_conf, traj_conf)
    generator.generate()

if __name__ == "__main__":
    main()
