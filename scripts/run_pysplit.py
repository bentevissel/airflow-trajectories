#import pysplit
from datetime import datetime #make sure you have pysplit in your virtual environment, pip install pysplit

class Inputs:
    def __init__(self, lat, lon, height, start_time, duration, meteo_dir, output_dir):
        """
        Inputs to run trajectory model on.
        Parameters:
        - lat, lon: starting (geographic) coorinates
        - height: starting altitude, m
        - start_time: trajectory launch time, string datetime format
        - duration: how long to run trajectory for, hours, negative indicates backwards trajectory
        - meteo_dir: directory where meteorological data is stored
        - output_dir: directory to place output from hysplit
        """
        self.lat = lat
        self.lon = lon
        self.height = height
        self.start_time = start_time
        self.duration = duration
        self.meteo_dir = meteo_dir
        self.output_dir = output_dir

    def __str__(self):
        return f"lat: {self.lat}, lon: {self.lon}, height: {self.height} m, start time: {self.start_time}"

class Trajectory:
    """Generating a trajectory using PYSPLIT package"""
    def __init__(self):
