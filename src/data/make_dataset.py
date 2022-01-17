""" Functions to create dataset for analysis
"""

import psycopg2
import pandas as pd

from src.utils.timer import timer


@timer
def create_speeches_dataset(con_details, query, save_location):
    """ Use local Docker database to extract speeches data

    :param con_details: Connection details for database
    :param query: SQL query for data extraction
    :param save_location: Location for resulting files
    """
    con = psycopg2.connect(**con_details)
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    df = pd.DataFrame(rows)
    column_names = ["id", "session", "electoral_term", "first_name", "last_name", "politician_id", "speech_content",
                    "fraction_id", "document_url", "position_short", "position_long", "date", "search_speech_content"]
    df.columns = column_names
    df.to_csv(save_location, index=False)


if __name__ == '__main__':
    con_details_localhost = {
        "host": "localhost",
        "database": "next",
        "user": "postgres",
        "password": "postgres",
        "port": "5432"
    }
    query_all = """SELECT * from open_discourse.speeches WHERE electoral_term = 18 OR electoral_term = 19"""
    save_location_all = "../../data/interim/bundestag_speeches_processed.csv"
    create_speeches_dataset(con_details_localhost, query_all, save_location_all)
