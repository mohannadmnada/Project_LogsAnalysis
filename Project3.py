#!/usr/bin/env python
import psycopg2
import datetime

DBNAME = "news"


def result_display(returned_results):
    for i in returned_results:
        # log = "- "
        # log += str(i[0]) + " - "
        # log += str(i[1]) + " views"
        log = '- {} - {} views\n'.format(i[0], i[1])
        # print log
        text_file.write(log)
        text_file.write("\n")


def error_display(returned_results):
    for i in returned_results:
        if i[1] > 1.0:
            log = '- {:%B %d, %Y} - {}% errors\n'.format(i[0], i[1])
            # print log
            text_file.write(log)
            text_file.write("\n")


def question_one():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select title, num from articles,
    (select split_part(path, '/article/', 2), count(*) as num
    from log group by path
    order by num desc) as subq
    where slug = split_part order by num desc limit 3;
    """
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def question_two():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select name, sum from authors join (
        select author , sum(num) from ( select author,
        articles.slug, num from articles join
        (select split_part(path, '/article/', 2), count(*) as num
        from log group by path) as subq on articles.slug = split_part
        order by num desc ) as subq2 group by author) as subq3
        on authors.id = author order by sum desc;
        """
    c.execute(query)
    resutls = c.fetchall()
    db.close()
    return resutls


def question_three():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select day, ROUND(errors * 100.0 / total_requests, 1)
    as percentage_errors
    from ( select time::date, count(*) as total_requests
    from log group by time::date) table1
    join (select time::date as day, count(*) as
    errors from log where status not like '200 OK'
    group by day) table2
    on (table2.day = table1.time::date)
    order by percentage_errors desc;
    """
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


text_file = open("Output.txt", "w")
ques1 = "1. What are the most popular three articles of all time?\n\n"
text_file.write(ques1)


# print "1. What are the most popular three articles of all time?"
results_one = question_one()
result_display(results_one)

text_file.write("\n")
ques2 = "2. Who are the most popular article authors of all time?\n\n"
text_file.write(ques2)
# print "\n", "2. Who are the most popular article authors of all time?"
results_two = question_two()
result_display(results_two)

text_file.write("\n")
ques3 = "3. On which days did more than 1% of requests lead to errors?\n\n"
text_file.write(ques3)
# print "\n", "3. On which days did more than 1% of requests lead to errors?"
results_three = question_three()
error_display(results_three)
text_file.close()
