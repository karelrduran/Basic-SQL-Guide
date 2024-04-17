from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric
# from data_connection import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WineType(Base):
    __tablename__ = 'wine_type'
    wine_type_id = Column(Integer, primary_key=True)
    type_id = Column(Text, nullable=False)


class Grapes(Base):
    __tablename__ = 'grapes'
    grape_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    parent_grape_id = Column(Integer, ForeignKey('grapes.grapes_id'), nullable=False)


class Country(Base):
    __tablename__ = 'countries'
    country_code = Column(Integer, primary_key=True)
    country = Column(Text, nullable=False)


class Regions(Base):
    __tablename__ = 'regions'
    region_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    parent_id = Column(Integer, nullable=False)
    fk_country_code = Column(Integer, ForeignKey('countries.country_code'), nullable=False)


class Wineries(Base):
    __tablename__ = 'wineries'
    winery_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    fk_region_id = Column(Integer, ForeignKey('regions.region_id'), nullable=False)


class Wines(Base):
    __tablename__ = 'wines'
    wine_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    fk_winery_id = Column(Integer, ForeignKey('wineries.winery_id'), nullable=False)
    fk_wine_type_id = Column(Integer, ForeignKey('wine_type.wine_type_id'), nullable=False)
    fk_grape_id = Column(Integer, ForeignKey('grapes.grape_id'), nullable=False)
    rating_average = Column(Numeric, nullable=False)
    ratings_count = Column(Integer, nullable=False)


class WineTasteLinks(Base):
    __tablename__ = 'wine_taste_link'
    fk_wine_id = Column(Integer, ForeignKey('wines.wine_id'), primary_key=True)
    property_id = Column(Integer, primary_key=True)
    property_level = Column(Numeric, nullable=False)


class Vintages(Base):
    __tablename__ = 'vintages'
    vintage_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)
    url = Column(Text, nullable=False)
    rating_average = Column(Numeric, nullable=False)
    rating_count = Column(Integer, nullable=False)
    alcohol_level = Column(Numeric, nullable=False)
    fk_wine_id = Column(Integer, ForeignKey('wines.wine_id'), nullable=False)


class Keywords(Base):
    __tablename__ = 'keywords'
    keyword_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)


class KeywordsWines(Base):
    __tablename__ = 'keywords_wine'
    fk_keywords_id = Column(Integer, ForeignKey('keyword.keywords_id'), nullable=False)
    fk_wine_id = Column(Integer, ForeignKey('wines.wine_id'), nullable=False)
    group_names = Column(Integer, primary_key=True, nullable=False)
    keyword_type = Column(Text, nullable=False)
    count = Column(Integer, nullable=False)
