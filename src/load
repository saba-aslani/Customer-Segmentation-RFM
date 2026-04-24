Import sqlite3

def load(df, database_name="rfm.db", table_name="rfm_table"):
    """
    Load the transformed RFM data into a SQLite database.
    """
    conn = sqlite3.connect(database_name)

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=True
    )

    conn.close()
