from pathlib import Path

from pyspark.sql import SparkSession


# Create Spark session
spark = (
    SparkSession.builder
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "2")
    .appName("HW04_Part3")
    .getOrCreate()
)


# Build dataset path
project_root = Path(__file__).resolve().parents[2]
data_path = project_root / "data" / "nuek-vuh3.csv"


# Load dataset
nuek_df = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(str(data_path))
)


# Repartition dataset
nuek_repart = nuek_df.repartition(2)


# Process and cache intermediate result
nuek_processed_cached = (
    nuek_repart
    .where("final_priority < 3")
    .select("unit_id", "final_priority")
    .groupBy("unit_id")
    .count()
    .cache()
)


# First action: compute and materialize cache
nuek_processed_cached.collect()


# Reuse cached result
nuek_processed = nuek_processed_cached.where("count > 2")


# Second action
nuek_processed.collect()


input("Press Enter to stop Spark...")


# Release cached data
nuek_processed_cached.unpersist()


spark.stop()