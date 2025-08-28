# Databricks notebook source
# MAGIC %sql
# MAGIC DESCRIBE TABLE workspace.default.netflix_titles;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT type, COUNT(*) AS total
# MAGIC FROM netflix_titles
# MAGIC GROUP BY type;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT country, COUNT(*) AS total
# MAGIC FROM netflix_titles
# MAGIC WHERE country IS NOT NULL
# MAGIC GROUP BY country
# MAGIC ORDER BY total DESC
# MAGIC LIMIT 10;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT listed_in AS genre, COUNT(*) AS total
# MAGIC FROM netflix_titles
# MAGIC GROUP BY genre
# MAGIC ORDER BY total DESC
# MAGIC LIMIT 10;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT release_year, COUNT(*) AS total
# MAGIC FROM netflix_titles
# MAGIC GROUP BY release_year
# MAGIC ORDER BY release_year DESC;
# MAGIC

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC WITH country_count AS (
# MAGIC     SELECT country, COUNT(*) AS total
# MAGIC     FROM netflix_titles
# MAGIC     WHERE country IS NOT NULL
# MAGIC     GROUP BY country
# MAGIC )
# MAGIC SELECT *
# MAGIC FROM country_count
# MAGIC ORDER BY total DESC
# MAGIC LIMIT 5;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT country,
# MAGIC        COUNT(*) AS total,
# MAGIC        RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
# MAGIC FROM netflix_titles
# MAGIC WHERE country IS NOT NULL
# MAGIC GROUP BY country;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   type, 
# MAGIC   COUNT(*) AS total_titles
# MAGIC FROM netflix_titles
# MAGIC GROUP BY type;
# MAGIC
