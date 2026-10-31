"""Computer Science XI — Unit 4: Data and Analysis (book 139-173)."""
from .common import bq, mcq

ITEMS = []

# A. MCQs — PDF 176-177 (book 171-172)
ITEMS += [
    mcq(4, 'A', 'i', 'Which of the following is a DBMS?',
        [('a', 'MS Word'), ('b', 'MS Excel'),
         ('c', 'MS Access'), ('d', 'MS Paint')], 'c',
        'MS Access is a database management system: it stores tables, defines relationships and '
        'supports queries, forms and reports. Word and Paint are text/graphics tools; Excel is a '
        'spreadsheet, not a full DBMS.', 176),
    mcq(4, 'A', 'ii', 'In an ER Model, a rectangle represents:',
        [('a', 'Attribute'), ('b', 'Relationship'),
         ('c', 'Entity'), ('d', 'Key')], 'c',
        'The standard ER notation uses a rectangle for an entity, an ellipse for an attribute, a '
        'diamond for a relationship and an underlined attribute for the primary key.', 176),
    mcq(4, 'A', 'iii', 'A one-to-many relationship means',
        [('a', 'One record relates to many'), ('b', 'Many to one only'),
         ('c', 'One to One'), ('d', 'None')], 'a',
        'In a 1:M relationship one record in the first table can be related to many records in the '
        'second (e.g. one class has many students), while each record in the second table relates '
        'to only one in the first.', 176),
    mcq(4, 'A', 'iv', 'Which object is used to retrieve data?',
        [('a', 'Table'), ('b', 'Form'),
         ('c', 'Query'), ('d', 'Report')], 'c',
        'A query asks the database for records that meet a condition and can combine fields from '
        'several tables. Forms are for data entry, reports for formatted output.', 177),
    mcq(4, 'A', 'v', 'Which function calculates average?',
        [('a', 'Sum()'), ('b', 'Count()'),
         ('c', 'Avg()'), ('d', 'Max()')], 'c',
        'Avg() (AVG in SQL) returns the arithmetic mean of a numeric field. Sum adds, Count counts '
        'records and Max returns the largest value.', 177),
    mcq(4, 'A', 'vi', 'Which key uniquely identifies each record in a table?',
        [('a', 'Foreign Key'), ('b', 'Primary Key'),
         ('c', 'Alternate Key'), ('d', 'Candidate Key')], 'b',
        'The primary key is the chosen candidate key whose value is unique and never null for every '
        'record. A foreign key refers to a primary key in another table. Note: a candidate key also '
        'uniquely identifies records; a primary key is the particular candidate key chosen for that role, '
        'so (b) is the conventional answer while (d) is technically also unique.', 177),
    mcq(4, 'A', 'vii', 'Which relationship requires a junction table?',
        [('a', 'One-to-One'), ('b', 'One-to-Many'),
         ('c', 'Many-to-Many'), ('d', 'None')], 'c',
        'A many-to-many relationship cannot be stored directly in two tables without duplication. A '
        'junction (link) table holds the pairs of keys, turning it into two one-to-many relationships.', 177),
    mcq(4, 'A', 'viii', 'Which database objects provides a user friendly interface for data entry?',
        [('a', 'Query'), ('b', 'Table'),
         ('c', 'Report'), ('d', 'Form')], 'd',
        'A form presents fields on screen with labels, controls and validation, so users can enter '
        'or edit records without working directly in the table grid.', 177),
    mcq(4, 'A', 'ix', 'Which chart is best used to show trends over time?',
        [('a', 'Pie Chart'), ('b', 'Bar Chart'),
         ('c', 'Line Chart'), ('d', 'Column Chart')], 'c',
        'A line chart plots values against time, making upward or downward trends easy to see. Pie '
        'charts show parts of a whole and bar/column charts compare categories.', 177),
    mcq(4, 'A', 'x', 'Which query operation combines records into categories for summarization?',
        [('a', 'Sorting'), ('b', 'Filtering'),
         ('c', 'Group by'), ('d', 'Validation')], 'c',
        'GROUP BY collects records that share a field value into one group, so aggregate functions '
        '(Count, Sum, Avg) can be applied per group, e.g. students per department.', 177),
]

