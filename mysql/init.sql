CREATE DATABASE IF NOT EXISTS game_db;
use game_db;

SET global general_log = on;

-- ###################################################################
-- table users
-- ###################################################################
CREATE TABLE IF NOT EXISTS users (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(110) NOT NULL,
    right_id SMALLINT UNSIGNED NOT NULL,
    username VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    can_edit SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    can_seelog SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    can_seeusers SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    hide SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    log_user_id INT UNSIGNED NOT NULL DEFAULT 0,
    log_comment VARCHAR(255) NOT NULL DEFAULT "",
    PRIMARY KEY (id),
    INDEX rights (right_id)
);

CREATE TABLE IF NOT EXISTS users_log (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    email VARCHAR(255),
    right_id SMALLINT UNSIGNED,
    username VARCHAR(100),
    position VARCHAR(100),
    can_edit SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    can_seelog SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    can_seeusers SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    hide SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    log_user_id INT UNSIGNED DEFAULT 0,
    log_comment VARCHAR(255) DEFAULT "",
    PRIMARY KEY (id),
    INDEX rights (right_id),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER users_log_ai AFTER INSERT ON users FOR EACH ROW
INSERT INTO users_log(logger_event, log_id, email, right_id, username,
          position, can_edit, can_seelog, can_seeusers,
          hide, log_user_id, log_comment)
    VALUES (
           "insert",
           NEW.id,
           NEW.email,
           NEW.right_id,
           NEW.username,
           NEW.position,
           NEW.can_edit,
           NEW.can_seelog,
           NEW.can_seeusers,
           NEW.hide,
           NEW.log_user_id,
           NEW.log_comment
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER users_log_au AFTER UPDATE ON users FOR EACH ROW
INSERT INTO users_log(logger_event, log_id, email, right_id, username,
          position, hide, can_edit, can_seelog, can_seeusers,
          log_user_id, log_comment)
    VALUES (
           "update",
           NEW.id,
           NEW.email,
           NEW.right_id,
           NEW.username,
           NEW.position,
           NEW.can_edit,
           NEW.can_seelog,
           NEW.can_seeusers,
           NEW.hide,
           NEW.log_user_id,
           NEW.log_comment
           );;
DELIMITER ;

-- ###################################################################
-- table rights
-- ###################################################################

CREATE TABLE IF NOT EXISTS rights(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_right VARCHAR(20) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (user_right)
);

CREATE TABLE IF NOT EXISTS rights_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    user_right VARCHAR(20) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (user_right),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER rights_log_ai AFTER INSERT ON rights FOR EACH ROW
INSERT INTO rights_log(logger_event, log_id, user_right, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.user_right,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER rights_log_au AFTER UPDATE ON rights FOR EACH ROW
INSERT INTO rights_log(logger_event, log_id, user_right, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.user_right,
           NEW.log_user_id
           );;
DELIMITER ;

INSERT IGNORE INTO rights ( user_right) VALUES ("blocked");
INSERT IGNORE INTO rights ( user_right) VALUES ("player");
INSERT IGNORE INTO rights ( user_right) VALUES ("operator");
INSERT IGNORE INTO rights ( user_right) VALUES ("manager");
INSERT IGNORE INTO rights ( user_right) VALUES ("admin");

-- ###################################################################
-- table question_levels
-- ###################################################################

CREATE TABLE IF NOT EXISTS question_levels(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    question_level INT UNSIGNED DEFAULT 0,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (question_level)
);

CREATE TABLE IF NOT EXISTS question_levels_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    question_level VARCHAR(20) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (question_level),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER question_levels_log_ai AFTER INSERT ON question_levels FOR EACH ROW
INSERT INTO question_levels_log(logger_event, log_id, question_level, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.question_level,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER question_levels_log_au AFTER UPDATE ON question_levels FOR EACH ROW
INSERT INTO question_levels_log(logger_event, log_id, question_level, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.question_level,
           NEW.log_user_id
           );;
DELIMITER ;

INSERT IGNORE INTO question_levels ( question_level) VALUES (1);
INSERT IGNORE INTO question_levels ( question_level) VALUES (2);
INSERT IGNORE INTO question_levels ( question_level) VALUES (3);
INSERT IGNORE INTO question_levels ( question_level) VALUES (4);
INSERT IGNORE INTO question_levels ( question_level) VALUES (5);
INSERT IGNORE INTO question_levels ( question_level) VALUES (6);
INSERT IGNORE INTO question_levels ( question_level) VALUES (7);
INSERT IGNORE INTO question_levels ( question_level) VALUES (8);
INSERT IGNORE INTO question_levels ( question_level) VALUES (9);
INSERT IGNORE INTO question_levels ( question_level) VALUES (10);
INSERT IGNORE INTO question_levels ( question_level) VALUES (11);
INSERT IGNORE INTO question_levels ( question_level) VALUES (12);
INSERT IGNORE INTO question_levels ( question_level) VALUES (13);
INSERT IGNORE INTO question_levels ( question_level) VALUES (14);
INSERT IGNORE INTO question_levels ( question_level) VALUES (15);

-- ###################################################################
-- table question_difficulties
-- ###################################################################

CREATE TABLE IF NOT EXISTS question_difficulties(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    difficulty int NOT NULL,
    difficulty_name VARCHAR(10) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (difficulty),
    UNIQUE (difficulty_name)
);

CREATE TABLE IF NOT EXISTS question_difficulties_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    difficulty int NOT NULL,
    difficulty_name VARCHAR(10) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (difficulty),
    UNIQUE (difficulty_name),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER question_difficulties_log_ai AFTER INSERT ON question_difficulties FOR EACH ROW
INSERT INTO question_difficulties_log(logger_event, log_id, difficulty, difficulty_name, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.difficulty,
           NEW.difficulty_name,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER question_difficulties_log_au AFTER UPDATE ON question_difficulties FOR EACH ROW
INSERT INTO question_difficulties_log(logger_event, log_id, difficulty, difficulty_name, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.difficulty,
           NEW.difficulty_name,
           NEW.log_user_id
           );;
DELIMITER ;

INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name) VALUES (0, "warm up");
INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name) VALUES (1, "2-5 Easy");
INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name) VALUES (2, "6-10 Average");
INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name) VALUES (3, "11-14 Difficult");
INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name) VALUES (4, "15");


