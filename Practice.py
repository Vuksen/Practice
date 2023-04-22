from sqlalchemy import MetaData, Table, Integer, String, Column
from sqlalchemy import insert
from sqlalchemy import update, delete
from sqlalchemy import select
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:fennekin@localhost/testing")

metadata = MetaData()

chat_groups = Table('chat_groups', metadata,
                    Column('id', Integer(), primary_key=True),
                    Column('group_name', String(200), nullable=False),
                    Column('description', String(400), nullable=False)
)


def adding_new_chat():
    name = input("input chat name: ")
    descript = input("input chat description: ")
    values = [
        {
            "group_name": name,
            "description": descript
        }
    ]
    with engine.begin() as connection:
        connection.execute(insert(chat_groups), values)
    print(4)


def get_chats():
    conn = engine.connect()
    s = select(chat_groups)
    r = conn.execute(s)
    for row in r:
        print(row)


def get_chat_by_id(index):
    conn = engine.connect()
    s = select(chat_groups).where(
        chat_groups.c.id == int(index)
    )
    r = conn.execute(s)
    for row in r:
        print(row)


def chat_update(index):
    new_group_name = input('Input new chat name: ')
    new_chat_description = input('Input new description')
    s = update(chat_groups).where(
        chat_groups.c.id == int(index)
    ).values(
        group_name=new_group_name,
        description=new_chat_description
    )
    with engine.begin() as connection:
        connection.execute(s)


def chat_delete(index):
    s = delete(chat_groups).where(
        chat_groups.c.id == int(index)
    )
    with engine.begin() as connection:
        connection.execute(s)


# metadata.create_all(engine)

adding_new_chat()
chat_update(4)
get_chats()
get_chat_by_id(2)

