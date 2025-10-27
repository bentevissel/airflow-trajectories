# This file contains the configurations for the trajectory generator

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass
class HYSPLITConfig:
    working_dir: Path
    storage_dir: Path
    meteo_dir: Path
    executable: Path = Path("C:/hysplit4/exec/hyts_std")

@dataclass
class TrajectoryConfig:
    basename: str
    years: List[int]
    months: List[int]
    hours: List[int]
    altitudes: List[int]
    location: Tuple[float, float]
    runtime: int = -120
    monthslice: slice = slice(0, 32, 2)
    get_reverse: bool = True
    get_clipped: bool = True
