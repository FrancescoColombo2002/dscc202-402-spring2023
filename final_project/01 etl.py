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

spark.sql("set spark.sql.streaming.schemaInference=true")
historic_trip_data_df = (spark.readStream
                         .option("header", True)
                         .csv(BIKE_TRIP_DATA_PATH))

# COMMAND ----------

display(historic_trip_data_df)

# COMMAND ----------

from pyspark.sql.functions import col
historic_trip_df = historic_trip_data_df.filter(("start_station_name == 'Cleveland Pl & Spring St' OR end_station_name == 'Cleveland Pl & Spring St'"))
display(historic_trip_df)

# COMMAND ----------

bronze_station_status_df = (spark.readStream
                           .format("delta")
                           .load(BRONZE_STATION_STATUS_PATH))

# COMMAND ----------

bronze_station_status_df.display()

# COMMAND ----------

bronze_station_info_df = (spark.readStream
                           .format("delta")
                           .option("ignoreChanges", "true")
                           .load(BRONZE_STATION_INFO_PATH))

# COMMAND ----------

bronze_station_info_df.display()

# COMMAND ----------

bronze_station_info_df = bronze_station_info_df.filter("short_name == '5492.05'").distinct()

# COMMAND ----------

bronze_station_info_df.display()

# COMMAND ----------

STATION_ID = "66db2fd0-0aca-11e7-82f6-3863bb44ef7c"

# COMMAND ----------

bronze_station_status_df = bronze_station_status_df.filter("station_id == '66db2fd0-0aca-11e7-82f6-3863bb44ef7c'")

# COMMAND ----------

bronze_station_status_df.display()

# COMMAND ----------

print(bronze_station_status_df.groupby().count())

# COMMAND ----------

import json

# Return Success
dbutils.notebook.exit(json.dumps({"exit_code": "OK"}))
# comment

# COMMAND ----------


