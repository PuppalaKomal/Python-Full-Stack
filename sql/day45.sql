create database student_instagramDB;

use student_instagramDB;
-- USERS TABLE
CREATE TABLE USERS(USERID INT PRIMARY KEY AUTO_INCREMENT,
					USERNAME VARCHAR(50) UNIQUE NOT NULL, 
                    EMAIL VARCHAR(100) UNIQUE NOT NULL, 
                    PASSWORD VARCHAR(20) NOT NULL, 
                    BIO TEXT, 
                    CREATESAT DATETIME DEFAULT current_timestamp);
-- POSTS TABLE
CREATE TABLE POSTS(POSTID BIGINT PRIMARY KEY AUTO_INCREMENT,
					USERID INT,
                    CAPTION TEXT,
                    LIKES_COUNT INT DEFAULT 0,
                    CREATEDAT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    foreign key(USERID) REFERENCES USERS(USERID)
                    );
-- COMMENTS TABLE
CREATE TABLE COMMENTS(COMMENTID INT PRIMARY KEY AUTO_INCREMENT,
						POSTID BIGINT,
                        USERID INT,
                        COMMENTTEXT VARCHAR(255) NOT NULL,
                        CREATEDAT DATETIME DEFAULT CURRENT_TIMESTAMP,
                        foreign key(POSTID) REFERENCES POSTS(POSTID),
                        foreign key(USERID) REFERENCES USERS(USERID)
                        );
INSERT INTO USERS(USERNAME, EMAIL, PASSWORD, BIO) VALUES
('rahul_01','rahul01@gmail.com','rahul123','Tech Enthusiast'),
('sneha_dev','sneha@gmail.com','sneha123','Frontend Developer'),
('arjun_codes','arjun@gmail.com','arjun123','Python Developer'),
('meena_art','meena@gmail.com','meena123','Artist & Designer'),
('kiran_db','kiran@gmail.com','kiran123','Database Learner'),
('pooja_ui','pooja@gmail.com','pooja123','UI/UX Designer'),
('vijay_ml','vijay@gmail.com','vijay123','Machine Learning Student'),
('anita_writer','anita@gmail.com','anita123','Content Writer'),
('rohit_dev','rohit@gmail.com','rohit123','Full Stack Learner'),
('komal_sql','komal@gmail.com','komal123','SQL & Data Enthusiast');

INSERT INTO POSTS(USERID, CAPTION, LIKES_COUNT) VALUES
(1,'Learning SQL joins today!',25),
(2,'Built my first HTML website!',40),
(3,'Python automation script completed.',35),
(4,'New digital artwork uploaded.',50),
(5,'Practicing MySQL queries.',20),
(6,'Working on UI design project.',45),
(7,'Training my ML model today.',30),
(8,'Published my new blog article.',15),
(9,'Started learning backend development.',28),
(10,'Completed SQL subqueries practice.',60);

INSERT INTO POSTS(USERID, CAPTION, LIKES_COUNT) VALUES
(2,'Exploring CSS Flexbox today.',32),
(3,'Debugging my Python project.',18),
(4,'Uploaded a new sketch artwork.',41),
(5,'Learning database normalization.',22),
(6,'Designing mobile app UI.',37),
(7,'Running my first ML experiment.',29),
(8,'Writing an article on tech trends.',14),
(9,'Learning REST APIs.',26),
(10,'Practicing SQL functions.',39),
(1,'Started learning JavaScript.',21),
(2,'Building a responsive webpage.',33),
(3,'Working with Python loops.',24),
(4,'Painting a digital portrait.',47),
(5,'SQL joins practice today.',19),
(6,'Creating wireframes for app.',35),
(7,'Deep learning basics study.',27),
(8,'Content writing tips post.',16),
(9,'Backend API testing.',31),
(10,'Working with SQL indexes.',42),
(1,'Learning Git and GitHub.',23);

INSERT INTO COMMENTS(POSTID, USERID, COMMENTTEXT) VALUES
(1,2,'Great work!'),
(1,3,'Very helpful post.'),
(2,4,'Nice website design.'),
(3,5,'Python is powerful!'),
(4,6,'Amazing artwork!'),
(5,7,'Keep learning SQL.'),
(6,8,'UI looks clean and modern.'),
(7,9,'Machine learning is interesting!'),
(8,10,'Good blog post.'),
(9,1,'Backend is fun to learn!');

INSERT INTO COMMENTS(POSTID, USERID, COMMENTTEXT) VALUES
(10,3,'Nice explanation!'),
(11,4,'Very informative post.'),
(12,5,'Good practice example.'),
(13,6,'Looks amazing!'),
(14,7,'Database concepts are useful.'),
(15,8,'Great UI design.'),
(16,9,'ML projects are exciting.'),
(17,10,'Interesting article.'),
(18,1,'APIs are very important.'),
(19,2,'SQL functions are powerful.'),
(20,3,'JavaScript is fun.'),
(21,4,'Responsive design looks great.'),
(22,5,'Python loops are easy to understand.'),
(23,6,'Beautiful artwork.'),
(24,7,'Joins are important in SQL.'),
(25,8,'Nice wireframe design.'),
(26,9,'Deep learning is fascinating.'),
(27,10,'Helpful writing tips.'),
(28,1,'API testing is useful skill.'),
(29,2,'Indexes improve performance.');

select * from users;
select * from posts;
select * from comments;

-- total number of users
select count(userid) as countusers from users;
-- total number of posts
select count(postid) as post_count from posts;
-- average likes per post(rounded to 2 decimal places)
select round(avg(likes_count),2) as Avg_like_per_post from posts;
-- maximum followers count
select *from posts where likes_count= (select max(likes_count)from posts order by );
-- minimum post count by a user
SELECT u.userid, u.username, COUNT(*) AS post_count
FROM posts p
INNER JOIN users u
ON u.userid = p.userid
GROUP BY u.userid, u.username;

