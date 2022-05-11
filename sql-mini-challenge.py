from sqlalchemy import(
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the insutrctions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "country" table
class Countries(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_city = Column(String)
    continient = Column(String)
    year_lived = Integer
    year_left = Integer


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on country table
china = Countries(
    country_name="China",
    capital_city="Beijing",
    continient="Asia",
    year_lived=1981,
    year_left=2002
)

cyprus = Countries(
    country_name = "Cyprus",
    capital_city = "Nicosia",
    continient = "Europe",
    year_lived = 2002,
    year_left = 2009
)

uk = Countries(
    country_name = "UK",
    capital_city = "London",
    continient = "Europe",
    year_lived = 2009,
    year_left = 2012
)

usa = Countries(
    country_name = "USA",
    capital_city = "Washington",
    continient = "North America",
    year_lived = 2012,
    year_left = 2014
)

ireland = Countries(
    country_name = "Ireland",
    capital_city = "Dublin",
    continient = "Europe",
    year_lived = 2014,
    year_left = 2016
)

germany = Countries(
    country_name = "Germany",
    capital_city = "Berlin",
    continient = "Europe",
    year_lived = 2016,
    year_left = 2018
)

cyprus = Countries(
    country_name = "Cyprus",
    capital_city = "Nicosia",
    continient = "Europe",
    year_lived = 2018,
    year_left = 2020
)

sweden = Countries(
    country_name = "Sweden",
    capital_city = "Stockholm",
    continient = "Europe",
    year_lived = 2020,
    year_left = 2022
)

# add each instance of our programmer to our session
# session.add(china)
# session.add(cyprus)
# session.add(uk)
# session.add(usa)
# session.add(ireland)
# session.add(germany)
# session.add(cyprus)
# session.add(sweden)

# commit our session to the database
# session.commit()


# updating a single record
# country = session.query(Countries).filter_by(id=7)
# country.year_left = "Still here!"

# commit our session to the database
# session.commit()


# update multiple records
# places = session.query(Countries)
# for place in places:
#     if place.capital_city == "Nicosia":
#         place.capital_city = "Too hot there"    
    
#     session.commit()


# query the database to find all countries
countries = session.query(Countries)
for country in countries:
    print(
        country.id,
        country.country_name,
        country.capital_city,
        country.continient,
        country.year_lived,
        country.year_left,
        sep=" | "
    )

