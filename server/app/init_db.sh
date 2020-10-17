DB_FILE=../data.sqlite
MIGRATION_DIR=./migrations

if [ -f "$DB_FILE" ]; then
    rm $DB_FILE
fi

if [ -d "$MIGRATION_DIR" ]; then
    rm -r $MIGRATION_DIR
fi

export FLASK_APP=flask_app:create_app &&\
flask db init && flask db migrate -m "initial migration" && flask db upgrade &&\
export FLASK_APP=init_db.py && flask run
