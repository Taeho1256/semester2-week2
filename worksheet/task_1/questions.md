You are working with a database used by a university library system.  
The system tracks library members, books, and borrowing activity.

The database contains the following tables:

members(<u>member_id</u>, member_name, join_date)  
books(<u>book_id</u>, title, author)  
loans(<u>loan_id</u>, member_id, book_id, loan_date, return_date)

---

a) For each pair of tables below, state the type of relationship  
(one-to-one, one-to-many, or many-to-many) and briefly explain your reasoning.

i. Members and loans [2]  
ii. Books and loans [2]  
iii. Members and books [2]  

i. One-to-Many: One member can have many loans.
ii. One-to-Many: One book can be borrowed many times.
iii. Many-to-Many: Many members borrow many books

---

b) A query joins members to loans using an INNER JOIN.

i. Explain what happens to members who have never borrowed a book. [2]  
ii. Explain how the results of the query would change if a LEFT JOIN were used instead. [2]  

i. INNER JOIN: Non-borrowers are excluded (no match found).
ii. LEFT JOIN: All members appear. Non-borrowers show NULL for loan data.
---

c) The head librarian would like to see how many books have been borrowed by each library member.

i. Write an SQL query which would show the name of each library member and how many loans they have taken out. [5]  

SELECT m.member_name, COUNT(l.loan_id) AS total_loans
FROM members m
LEFT JOIN loans l ON m.member_id = l.member_id
GROUP BY m.member_name;
---

d) The head librarian asks:  
“Why don’t you store the book title with the loan? Wouldn’t that make it easier to see the data?”

i. Explain, using appropriate non-technical language, why this would be bad database design. [5]

Duplication: Storing something 100 times wastes space.
Hard to Update: If you fix a typo in a title, you must change it in every loan record.
Messy Data: It’s easier to keep book details in one list and loan records in another.