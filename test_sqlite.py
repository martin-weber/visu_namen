import sqlite3

conn = sqlite3.connect('zh_namen.db')

query = """SELECT vorname,
                  SUM(anzahl) as total,
                  AVG(anzahl) as avg_anzahl,
                  MIN(anzahl) as min_anzahl,
                  MAX(anzahl) as max_anzahl,
                  MIN(jahrgang) as first_year,
                  MAX(jahrgang) as last_year,
                  geschlecht
            FROM vornahmen_zuerich
            WHERE :from_year <= jahrgang AND jahrgang <= :to_year AND geschlecht like :gender
            GROUP BY vorname, geschlecht
            ORDER BY total DESC
            LIMIT :limit"""
params = {"from_year": 1980, "to_year": 2016, "gender": "%", "limit": 100}

cursor = conn.cursor()
cursor.execute(query, params)
rows = cursor.fetchall()

print(cursor.rowcount)
for row in rows:
    print(row)

cursor.close()
conn.close()