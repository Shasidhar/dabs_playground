# Databricks notebook source
# MAGIC %md
# MAGIC # Demo of Databricks Workflows &raquo; Serverless and *Classic*
# MAGIC ## Classic

# COMMAND ----------

# Configure Delta Lake path
delta_path = "/tmp/dais2023/classic_workflows"

# Remove folder if it exists
dbutils.fs.rm(delta_path, recurse=True)

# COMMAND ----------

# Configure input source path
source_path = "dbfs:/databricks-datasets/retail-org/loyalty_segments/"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Read Purchase Orders data and write to Delta

# COMMAND ----------

# Create the Delta table with the Purchase Orders data
(spark
   .read
   .format("csv")
   .load(source_path, inferSchema=True, header=True)
   .write
   .mode("overwrite")
   .format("delta")
   .save(delta_path)
)