# B. Fill in the Blanks — PDF 177 (book 172)
ITEMS += [
    bq(4, 'B', 'i', 'In a relational database, a ____________ key is used to establish a link between '
       'two tables by referring to the primary key of another table.',
       'foreign',
       'A foreign key is a field in one table whose values must match the primary key values of '
       'another table; it creates the relationship between the two tables.', 177),
    bq(4, 'B', 'ii', 'If two entities are connected through an intermediate entity instead of directly, '
       'this usually indicates the resolution of a ____________ relationship.',
       'many-to-many',
       'A many-to-many relationship is resolved by introducing an intermediate (junction) entity '
       'that has one-to-many links to each of the original entities.', 177),
    bq(4, 'B', 'iii', 'When a record in one table is deleted, and related records in another table must '
       'also be removed automatically, this is controlled through ____________ rules.',
       'cascade delete',
       'Cascade delete is a referential-integrity rule: deleting the parent record automatically '
       'deletes the child records that refer to it, preventing orphan records.', 177),
    bq(4, 'B', 'iv', 'A table created to resolve a many-to-many relationship is commonly referred to as '
       'a ____________ table.',
       'junction (link / bridge / associative)',
       'A junction table stores the foreign keys of both entities, and each row represents one '
       'association between them (e.g. Enrollment linking Student and Course).', 177),
    bq(4, 'B', 'v', 'A candidate key that is not chosen as the primary key is known as ____________.',
       'an alternate key',
       'A table may have several candidate keys (each unique and minimal). One becomes the primary '
       'key; the remaining candidate keys are alternate keys.', 177),
]

# C. Short answers — PDF 177 (book 172)
ITEMS += [
    bq(4, 'C', 'i', 'Differentiate between a field and a record.',
       'A field is a single column of a table: one attribute of the entity, with a defined data type '
       '(e.g. StudentName or Marks). It describes WHAT kind of data is stored.\n'
       'A record is a single row of a table: one complete entity instance, containing one value for '
       'each field (e.g. one student\'s name, roll number, class and marks).\n'
       'So a field is a property across many records, while a record is one item across many fields.',
       'Field = column (attribute); record = row (entity instance). The intersection of a record and '
       'a field holds one value.', 177),
    bq(4, 'C', 'ii', 'What is referential integrity?',
       'Referential integrity is a database rule that every foreign-key value must either match an '
       'existing primary-key value in the related table or be null. It prevents orphan records \u2014 '
       'for example, it stops a student record from referring to a class that does not exist.\n'
       'The DBMS enforces it when records are inserted, updated or deleted, often with cascade '
       'update and cascade delete rules.',
       'Referential integrity keeps relationships consistent across tables: a child row cannot '
       'point to a missing parent row.', 177),
    bq(4, 'C', 'iii', 'Explain the role of a Database Management System (DBMS).',
       'A DBMS is software that creates, stores, manages and secures databases and provides an '
       'interface between users/applications and the data. Its roles include:\n'
       '\u2022 defining the database structure (tables, fields, keys, relationships);\n'
       '\u2022 inserting, updating, deleting and retrieving data;\n'
       '\u2022 enforcing integrity rules (primary keys, referential integrity, validation);\n'
       '\u2022 controlling concurrent access so multiple users do not corrupt data;\n'
       '\u2022 providing security through user accounts and permissions;\n'
       '\u2022 backup and recovery after failures;\n'
       '\u2022 supporting queries, forms and reports.\n'
       'Examples: MS Access, MySQL, SQL Server, Oracle.',
       'The DBMS centralizes data management so applications do not need to implement storage, '
       'locking, security or recovery themselves.', 177),
    bq(4, 'C', 'iv', 'Explain a one-to-many relationship with an example.',
       'In a one-to-many (1:M) relationship, one record in table A can be associated with many '
       'records in table B, but each record in B is associated with at most one record in A.\n'
       'Example: one Class has many Students, while each Student belongs to exactly one Class. The '
       'Class table has a primary key ClassID; the Student table contains ClassID as a foreign key.\n'
       'Other examples: one Department has many Employees; one Customer places many Orders.',
       'The "one" side holds the primary key; the "many" side holds the matching foreign key. No '
       'junction table is needed for 1:M.', 177),
    bq(4, 'C', 'v', 'Define data visualization and give one example.',
       'Data visualization is the presentation of data in a graphical form \u2014 charts, graphs, maps, '
       'dashboards or infographics \u2014 so that patterns, trends, comparisons and outliers can be '
       'understood quickly.\n'
       'Example: a line chart of monthly sales over one year shows whether sales are rising or '
       'falling; a pie chart shows each department\'s share of the total budget.',
       'Visualization does not replace the data; it makes the meaning of the data easier for people '
       'to see and act on.', 177),
]

