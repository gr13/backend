import sys
from sqlalchemy.sql import text

from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))


class TestGlobalFixtures():
    """
    Prepares the class before test run
    """
    app = None
    db = None

    @staticmethod
    def add_row_to_table(sql_script):
        """
        Adds one row to a table
        """
        with TestGlobalFixtures.app.app_context():
            TestGlobalFixtures.db.session.execute(text(sql_script))
            TestGlobalFixtures.db.session.commit()

    @staticmethod
    def prepare_table_rights():
        """
        adds rights to the database
        """
        sql_scripts = [
            "INSERT IGNORE INTO rights ( user_right) VALUES ('blocked');",
            "INSERT IGNORE INTO rights ( user_right) VALUES ('player');",
            "INSERT IGNORE INTO rights ( user_right) VALUES ('operator');",
            "INSERT IGNORE INTO rights ( user_right) VALUES ('manager');",
            "INSERT IGNORE INTO rights ( user_right) VALUES ('admin');",
        ]
        for script in sql_scripts:
            TestGlobalFixtures.add_row_to_table(script)

    @staticmethod
    def prepare_table_users():
        """
        adds rights to the database
        """
        user_blocked = """
            INSERT IGNORE
            INTO users (email, right_id, username, password, position)
            VALUES ("blocked@email.com", 1, "blocked","abc", "blocked");
            """
        user_player = """
            INSERT IGNORE
            INTO users (email, right_id, username, password, position)
            VALUES ("player@email.com", 2, "player","abc2", "blocked");
            """
        sql_scripts = [user_blocked, user_player,]
        for script in sql_scripts:
            TestGlobalFixtures.add_row_to_table(script)

    @staticmethod
    def prepare_table_question_levels():
        """
        adds question levels to the database
        """
        sql_scripts = [
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (1, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (2, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (3, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (4, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (5, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (6, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (7, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (8, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (9, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (10, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (11, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (12, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (13, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (14, 0);",  # noqa:E501
            "INSERT IGNORE INTO question_levels (question_level, hide) VALUES (15, 0);",  # noqa:E501
        ]
        for script in sql_scripts:
            TestGlobalFixtures.add_row_to_table(script)

    @staticmethod
    def prepare_table_question_difficulties():
        """
        adds question levels to the database
        """
        sql_scripts = [
            "INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name, hide) VALUES (0, 'warm up', 0);",  # noqa:E501
            "INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name, hide) VALUES (1, '2-5 Easy', 0);",  # noqa:E501
            "INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name, hide) VALUES (2, '6-10 Average', 0);",  # noqa:E501
            "INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name, hide) VALUES (3, '11-14 Difficult', 0);",  # noqa:E501
            "INSERT IGNORE INTO question_difficulties (difficulty, difficulty_name, hide) VALUES (4, '15', 0);",  # noqa:E501
        ]
        for script in sql_scripts:
            TestGlobalFixtures.add_row_to_table(script)

    @staticmethod
    def prepare_table_chapters():
        """
        adds chapters to the database
        """
        sql_scripts = [
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (1, 'Roles and Responsibilities');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (2, 'Well-Being of the Emergency Responder');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (3, 'Patient Assesment');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (4, 'Respiratory Emergencies');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (5, 'Supplementary Oxygen');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (6, 'Cardiovascular Emergencies');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (7, 'Trauma');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (8, 'Medical Conditions');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (9, 'Musculoskeletal Injuries');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (10, 'Environmental Emergencies');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (11, 'Special Populations');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (12, 'Special Situations');",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name) VALUES (13, 'Appendix');",  # noqa:E501
        ]
        for script in sql_scripts:
            TestGlobalFixtures.add_row_to_table(script)

    @staticmethod
    def prepare_table_sub_chapters():
        """
        adds sub_chapters to the database
        """
        sql_scripts = [
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 1, 'The Emergency Medical System');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 2, 'Legal and Ethical Issues');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 3, 'Communication');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (1, 4, 'Documentation and Record Keeping');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 1, 'Health andd Well-Being');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 2, 'Critical Incident Stress');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (2, 3, 'Infection Control');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 1, 'Emergency Scene Management and Primary Assessment');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 2, 'Secondary Assessment');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 3, 'Lifting and Carrying');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (3, 4, 'Multiple Patient Incidents');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 1, 'Respiratory Disease');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 2, 'Airway Obstructions');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (4, 3, 'Establishing and Maintaining the Airway');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (5, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (5, 1, 'Oxygen Administration');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (5, 2, 'Artificital Ventilation');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 1, 'Cardiovascular Disease');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 2, 'Cerebrovascular Emergencies (Stroke/TIA)');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 3, 'Cardiopulmonary Resuscitation');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (6, 4, 'Automated External Defibrillation');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 1, 'Shock');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 2, 'Wound Management');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 3, 'Eye Injuries');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 4, 'Burns');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 5, 'Chest Injuries');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 6, 'Gastrointestinal and Genitourinary');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (7, 7, 'Dental Emergencies');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 1, 'Diabetes');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 2, 'Seizures');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 3, 'Unconsciousness and Fainting');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (8, 4, 'General Pharmacology');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (9, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (9, 1, 'Head, Spinal and Pelvic Injuries');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (9, 2, 'Bone, Joint and Muscle Injuries');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 1, 'Heat and Cold-Related Emergencies');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 2, 'Poisons, Bites and Stings');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (10, 3, 'Aquatic Emergencies');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 1, 'Emergency Childbirth, Miscarriage and Neonates');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 2, 'Pediatric Patients');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 3, 'Geriatric Patients');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 4, 'Bariatric Patients');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 5, 'Special Needs and Palliative Care');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 6, 'Behavioral Emergencies');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (11, 7, 'Substance Abuse');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 1, 'Special Rescue Situations');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 2, 'Chemical, Biological, Radiological, Nuclear and Explosive Events (CBRNE)');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 3, 'Extended Patient Care');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 4, 'Maintaining Peripheral IVS');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 5, 'Death in Remote Areas');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 6, 'First Aid Stations and Rooms');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (12, 7, 'Ambulance Operations and Maintenance');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (13, 0, 'All');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (13, 1, 'Anatomy and Physiology');",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name) VALUES (13, 2, 'Medical Terminology');",  # noqa:E501

        ]
        for script in sql_scripts:
            TestGlobalFixtures.add_row_to_table(script)

    @staticmethod
    def prepare_fixtures(app, db):
        """
        prepare all tables
        """
        TestGlobalFixtures.app = app
        TestGlobalFixtures.db = db
        TestGlobalFixtures.prepare_table_rights()
        TestGlobalFixtures.prepare_table_users()
        TestGlobalFixtures.prepare_table_question_levels()
        TestGlobalFixtures.prepare_table_question_difficulties()
        TestGlobalFixtures.prepare_table_chapters()
        TestGlobalFixtures.prepare_table_sub_chapters()
