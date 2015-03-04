------------------
-- Problem 1
------------------

-- Create table
CREATE TABLE frequency (
    docid character(30),
    term character(30),
    count integer
    )

COPY frequency FROM 'C:\Users\Cicero\Documents\Estudos\University of Washigton\Introduction to Data Science\assignment2\Frequency2.csv' CSV HEADER

-- a
-- σ10398_txt_earn(frequency)
select * from frequency
where docid = '10398_txt_earn';

-- b
-- πterm(σdocid=10398_txt_earn and count=1(frequency))
select term from frequency
where docid = '10398_txt_earn' and count = 1;

-- c
-- πterm(σdocid=10398_txt_earn and count=1(frequency)) U πterm(σdocid=925_txt_trade and count=1(frequency))
select term from frequency
where docid = '10398_txt_earn' and count = 1 
UNION 
select term from frequency
where docid = '925_txt_trade' and count = 1;

-- d
-- count: Write a SQL statement to count the number of documents containing the word "parliament"
select COUNT(DISTINCT docid) from frequency
where term = 'parliament';

-- e
-- big documents: Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms.
select docid
from frequency
group by
docid
HAVING
sum(count) > 300;

-- f
-- two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
select 
count(DISTINCT docid) 
from(
select DISTINCT docid from frequency
where term = 'transactions'
INTERSECT
select DISTINCT docid from frequency
where term = 'world') frequency;

------------------
-- Problem 2
------------------

-- Create table
CREATE TABLE Ma (
    row_num integer,
    col_num integer,
    valor integer
    )

CREATE TABLE Mb (
    row_num integer,
    col_num integer,
    valor integer
    )

COPY Ma FROM 'C:\Users\Cicero\Documents\Estudos\University of Washigton\Introduction to Data Science\assignment2\a.csv' CSV HEADER
COPY Mb FROM 'C:\Users\Cicero\Documents\Estudos\University of Washigton\Introduction to Data Science\assignment2\b.csv' CSV HEADER

-- g
-- Express A X B as a SQL query,

-- using JOIN
CREATE VIEW MatrixC(i, j, element_value)
as
select ma.row_num , mb.col_num, sum(ma.valor * mb.valor)
FROM ma JOIN mb ON ma.col_num = mb.row_num
GROUP BY ma.row_num , mb.col_num;

-- using Where (eu prefiro)
CREATE VIEW MatrixC(i, j, element_value)
as
SELECT ma.row_num, mb.col_num, SUM(ma.valor * mb.valor)
FROM ma, mb
WHERE ma.col_num = mb.row_num
GROUP BY ma.row_num, mb.col_num;

------------------
-- Problem 3
------------------

-- h
-- Write a query to compute the similarity matrix DDT
CREATE VIEW Doc_similarity(doci, docj, similarity)
as
SELECT x.docid, y.docid, SUM(x.count * y.count)
FROM frequency x, frequency y
WHERE x.term = y.term and x.docid < y.docid
GROUP BY x.docid, y.docid;

-- i
-- Find the best matching document to the keyword query "washington taxes treasury". You can add this set of keywords to the document corpus with a union of scalar queries:

CREATE VIEW new_freq(docid, term, count)
as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count


SELECT x.docid, y.docid, SUM(x.count * y.count)
FROM new_freq x, new_freq y
WHERE x.term = y.term and x.docid = 'q'
GROUP BY x.docid, y.docid
ORDER BY sum DESC;

