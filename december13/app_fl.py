from flask import Flask, render_template
from typing import List

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey


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


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///C:\\Users\\User\\Documents\\уроки PY\\PythonWork\\db\\bot_todo'

db = SQLAlchemy(model_class=Base)
db.init_app(app)



todo = [{'id': 1, 'name': 'погулять'},
        {'id': 2, 'name': 'поиграть'},
        {'id': 3, 'name': 'поужинать'},
        {'id': 4, 'name': 'почитать'}]




@app.route('/')
def main():
    todo_db = db.session.execute(db.select(Task)).scalars().all()
    users = db.session.execute(db.select(User)).scalars().all()
    return render_template('main.html', todo_data=todo_db, users=users)

@app.route('/about')
def about_page():
    return render_template('about_page.html')

@app.route('/tasks/<int:user_id>')
def user_tasks(user_id):
    tasks = db.session.execute(db.select(Task).filter_by(user_id=user_id)).scalars().all()
    return render_template('tasks.html', tasks=tasks, user_id=user_id)

if __name__ == '__main__':
    app.run(debug=True)















