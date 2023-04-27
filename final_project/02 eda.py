# Databricks notebook source
# MAGIC %run ./includes/includes

# COMMAND ----------

start_date = str(dbutils.widgets.get('01.start_date'))
end_date = str(dbutils.widgets.get('02.end_date'))
hours_to_forecast = int(dbutils.widgets.get('03.hours_to_forecast'))
promote_model = bool(True if str(dbutils.widgets.get('04.promote_model')).lower() == 'yes' else False)

print(start_date,end_date,hours_to_forecast, promote_model)
print("YOUR CODE HERE...")

# COMMAND ----------

pip install -U pandas-profiling

# COMMAND ----------

# DBTITLE 1,Imports
from pathlib import Path
from pyspark.sql.functions import *

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import requests

import pandas_profiling
import pandas as pd
from pandas_profiling.utils.cache import cache_file

# COMMAND ----------


historic_trip_data_df = (spark.read
     .format("delta")
     .load("dbfs:/FileStore/tables/G11/bronze/historic_trip_data/"))
historic_trip_data_df.display()
historic_trip_data_df.printSchema()
historic_trip_data_df.count()


# COMMAND ----------


bronze_station_status_df = (spark.read
                           .format("delta")
                           .load("dbfs:/FileStore/tables/G11/bronze/station_status"))
bronze_station_status_df.display()


# COMMAND ----------

historic_trip_data_df = historic_trip_data.select("*").toPandas()
historic_trip_data_df['started_at']= pd.to_datetime(historic_trip_data_df['started_at'])
historic_trip_data_df['ended_at']= pd.to_datetime(historic_trip_data_df['ended_at'])


historic_trip_data_profile = pandas_profiling.ProfileReport(historic_trip_data_df)
historic_trip_data_profile

# COMMAND ----------

bronze_station_info_df = (spark.read
                         .format("delta")
                         .load("dbfs:/FileStore/tables/G11/bronze/station_info"))
bronze_station_info_df.display()

# COMMAND ----------

#For historic_trip_data_df

import pandas_profiling
import pandas as pd
from pandas_profiling.utils.cache import cache_file

historic_trip_data_df = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/bronze/historic_trip_data"))

df = historic_trip_data_df.select("*").toPandas()


# COMMAND ----------

profile = pandas_profiling.ProfileReport(df)
profile

# COMMAND ----------

#For bronze_station_status_df

import pandas_profiling
import pandas as pd
from pandas_profiling.utils.cache import cache_file

bronze_station_status_df = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/bronze/station_status"))
df = bronze_station_status_df.select("*").toPandas()

# COMMAND ----------

profile = pandas_profiling.ProfileReport(df)
profile

# COMMAND ----------

import pandas_profiling
import pandas as pd
from pandas_profiling.utils.cache import cache_file

bronze_station_info_df = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/bronze/station_info"))

df = bronze_station_info_df.select("*").toPandas()


# DBTITLE 1,bronze_station_status
bronze_station_status = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/bronze_station_status"))
bronze_station_status.display()

# COMMAND ----------

bronze_station_status_df = bronze_station_status.select("*").toPandas()
bronze_station_status_profile = pandas_profiling.ProfileReport(bronze_station_status_df)
bronze_station_status_profile

# COMMAND ----------

# DBTITLE 1,bronze_station_info
bronze_station_info = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/bronze_station_info"))
bronze_station_info.display()


# COMMAND ----------

bronze_station_info_df = bronze_station_info.select("*").toPandas()
bronze_station_info_profile = pandas_profiling.ProfileReport(bronze_station_info_df)
bronze_station_info_profile

# COMMAND ----------


historic_weather_df = (spark.readStream.format("delta").load("dbfs:/FileStore/tables/G11/bronze/historic_weather_data"))
historic_weather_df.display()

historic_weather_df = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/bronze/historic_weather_data"))
historic_weather_df.display()
historic_weather_df.printSchema()


# COMMAND ----------

import pandas_profiling
import pandas as pd
from pandas_profiling.utils.cache import cache_file

historic_weather_data_df = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/bronze/historic_weather_data"))
df = historic_weather_data_df.select("*").toPandas()

# COMMAND ----------

#Reading stream for historic trip data bronze
historic_trip_data_df = (spark.read
     .format("delta")
     .load("dbfs:/FileStore/tables/G11/bronze/historic_trip_data"))
historic_trip_data_df.display()
historic_trip_data_df.printSchema()
#here we have a bar chart displaying the end spots of the bikes and which spots are most common
#It is also grouped by if its a member or a casual user

# COMMAND ----------

historic_weather_df = (spark.read
                      .option("header", True)
                      .csv(NYC_WEATHER_FILE_PATH))
historic_weather_df.display()

# DBTITLE 1,historic_weather
historic_weather = (spark.read.format("delta").load("dbfs:/FileStore/tables/G11/historic_weather_df"))
historic_weather.display()


# COMMAND ----------

#Counts how many disctinct descriptions of the weather
print("Distinct Count: " + str(historic_weather.select("description").distinct().count()))
print("Distinct Count: " + str(historic_weather.select("description").distinct().count()))

# COMMAND ----------

historic_weather_df = historic_weather.select("*").toPandas()
historic_weather_profile = pandas_profiling.ProfileReport(historic_weather_df)
historic_weather_profile

# COMMAND ----------


# DBTITLE 1,More in depth EDA


# COMMAND ----------

import json

# Return Success
dbutils.notebook.exit(json.dumps({"exit_code": "OK"}))

# COMMAND ----------