# D. Detailed answers — PDF 178 (book 173)
ITEMS += [
    bq(4, 'D', 'i', 'Define data and information with examples. Also explain the concept of a database '
       'and its advantages.',
       'Data are raw, unprocessed facts and figures without context: 42, 75, "Ali", 2026-10-25.\n'
       'Information is data that has been processed, organized and interpreted so it has meaning: '
       '"Ali scored 75 out of 100 in 2026" or "average marks = 68%". Information supports decisions.\n'
       'Example: the individual marks 60, 70, 80 are data; the average 70 and the statement "the '
       'class average is 70" are information.\n'
       'A database is an organized collection of related data stored so that it can be accessed, '
       'managed and updated efficiently. It is usually organized into tables with rows (records) '
       'and columns (fields), with keys defining the relationships.\n'
       'Advantages of a database:\n'
       '\u2022 reduces data redundancy (data stored once, not in many files);\n'
       '\u2022 maintains consistency (one update is seen everywhere);\n'
       '\u2022 enforces integrity and validation rules;\n'
       '\u2022 supports sharing by many users and applications;\n'
       '\u2022 provides security, backup and recovery;\n'
       '\u2022 allows powerful queries and reports;\n'
       '\u2022 separates data from programs, so applications can change without rewriting the data.',
       'Data becomes information after processing. A database solves the duplication and '
       'inconsistency problems of separate flat files.', 178),
    bq(4, 'D', 'ii', 'What is a Database Management System (DBMS)? Explain its functions and advantages.',
       'A DBMS is the software layer that creates, stores, controls and protects a database and '
       'lets users and programs work with the data. Examples: MS Access, MySQL, SQL Server, Oracle.\n'
       'Functions:\n'
       '1. Data definition \u2014 create and modify tables, fields, data types, keys and relationships.\n'
       '2. Data manipulation \u2014 insert, update, delete and retrieve records (often through SQL).\n'
       '3. Query processing \u2014 interpret queries, optimize them and return results.\n'
       '4. Integrity enforcement \u2014 apply primary keys, foreign keys, validation and cascade rules.\n'
       '5. Concurrency control \u2014 allow many users to work at once without conflicts (locking, '
       'transactions).\n'
       '6. Security \u2014 authenticate users and grant or deny permissions on objects.\n'
       '7. Backup and recovery \u2014 restore the database after a failure.\n'
       '8. Data dictionary/metadata \u2014 keep descriptions of the structure of the database.\n'
       'Advantages: reduced redundancy and inconsistency, controlled sharing, better security, '
       'enforced standards, backup/recovery, data independence and easier reporting. Disadvantages '
       'can include cost, complexity and the need for skilled administration.',
       'The DBMS provides the services that a raw file system lacks: structure, integrity, '
       'concurrency, security and recovery.', 178),
    bq(4, 'D', 'iii', 'Explain the Entity-Relationship (ER) Model. Define entities, attributes, and '
       'relationships with suitable examples.',
       'The Entity-Relationship (ER) Model is a conceptual design method that represents a system '
       'as entities, their attributes and the relationships between them. It is drawn as an ER '
       'diagram before the tables are created.\n'
       'Entity \u2014 a real-world object or concept about which data is stored. Drawn as a rectangle. '
       'Examples: Student, Course, Teacher.\n'
       'Attribute \u2014 a property of an entity. Drawn as an ellipse connected to the entity. '
       'Example: Student has RollNo, Name, Class, Marks. The attribute that uniquely identifies an '
       'entity instance (RollNo) is underlined as the primary key.\n'
       'Relationship \u2014 an association between two entities. Drawn as a diamond with lines to the '
       'entities, and labelled with its cardinality. Examples: Student "enrolls in" Course, Teacher '
       '"teaches" Course, a Student "belongs to" a Class.\n'
       'Cardinality:\n'
       '\u2022 one-to-one (1:1) \u2014 one Student has one AdmissionRecord;\n'
       '\u2022 one-to-many (1:M) \u2014 one Class contains many Students;\n'
       '\u2022 many-to-many (M:N) \u2014 many Students enroll in many Courses, resolved by an '
       'Enrollment junction entity.\n'
       'Example ER for a school: Student (RollNo, Name, ClassID) \u2014 many students belong to one '
       'Class; Teacher (TeacherID, Name) teaches Course (CourseID, Title); Student enrolls in Course '
       'through Enrollment (RollNo, CourseID, Grade).',
       'The ER model focuses on WHAT data exists and how it is related, not on the physical storage; '
       'the diagram is then converted to relational tables.', 178),
]

