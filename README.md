# airflow-trajectories

In order to run the airflow trajectory generator, it is necessary to install HYSPLIT and the PySplit package.

First, create a virtual environment which runs on Python3.6 or 3.7, because Pysplit depends on that environment.

# Installing Hysplit

Highsplit can be downloaded using the following link: https://ready.arl.noaa.gov/HYSPLIT.php 

Place the HYSPLIT folder in the same directory as the folder you are working in/the virtual environment. 

# Pysplit

Pysplit can be installed in the virtual environment using 
```
pip install pysplit
```

# Data
The data has been obtained from https://www.ready.noaa.gov/data/archives/gdas1/

It is avaiable in the /data/ folder as a zip