-- ###################################################################
-- table chapters
-- ###################################################################

CREATE TABLE IF NOT EXISTS chapters(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    chapter INT NOT NULL,
    chapter_name VARCHAR(255) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (chapter),
    UNIQUE (chapter_name)
);

CREATE TABLE IF NOT EXISTS chapters_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    chapter INT NOT NULL,
    chapter_name VARCHAR(255) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (chapter),
    UNIQUE (chapter_name),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER chapters_log_ai AFTER INSERT ON chapters FOR EACH ROW
INSERT INTO chapters_log(logger_event, log_id, chapter, chapter_name, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.chapter,
           NEW.chapter_name,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER chapters_log_au AFTER UPDATE ON chapters FOR EACH ROW
INSERT INTO chapters_log(logger_event, log_id, chapter, chapter_name, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.chapter,
           NEW.chapter_name,
           NEW.log_user_id
           );;
DELIMITER ;

INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (1, "Roles and Responsibilities");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (2, "Well-Being of the Emergency Responder");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (3, "Patient Assesment");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (4, "Respiratory Emergencies");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (5, "Supplementary Oxygen");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (6, "Cardiovascular Emergencies");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (7, "Trauma");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (8, "Medical Conditions");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (9, "Musculoskeletal Injuries");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (10, "Environmental Emergencies");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (11, "Special Populations");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (12, "Special Situations");
INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (13, "Appendix");

-- ###################################################################
-- table sub-chapters
-- ###################################################################

CREATE TABLE IF NOT EXISTS sub_chapters(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    chapter_id int,
    sub_chapter INT NOT NULL,
    sub_chapter_name VARCHAR(255) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (sub_chapter_name)
);

CREATE TABLE IF NOT EXISTS sub_chapters_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    chapter_id int,
    sub_chapter INT NOT NULL,
    sub_chapter_name VARCHAR(255) NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (sub_chapter_name),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER sub_chapters_log_ai AFTER INSERT ON sub_chapters FOR EACH ROW
INSERT INTO sub_chapters_log(logger_event, log_id, chapter_id, sub_chapter, sub_chapter_name, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.chapter_id,
           NEW.sub_chapter,
           NEW.sub_chapter_name,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER sub_chapters_log_au AFTER UPDATE ON sub_chapters FOR EACH ROW
INSERT INTO sub_chapters_log(logger_event, log_id, chapter_id, sub_chapter, sub_chapter_name, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.chapter_id,
           NEW.sub_chapter,
           NEW.sub_chapter_name,
           NEW.log_user_id
           );;
DELIMITER ;

INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 1, "The Emergency Medical System");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 2, "Legal and Ethical Issues");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 3, "Communication");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 4, "Documentation and Record Keeping");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 1, "Health andd Well-Being");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 2, "Critical Incident Stress");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 3, "Infection Control");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 1, "Emergency Scene Management and Primary Assessment");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 2, "Secondary Assessment");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 3, "Lifting and Carrying");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 4, "Multiple Patient Incidents");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 1, "Respiratory Disease");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 2, "Airway Obstructions");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 3, "Establishing and Maintaining the Airway");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (5, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (5, 1, "Oxygen Administration");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (5, 2, "Artificital Ventilation");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 1, "Cardiovascular Disease");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 2, "Cerebrovascular Emergencies (Stroke/TIA)");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 3, "Cardiopulmonary Resuscitation");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 4, "Automated External Defibrillation");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 1, "Shock");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 2, "Wound Management");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 3, "Eye Injuries");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 4, "Burns");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 5, "Chest Injuries");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 6, "Gastrointestinal and Genitourinary");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 7, "Dental Emergencies");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 1, "Diabetes");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 2, "Seizures");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 3, "Unconsciousness and Fainting");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 4, "General Pharmacology");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (9, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (9, 1, "Head, Spinal and Pelvic Injuries");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (9, 2, "Bone, Joint and Muscle Injuries");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 1, "Heat and Cold-Related Emergencies");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 2, "Poisons, Bites and Stings");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 3, "Aquatic Emergencies");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 1, "Emergency Childbirth, Miscarriage and Neonates");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 2, "Pediatric Patients");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 3, "Geriatric Patients");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 4, "Bariatric Patients");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 5, "Special Needs and Palliative Care");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 6, "Behavioral Emergencies");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 7, "Substance Abuse");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 1, "Special Rescue Situations");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 2, "Chemical, Biological, Radiological, Nuclear and Explosive Events (CBRNE)");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 3, "Extended Patient Care");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 4, "Maintaining Peripheral IVS");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 5, "Death in Remote Areas");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 6, "First Aid Stations and Rooms");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 7, "Ambulance Operations and Maintenance");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (13, 0, "All");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (13, 1, "Anatomy and Physiology");
INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (13, 2, "Medical Terminology");


