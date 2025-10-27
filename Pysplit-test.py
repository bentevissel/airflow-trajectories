#Pysplit-test.py 
# Test script

# Prior to attempting trajectory generation with PySPLIT, the user should ensure
# that meteorology file names follow a format of '*mon*YY*#' or '*mon*YYYY*#' where:

# * '*' is a Bash-style wildcard
# * 'mon' is a three-letter lower-case abbreviation of the month
# * 'YY' or 'YYYY' is a two or four digit integer representation of the year 
# * '#' is the number of the file within the month

# For example, '*jan*07*2' will match files named 'gdas1.jan2007.w2' and
# 'edas.jan2007_2'.

# Import the package

import pysplit

#Working directory
working_dir = "/home/bvissel/airflow/hysplit5.4/working/"
#location where it will be stored
storage_dir = "/home/bvissel/airflow/trajectories/colgate2/"
#data dir
meteo_dir = "/home/bvissel/airflow/data/"

#specify where hysplit is located
hysplit_executable = "/home/bvissel/airflow/hysplit5.4/exec/hyts_std"
# in order for this to work also need to enter in terminal: 
# ls -l /home/bvissel/airflow/hysplit5.4/exec/hyts_std
# chmod +x /home/bvissel/airflow/hysplit5.4/exec/hyts_std

#basename
basename = 'colgate'


# Specify the arguments

years = [2012, 2020, 2025]
months = [8]
hours = [11, 17, 23]
altitudes = [500, 1000, 1500]
location = (42.82, -75.54)
runtime = -120


#run function

pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 2), get_reverse=True,
                          get_clipped=True, hysplit=hysplit_executable)