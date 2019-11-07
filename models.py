import datetime

import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase

# import main_1 as mone

db = PostgresqlExtDatabase('todolist-demo')


class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now())
    updated_at = pw.DateTimeField(default=datetime.datetime.now())

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db
        # Check this one out here http://docs.peewee-orm.com/en/latest/peewee/models.html#table-names
        legacy_table_names = False


class UserProfile(BaseModel):
    username = pw.CharField()
    password = pw.CharField()


class TodoList(BaseModel):
    name = pw.CharField()
    user_profile = pw.ForeignKeyField(
        UserProfile, backref="lists")


class TodoTask(BaseModel):
    task = pw.CharField()
    completed = pw.BooleanField(default=False)
    todo_list = pw.ForeignKeyField(TodoList, backref="todos")


db.connect()

db.create_tables([UserProfile, TodoList, TodoTask])


# Define your models here
# class if __name__ == "__main__":
