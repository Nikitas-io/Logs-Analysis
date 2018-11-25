#!/bin/env python2.7

import psycopg2
import datetime

db = psycopg2.connect(database="news")
c = db.cursor()

# 1. Find the three most popular articles of all time.
# The use of the CONCAT() sql function in this case is to create a
# string that can match the path of the logs, by adding the "/article/"
# sub-path to the article's slug.
c.execute('''SELECT title, COUNT(log.id) AS views
    FROM log, articles WHERE path = CONCAT('/article/',articles.slug)
    GROUP BY title
    ORDER BY views DESC
    LIMIT 3;
''')
results1 = c.fetchall()
print("3 Most Popular Articles:\n")
for i in range(len(results1)):
    print('"' + results1[i][0] + '" - ' + str(results1[i][1]) + " views")

# 2. Find the most popular article authors of all time.
c.execute('''SELECT name, COUNT(log.id) AS views
    FROM log, articles, authors
    WHERE path = CONCAT('/article/',articles.slug)
    AND authors.id = articles.author
    GROUP BY name
    ORDER BY views DESC
''')
results2 = c.fetchall()
print("\n-----------------------\n\nAuthors Ordered by Popularity:\n")
for i in range(len(results2)):
    print(results2[i][0] + ' - ' + str(results2[i][1]) + " views")

# 3. Find on which days did more than 1% of requests lead to errors.
''' The SQL DATE() function extracts the date part out of the date-time
expressions in the log.time column.
The SQL ROUND() function rounds a number to a specified number of
decimal places. In this case, 1 decimal place.
The SQL CASE() function goes through conditions and returns a value
when the first condition is met. '''
# To find the percentage of errors each day, I devided the sum of the
# errors by the total of the requests and grouped by day.
c.execute('''SELECT * FROM(
    SELECT DATE(time) AS day,
    ROUND(100.0 * SUM(
    CASE
        WHEN log.status = '200 OK' THEN 0
        ELSE 1
    END) / COUNT(log.id), 1) AS error_margin
    FROM log
    GROUP BY day
    ORDER BY error_margin DESC
    ) AS days
    WHERE error_margin > 1;
''')
results3 = c.fetchall()
print("\n-----------------------\n\nDays with more than 1% errors:\n")
for i in range(len(results3)):
    # Get the date as returned by the database.
    day = results3[i][0]
    # Reconstruct the date in a different format.
    newFormat = day.strftime("%B") + ' ' + \
        day.strftime("%d") + ', ' + day.strftime("%Y")
    print(newFormat + ' - ' + str(results3[i][1]) + '% errors')

db.close()