# E. Activities — PDF 178 (book 173)
ITEMS += [
    bq(4, 'E', 1, 'Create a Student table in MS Access with at least five fields and assign an '
       'appropriate primary key.',
       'Table design:\n'
       'Field Name | Data Type | Notes\n'
       'RollNo | Short Text (or Number) | Primary key, unique student number\n'
       'StudentName | Short Text | required\n'
       'Class | Short Text | e.g. "XI-A"\n'
       'Gender | Short Text | validation: M/F\n'
       'DateOfBirth | Date/Time | \n'
       'Marks | Number | validation: 0-100\n'
       'Steps in Access: Create > Table Design; enter the six fields and data types; select RollNo '
       'and click Primary Key; save the table as Student; switch to Datasheet View and enter records.',
       'RollNo is the primary key because no two students share the same roll number and it is never '
       'null. The remaining fields store the attributes of each student.', 178),
    bq(4, 'E', 2, 'Design an Entity-Relationship (ER) diagram for a school database showing the '
       'entities Student, Course, and Teacher along with their relationships.',
       'Entities and attributes:\n'
       'Student (RollNo underlined, Name, Class)\n'
       'Teacher (TeacherID underlined, Name, Department)\n'
       'Course (CourseID underlined, Title, CreditHours)\n'
       'Relationships:\n'
       '\u2022 Teacher \u2014 teaches \u2014 Course: one teacher can teach many courses, and a course is taught '
       'by one teacher (1:M).\n'
       '\u2022 Student \u2014 enrolls in \u2014 Course: many students enroll in many courses (M:N), resolved '
       'by the junction entity Enrollment (RollNo, CourseID, Grade).\n'
       'Diagram notation: rectangles for Student, Teacher, Course; ellipses for attributes; diamonds '
       'for "teaches" and "enrolls"; 1/M labels on the connecting lines; underline RollNo, TeacherID '
       'and CourseID as primary keys.',
       'The M:N relationship must be resolved with Enrollment, which holds the foreign keys to both '
       'Student and Course.', 178),
    bq(4, 'E', 3, 'Create a data entry form for the Student table using the Form Wizard, and use it '
       'to enter student records.',
       'Steps in MS Access:\n'
       '1. Select the Student table in the Navigation Pane.\n'
       '2. Choose Create > Form Wizard.\n'
       '3. Select the fields to display (RollNo, StudentName, Class, Gender, DateOfBirth, Marks) and '
       'click Next.\n'
       '4. Choose the layout (Columnar) and style, then click Next.\n'
       '5. Name the form frmStudent and click Finish.\n'
       '6. The form opens in Form View: type the values in the fields and press Tab; the record is '
       'saved when you move to the next record.\n'
       '7. Use the navigation buttons at the bottom to move between existing records.',
       'A form does not change the table; it is an interface that reads and writes rows of the '
       'underlying Student table with validation applied.', 178),
    bq(4, 'E', 4, 'Create queries to retrieve student records by displaying selected fields, applying '
       'filters, and using both AND and OR conditions.',
       'Query 1 \u2014 selected fields: select StudentName, Class, Marks from Student; display only '
       'those columns.\n'
       'Query 2 \u2014 AND filter: Class = "XI-A" AND Marks >= 60. Only students of XI-A who scored 60 '
       'or more are returned (both conditions must be true).\n'
       'Query 3 \u2014 OR filter: Class = "XI-A" OR Class = "XI-B". Students from either class are '
       'returned (at least one condition is true).\n'
       'SQL equivalents:\n'
       'SELECT StudentName, Class, Marks FROM Student;\n'
       'SELECT * FROM Student WHERE Class = \'XI-A\' AND Marks >= 60;\n'
       'SELECT * FROM Student WHERE Class = \'XI-A\' OR Class = \'XI-B\';\n'
       'In Access Design View, enter the criteria in the Criteria row of each field; criteria on '
       'different fields on the same row are combined with AND, while criteria on separate rows '
       'are combined with OR.',
       'AND narrows the result (both conditions), OR broadens it (either condition).', 178),
    bq(4, 'E', 5, 'Generate a grouped query to summarize the number of students in each department, '
       'and present the results using a suitable chart (bar or pie chart).',
       '1. Add a Department field (Short Text) to the Student table if it is not already present, '
       'then create a query based on Student.\n'
       '2. On the Query Design toolbar click Totals.\n'
       '3. Drag Department to the first column and set its Total row to Group By.\n'
       '4. Drag RollNo to the second column and set its Total row to Count (Count Of RollNo).\n'
       '5. Run the query; it returns one row per department with the number of students.\n'
       'SQL: SELECT Department, COUNT(RollNo) AS StudentCount FROM Student GROUP BY Department;\n'
       '6. With the query open, choose Insert > Chart (or Create > Chart) and select a bar chart for '
       'comparing departments or a pie chart for showing each department\'s share of the total.\n'
       'Sample result: Computer Science 40, Biology 35, Commerce 50, Arts 25.',
       'GROUP BY collapses each department into one row so COUNT counts the students per group. A '
       'bar chart compares departments directly; a pie chart shows proportions.', 178),
]
