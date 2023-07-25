from sqlalchemy import create_engine, text

db_connection_string  = "mysql+pymysql://uvc61wgaht368k3g7w72:pscale_pw_DEewrtx7jdlqYzG1hmc2B38k9T2JCKQSVqciEjBHH9M@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"

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

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linked_in, cv_link) VALUES (job_id, :full_name, :e-mail, :linked-in, :cv_link)")
        conn.execute(query,
                    job_id=job_id, 
                    full_name=data['full_name'],
                    email=data['e-mail'],
                    linkedin=data['linked-in'],
                    cv_link=data['cv_link'])