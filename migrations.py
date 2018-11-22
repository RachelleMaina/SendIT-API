from app.db_config import create_tables, destroy_tables, db_init
def setup_db():
    # db_init()
    destroy_tables()
    create_tables()

if __name__ == '__main__':
    setup_db()