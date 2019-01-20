#!/usr/bin/env python 2.7.12

import psycopg2


DB = "news"


def get_articles():
    """Return the most popular three articles,
     most popular article at the top."""
    db = psycopg2.connect(database=DB)
    c = db.cursor()
    print("The most popular three articles:")
    c.execute(
        "SELECT title," +
        " COUNT(path) as numberOfViws FROM articles ,log " +
        "where status = '200 OK'  and SUBSTRING(log.path, 10, 50) =slug" +
        " GROUP BY path, title ORDER BY COUNT(path)  DESC Limit 3 ;"
    )
    articles = c.fetchall()
    for a, b in articles:
        Pinstr = "\"{0}\" _ {1} views ".format(a, b)
        print (Pinstr)
    print("\n")
    db.close()
    return articles


def get_authors():
    """Return the most popular article authors,
     most popular author at the top."""
    db = psycopg2.connect(database=DB)
    c = db.cursor()
    c.execute(
        "select name, sum(numberOfViws) from authors ," +
        "(SELECT title, author, COUNT(path) as numberOfViws " +
        " FROM articles ,log " +
        " where status = '200 OK'  and SUBSTRING(log.path, 10, 50) =slug" +
        " GROUP BY path, title , author ORDER BY COUNT(path)  DESC) as num" +
        " where authors.id= num.author" +
        " group by name ORDER BY sum(numberOfViws)  DESC;"
    )
    print("The most popular article authors:")
    authors = c.fetchall()
    for a, b in authors:
        pinstr = "{0} _ {1} views ".format(a, b)
        print (pinstr)
    print("\n")
    db.close()
    return authors


def get_errors():
    """Return the days that lead to errors more than 1%."""
    db = psycopg2.connect(database=DB)
    c = db.cursor()
    c.execute(
        "SELECT date(time)," +
        "100.0 * Sum(CASE WHEN status != '200 OK' " +
        "THEN 1 ELSE 0 END) / Count(*) AS pregnencies_succeded_pct" +
        " FROM log GROUP  BY date(time) " +
        "having 100.0*Sum(CASE WHEN status!='200 OK'" +
        "THEN 1 ELSE 0 END)/Count(*)> 1;"
    )
    errors = c.fetchall()
    print("The days that lead to errors more than 1%:")
    for a, b in errors:
        m = a.strftime("%B %d,%Y")
        n = round(b, 2)
        print m, "_", n, "% errors"
    print("\n")
    db.close()
    return errors


if __name__ == '__main__':
    get_articles()
    get_authors()
    get_errors()
