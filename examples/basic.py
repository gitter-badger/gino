import asyncpg
from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='noname')
    profile = db.Column(db.JSONB())

    def __repr__(self):
        return '{}<{}>'.format(self.nickname, self.id)


async def main():
    conn = await asyncpg.connect('postgresql://localhost/gino')

    # You will need to create the database and table manually

    print(await User.create(bind=conn, nickname='fantix'))
    print(await User.get(1, bind=conn))


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
