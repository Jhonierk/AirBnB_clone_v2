#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    __engine = None
    __session = None
    valid_classes = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://" +
                                      os.environ['HBNB_MYSQL_USER'] +
                                      ":" + os.environ['HBNB_MYSQL_PWD'] +
                                      "@" + os.environ['HBNB_MYSQL_HOST'] +
                                      ":3306/" +
                                      os.environ['HBNB_MYSQL_DB'])

        try:
            if os.environ['HBNB_MYSQL_ENV'] == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        storage = {}
        if cls is None:
          objects = self.__session.query(User, State, City,  Amenity,
                                           Place, Review)
            for obj in objects:
                key = type(obj).__name__ + "." + str(obj.id)
                class_objects[key] = obj
                # return class_objects with all class objects
        else:
            # make sure use eval(cls) when filestorage is being used
            # objects = self.__session.query(eval(cls)).all()
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = type(obj).__name__ + "." + str(obj.id)
                class_objects[key] = obj

        return class_objects

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        try:
            self.__session.commit()
        except:
            self.__session.rollback()
            raise
        finally:
            self.__session.close()

    def update(self, cls, obj_id, key, new_value):
        res = self.__session.query(eval(cls)).filter(eval(cls).id == obj_id)

        if res.count() == 0:
            return 0

        res.update({key: (new_value)})
        return 1

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def delete(self, obj=None):
        if obj is None:
            return

        self.__session.delete(obj)

    def close(self):
        self.__session.close()
