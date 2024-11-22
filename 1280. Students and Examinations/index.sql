SELECT 
    S.student_id
    ,S.student_name 
    ,Su.subject_name
    ,Count(E.student_id) as attended_exams
From Students S
Cross Join Subjects Su
Left Join Examinations E
On S.student_id = E.student_id
And Su.subject_name = E.subject_name
Group by S.student_id, S.student_name, Su.subject_name
Order by S.student_id, S.student_name, Su.subject_name