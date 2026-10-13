from pathlib import Path

from pyspark.sql import SparkSession


# Create Spark session
spark = (
    SparkSession.builder
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "2")
    .appName("HW04_Part1")
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


# Process data
nuek_processed = (
    nuek_repart
    .where("final_priority < 3")
    .select("unit_id", "final_priority")
    .groupBy("unit_id")
    .count()
)


# Additional transformation
nuek_processed = nuek_processed.where("count > 2")


# Trigger execution
nuek_processed.collect()


input("Press Enter to stop Spark...")


spark.stop()