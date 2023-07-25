from sqlalchemy import create_engine, text

db_connection_string  = "mysql+pymysql://8rrg1t084f9cx635zqhl:pscale_pw_kuDzXO6pVFP4ZRhqJGDqb1HSxVfz8E6tLpzSevDpzRN@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

# Not sure how to encode sever password/username

engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        result_dicts = []
        for row in result.all():
            result_dicts.append(dict(row._mapping))
        return result_dicts
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM JOBS WHERE id=:val"),
                              val = id)
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])