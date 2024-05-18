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
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (1, 'Roles and Responsibilities', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (2, 'Well-Being of the Emergency Responder', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (3, 'Patient Assesment', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (4, 'Respiratory Emergencies', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (5, 'Supplementary Oxygen', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (6, 'Cardiovascular Emergencies', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (7, 'Trauma', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (8, 'Medical Conditions', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (9, 'Musculoskeletal Injuries', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (10, 'Environmental Emergencies', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (11, 'Special Populations', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (12, 'Special Situations', 0);",  # noqa:E501
            "INSERT IGNORE INTO chapters (chapter, chapter_name, hide) VALUES (13, 'Appendix', 0);",  # noqa:E501
        ]
        for script in sql_scripts:
            TestGlobalFixtures.add_row_to_table(script)

    @staticmethod
    def prepare_table_sub_chapters():
        """
        adds sub_chapters to the database
        """
        sql_scripts = [
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (1, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (1, 1, 'The Emergency Medical System', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (1, 2, 'Legal and Ethical Issues', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (1, 3, 'Communication', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (1, 4, 'Documentation and Record Keeping', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (2, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (2, 1, 'Health andd Well-Being', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (2, 2, 'Critical Incident Stress', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (2, 3, 'Infection Control', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (3, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (3, 1, 'Emergency Scene Management and Primary Assessment', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (3, 2, 'Secondary Assessment', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (3, 3, 'Lifting and Carrying', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (3, 4, 'Multiple Patient Incidents', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (4, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (4, 1, 'Respiratory Disease', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (4, 2, 'Airway Obstructions', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (4, 3, 'Establishing and Maintaining the Airway', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (5, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (5, 1, 'Oxygen Administration', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (5, 2, 'Artificital Ventilation', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (6, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (6, 1, 'Cardiovascular Disease', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (6, 2, 'Cerebrovascular Emergencies (Stroke/TIA)', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (6, 3, 'Cardiopulmonary Resuscitation', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (6, 4, 'Automated External Defibrillation', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 1, 'Shock', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 2, 'Wound Management', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 3, 'Eye Injuries', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 4, 'Burns', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 5, 'Chest Injuries', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 6, 'Gastrointestinal and Genitourinary', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (7, 7, 'Dental Emergencies', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (8, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (8, 1, 'Diabetes', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (8, 2, 'Seizures', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (8, 3, 'Unconsciousness and Fainting', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (8, 4, 'General Pharmacology', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (9, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (9, 1, 'Head, Spinal and Pelvic Injuries', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (9, 2, 'Bone, Joint and Muscle Injuries', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (10, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (10, 1, 'Heat and Cold-Related Emergencies', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (10, 2, 'Poisons, Bites and Stings', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (10, 3, 'Aquatic Emergencies', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 1, 'Emergency Childbirth, Miscarriage and Neonates', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 2, 'Pediatric Patients', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 3, 'Geriatric Patients', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 4, 'Bariatric Patients', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 5, 'Special Needs and Palliative Care', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 6, 'Behavioral Emergencies', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (11, 7, 'Substance Abuse', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 1, 'Special Rescue Situations', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 2, 'Chemical, Biological, Radiological, Nuclear and Explosive Events (CBRNE)', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 3, 'Extended Patient Care', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 4, 'Maintaining Peripheral IVS', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 5, 'Death in Remote Areas', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 6, 'First Aid Stations and Rooms', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (12, 7, 'Ambulance Operations and Maintenance', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (13, 0, 'All', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (13, 1, 'Anatomy and Physiology', 0);",  # noqa:E501
            "INSERT IGNORE INTO sub_chapters (chapter_id, sub_chapter, sub_chapter_name, hide) VALUES (13, 2, 'Medical Terminology', 0);",  # noqa:E501

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
