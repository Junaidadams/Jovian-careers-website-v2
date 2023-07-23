from sqlalchemy import create_engine, text

db_connection_string  = "mysql+pymysql://llk26msts3trw4sc60ae:pscale_pw_9yRVNyDjg6BBreTZHzi4jLbwZTObZFWUEmxaCEAXuwF@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        result_dicts = []
        for row in result.all():
            result_dicts.append(dict(row._mapping))
        return result_dicts
    