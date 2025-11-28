from pyspark.sql import SparkSession



print("Creating Spark Session:")

spark: SparkSession = (
    SparkSession.builder
    .appName('AWS_WORKSPACE') #type: ignore
    .getOrCreate()
)






print("-----------------------------------------------------------------------------")
print("**************************Execution Completed********************************")
print("-----------------------------------------------------------------------------")
# spark.stop()