-- ###################################################################
-- table questions
-- ###################################################################

CREATE TABLE IF NOT EXISTS questions(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    level_id INT,
    difficulty_id INT,
    chapter_id INT,
    sub_chapter_id INT,
    question VARCHAR(255) NOT NULL,
    image_file VARCHAR(20) NOT NULL DEFAULT 'default.jpg',
    answer_A VARCHAR(255) NOT NULL,
    answer_B VARCHAR(255) NOT NULL,
    answer_C VARCHAR(255) NOT NULL,
    answer_D VARCHAR(255) NOT NULL,
    answer_time INT NOT NULL DEFAULT 60,
    correct_answer VARCHAR(1) NOT NULL,
    correct_answer_text VARCHAR(255) NOT NULL,
    answer_img VARCHAR(20) NOT NULL DEFAULT 'default.jpg',
    is_validated SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS questions_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    level_id INT,
    difficulty_id INT,
    chapter_id INT,
    sub_chapter_id INT,
    question VARCHAR(255) NOT NULL,
    image_file VARCHAR(20) NOT NULL DEFAULT 'default.jpg',
    answer_A VARCHAR(255) NOT NULL,
    answer_B VARCHAR(255) NOT NULL,
    answer_C VARCHAR(255) NOT NULL,
    answer_D VARCHAR(255) NOT NULL,
    correct_answer VARCHAR(1) NOT NULL,
    correct_answer_text VARCHAR(255) NOT NULL,
    answer_time INT NOT NULL DEFAULT 60,
    answer_img VARCHAR(20) NOT NULL DEFAULT 'default.jpg',
    is_validated SMALLINT UNSIGNED NOT NULL DEFAULT 0,

    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER questions_log_ai AFTER INSERT ON questions FOR EACH ROW
INSERT INTO questions_log(logger_event, log_id, level_id, difficulty_id, chapter_id, sub_chapter_id, question, image_file, answer_A, answer_B, answer_C,
            answer_D, correct_answer, correct_answer_text, answer_time, answer_img, is_validated, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.level_id,
           NEW.difficulty_id,
           NEW.chapter_id,
           NEW.sub_chapter_id,
           NEW.question,
           NEW.image_file,
           NEW.answer_A,
           NEW.answer_B,
           NEW.answer_C,
           NEW.answer_D,
           NEW.correct_answer,
           NEW.correct_answer_text,
           NEW.answer_time,
           NEW.answer_img,
           NEW.is_validated,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER questions_log_au AFTER UPDATE ON questions FOR EACH ROW
INSERT INTO questions_log(logger_event, log_id, level_id, difficulty_id, chapter_id, sub_chapter_id, question, image_file, answer_A, answer_B, answer_C,
            answer_D, correct_answer, correct_answer_text, answer_time, answer_img, is_validated, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.level_id,
           NEW.difficulty_id,
           NEW.chapter_id,
           NEW.sub_chapter_id,
           NEW.question,
           NEW.image_file,
           NEW.answer_A,
           NEW.answer_B,
           NEW.answer_C,
           NEW.answer_D,
           NEW.correct_answer,
           NEW.correct_answer_text,
           NEW.answer_time,
           NEW.answer_img,
           NEW.is_validated,
           NEW.log_user_id
           );;
DELIMITER ;


-- ###################################################################
-- table game_questions
-- ###################################################################

CREATE TABLE IF NOT EXISTS game_questions(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    game_id int NOT NULL,
    question_id int NOT NULL,
    question_order int NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS game_questions_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    game_id int NOT NULL,
    question_id int NOT NULL,
    question_order int NOT NULL,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER game_questions_log_ai AFTER INSERT ON game_questions FOR EACH ROW
INSERT INTO game_questions_log(logger_event, log_id, game_id, question_id, question_order, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.game_id,
           NEW.question_id,
           NEW.question_order,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER game_questions_log_au AFTER UPDATE ON game_questions FOR EACH ROW
INSERT INTO game_questions_log(logger_event, log_id, game_id, question_id, question_order, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.game_id,
           NEW.question_id,
           NEW.question_order,
           NEW.log_user_id
           );;
DELIMITER ;


-- ###################################################################
-- table games
-- ###################################################################

CREATE TABLE IF NOT EXISTS games(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id INT,
    game_uid VARCHAR(5) NOT NULL,
    game_description VARCHAR(255) NOT NULL,
    recommend SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    approved SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    approved_user_id int,
    is_random SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    is_multiplayer SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    number_of_questions INT UNSIGNED DEFAULT 0,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS games_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    user_id INT,
    game_uid VARCHAR(5) NOT NULL,
    game_description VARCHAR(255) NOT NULL,
    recommend SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    approved SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    approved_user_id int,
    is_random SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    is_multiplayer SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER games_log_ai AFTER INSERT ON games FOR EACH ROW
INSERT INTO games_log(logger_event, log_id, user_id, game_uid, game_description,
            recommend, approved, approved_user_id, is_random, is_multiplayer, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.user_id,
           NEW.game_uid,
           NEW.game_description,
           NEW.recommend,
           NEW.approved,
           NEW.approved_user_id,
           NEW.is_random,
           NEW.is_multiplayer,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER games_log_au AFTER UPDATE ON games FOR EACH ROW
INSERT INTO games_log(logger_event, log_id, user_id, game_uid, game_description,
            recommend, approved, approved_user_id, is_random, is_multiplayer, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.user_id,
           NEW.game_uid,
           NEW.game_description,
           NEW.recommend,
           NEW.approved,
           NEW.approved_user_id,
           NEW.is_random,
           NEW.is_multiplayer,
           NEW.log_user_id
           );;
DELIMITER ;


-- ###################################################################
-- table game_plays
-- ###################################################################

CREATE TABLE IF NOT EXISTS game_plays(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id INT,
    player_name VARCHAR(5) NOT NULL,
    player_id INT,
    game_id INT NOT NULL,
    question_id INT NOT NULL,
    answer VARCHAR(1),
    is_answer_correct SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS game_plays_log(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ts TIMESTAMP  DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    logger_event VARCHAR(50),
    log_id INT UNSIGNED,
    user_id INT,
    player_name VARCHAR(5) NOT NULL,
    player_id INT,
    game_id INT NOT NULL,
    question_id INT NOT NULL,
    answer VARCHAR(1),
    is_answer_correct SMALLINT UNSIGNED NOT NULL DEFAULT 0,
    log_user_id INT UNSIGNED DEFAULT 0,
    PRIMARY KEY (id),
    INDEX log_id (log_id),
    INDEX log_user_id (log_user_id)
);

DELIMITER ;;
CREATE TRIGGER game_plays_log_ai AFTER INSERT ON game_plays FOR EACH ROW
INSERT INTO game_plays_log(logger_event, log_id, user_id, player_name, player_id,
            game_id, question_id, answer, is_answer_correct, log_user_id)
    VALUES (
           "insert",
           NEW.id,
           NEW.user_id,
           NEW.player_name,
           NEW.player_id,
           NEW.game_id,
           NEW.question_id,
           NEW.answer,
           NEW.is_answer_correct,
           NEW.log_user_id
           );;
DELIMITER ;
DELIMITER ;;
CREATE TRIGGER game_plays_log_au AFTER UPDATE ON game_plays FOR EACH ROW
INSERT INTO game_plays_log(logger_event, log_id, user_id, player_name, player_id,
            game_id, question_id, answer, is_answer_correct, log_user_id)
    VALUES (
           "update",
           NEW.id,
           NEW.user_id,
           NEW.player_name,
           NEW.player_id,
           NEW.game_id,
           NEW.question_id,
           NEW.answer,
           NEW.is_answer_correct,
           NEW.log_user_id
           );;
DELIMITER ;
