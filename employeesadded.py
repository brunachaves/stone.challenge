from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dbfunc_setup import Employee, Base

engine = create_engine('sqlite:///employee.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Info for Vivian Chaves
employee1 = Employee(name="Vivian Chaves", age = 37, role = "Encantadora" )

session.add(employee1)
session.commit()


# Info for Pedro Silva
employee2 = Employee(name="Pedro Guilherme", age = 28, role = "Recrutador")

session.add(employee2)
session.commit()


# Info for Juliana Batisa
employee3 = Employee(name="Juliana Batista", age = 24, role = "Marca")

session.add(employee3)
session.commit()

# Info for Michele Rocha
employee4 = Employee(name="Michele Rocha", age = 20, role = "Tecnologia RC")

session.add(employee4)
session.commit()





print("employee added!")