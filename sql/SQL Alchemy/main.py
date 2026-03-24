from sqlalchemy import Column, String, Integer, create_engine, func
from sqlalchemy.orm import declarative_base, sessionmaker

#create engine
engine = create_engine('sqlite:///test.db')

#2. creating session maker
session = sessionmaker(bind = engine)
session = session()

#3. create table based on orm
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable= False)
    age = Column(Integer)

#Table creation 
Base.metadata.create_all(engine)#this creates table
print("table created")

#inserting data
user1 = User(name = 'ravi', age = 20)
#add data into table
session.add(user1)
session.commit()
print("data inserted")
#insert multiple records
user2 = User(name="komal",age = 22)
user3 = User(name='Dhanu',age = 20)
user4 = User(name = 'Durga', age = 34)

#data fetching
session.add_all([user2, user3, user4])
session.commit()
data = session.query(User).all()
print(data)
for row in data:
     print(f"{row.id} {row.name} {row.age}")

#applying group by
data = session.query(func.count(User.id)).all()
print(data)

data = session.query(User.name,func.count(User.name)).group_by(User.name).all()
print(data)