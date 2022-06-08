# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

DELETE p2 FROM Person p1
join person p2 
where p1.email = p2.email and p1.id < p2.id