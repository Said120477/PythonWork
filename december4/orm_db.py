from sqlalchemy import create_engine, select, ForeignKey, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List

db_name = 'C:\\Users\\User\\Documents\\уроки PY\\PythonWork\\db\\bot_todo'
engine = create_engine(f'sqlite:///{db_name}')

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    user: Mapped["User"] = relationship(back_populates='tasks')


    def __repr__(self):
        return f"{self.id} - {self.name}"

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    telegram_id: Mapped[int]

    tasks: Mapped[List['Task']] = relationship(back_populates='user')

    def __repr__(self):
        return f"{self.telegram_id}"

sesion = Session(engine)
# r = sesion.execute(select(Task)).scalars().all()
# task = r[0]
# sesion.close()
# print(r)
# print(task.name)

session = Session(engine)
# task = Task(name='прибраться дома')
# session.add(task)
# session.commit()
# session.close()

users = session.scalars(select(User)).all()
# print(users[0].name, users[0].telegram_id)

tasks = session.scalars(select(Task).where(Task.user_id == 1)).all()
print(tasks)

# for task in tasks:
#     print(task.name, task.user.telegram_id)

user = session.scalars(select(User).where(User.id == 1)).one()
tasks = user.tasks
print(tasks)


session.close()









