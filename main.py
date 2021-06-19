from google.cloud import bigquery

BQ_client = bigquery.Client()

simple_query = """
    SELECT date, keywords, title, id FROM bigquery-public-data.breathe.nature LIMIT 10
"""

custom_dataset_query = """
    SELECT Movie_Title, Release_Date, Genre, Revenue FROM `googe-drive-test.my_dataset_movies.movies` LIMIT 1000
"""

query_results = BQ_client.query(custom_dataset_query)

for i, result in enumerate(query_results):
    print(f"{i}:${result}\n")    
