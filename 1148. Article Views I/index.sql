--  Write your MySQL query statement below
Select distinct author_id as id
From Views
Where author_id = viewer_id
Order By author_id ASC
