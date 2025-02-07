from sqlalchemy import create_engine, text

conn = 'postgresql+psycopg2://postgres:12345@localhost:5432/bot_tasks'
engine = create_engine(conn)

c = engine.connect()
r = c.execute(text('select * from task')).scalars().all()
print(r)






