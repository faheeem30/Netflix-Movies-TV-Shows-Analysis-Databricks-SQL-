
# 📺 Netflix Movies & TV Shows Analysis

## 🔹 Overview

This project analyzes the **Netflix Movies and TV Shows dataset** available on [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).
The goal is to perform **SQL-based analysis** to uncover insights about Netflix content, including the distribution of movies and TV shows, popular genres, release trends, and country-wise availability.


---

## 🔍 Analysis Performed

Using SQL queries, the following analyses were performed on the dataset:

1. **Movies vs TV Shows**

   ```sql
   SELECT type, COUNT(*) AS total_titles
   FROM netflix_titles
   GROUP BY type;
   ```

   * Counts total titles by type.
   * Helps understand the proportion of Movies vs TV Shows on Netflix.

2. **Top Countries with Most Content**

   ```sql
   SELECT country, COUNT(*) AS total
   FROM netflix_titles
   WHERE country IS NOT NULL
   GROUP BY country
   ORDER BY total DESC
   LIMIT 10;
   ```

   * Shows which countries produce the most Netflix content.

3. **Most Common Genres**

   ```sql
   SELECT listed_in AS genre, COUNT(*) AS total
   FROM netflix_titles
   GROUP BY genre
   ORDER BY total DESC
   LIMIT 10;
   ```

   * Identifies the genres that dominate Netflix content.

4. **Content Release Trends**

   ```sql
   SELECT release_year, COUNT(*) AS total
   FROM netflix_titles
   GROUP BY release_year
   ORDER BY release_year DESC;
   ```

   * Tracks the number of titles released each year.

5. **Top Countries by Content (with ranking)**

   ```sql
   SELECT country,
          COUNT(*) AS total,
          RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
   FROM netflix_titles
   WHERE country IS NOT NULL
   GROUP BY country;
   ```

   * Assigns a rank to countries based on the number of titles they produce.
<img width="1916" height="941" alt="image" src="https://github.com/user-attachments/assets/e21ee71c-df7e-48d1-a2d6-0d62e73dbd9f" />
<img width="1366" height="528" alt="image" src="https://github.com/user-attachments/assets/9062b137-858c-4f46-bed5-074e014e1fd6" />
<img width="1388" height="719" alt="image" src="https://github.com/user-attachments/assets/34321d17-3663-44c3-bc35-b5377d7f9865" />
<img width="1364" height="703" alt="image" src="https://github.com/user-attachments/assets/ba0e1cdf-8acd-4513-9b65-7212539c073f" />
<img width="1320" height="761" alt="image" src="https://github.com/user-attachments/assets/c4b070a9-da09-4ccb-bdf9-95c877f09314" />
<img width="1318" height="662" alt="image" src="https://github.com/user-attachments/assets/9bc4eda9-d293-4ca1-af34-e79a0491dbdb" />
<img width="1340" height="788" alt="image" src="https://github.com/user-attachments/assets/b5facd1b-c814-47cd-a50a-0b6c46f2c26f" />
<img width="1337" height="683" alt="image" src="https://github.com/user-attachments/assets/ed53317d-8e68-40bc-bb11-8edba19578f8" />


---

## 📊 Dashboard



👉 [View the Dashboard](https://dbc-e262f608-67b4.cloud.databricks.com/dashboardsv3/01f08105e03c152ea939ec4bdbea26be/published?o=1843048436549062)

<img width="1912" height="940" alt="image" src="https://github.com/user-attachments/assets/54741eeb-d6fb-4f4b-bad2-e72718832d75" />

---

## 🛠️ Tools & Technologies

* **Databricks** (PySpark + SQL)
* **Jupyter Notebook** (`netflix.ipynb` #in databricks query can retrieved as jypternotebook file )
* **Python** (`netflix.py`#in databricks this file magic command from databricks)
* **GitHub** for version control

---

## ⚡ Key Insights

* Movies dominate the Netflix library compared to TV Shows.
* The USA produces the highest number of Netflix titles.
* Drama, Comedies, and Documentaries are the most common genres.
* Netflix content production has increased significantly over the years.

---

## 📁 Dataset

* Source: [Kaggle - Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
* Columns include: `title`, `type`, `country`, `release_year`, `listed_in` (genres), `duration`, etc.

---







