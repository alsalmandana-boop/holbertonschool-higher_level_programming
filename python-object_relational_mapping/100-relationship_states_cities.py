
#!/usr/bin/python3
"""Create California and San Francisco using SQLAlchemy relationships."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_state = State(name="California")
        new_state.cities.append(City(name="San Francisco"))

        session.add(new_state)
        session.commit()
    finally:
        session.close()

