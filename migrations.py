from instance.db_config import create_tables, destroy_tables, create_admin, create_user, create_order, db_init
def setup_db():
    # db_init()
    destroy_tables()
    create_tables()
    create_admin()
    create_order()
    create_user()

if __name__ == '__main__':
    setup_db()