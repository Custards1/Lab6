import mysql.connector

# #####################################################################################
class Student:

    def __init__(self, oid: str, name: str, email: str, standing: str, gpa: int):
        self.__name = name
        self.__email = email
        self.__standing = standing
        self.gpa = gpa
        self.__id = oid

    def __str__(self):
        return f"""{self.name:<20} - {self.id:^10} - {self.email:<50} - Standing: {self.standing}"""

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def id(self):
        return self.__id

    @property
    def standing(self):
        return self.__standing

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float):
        if 0 <= value <= 4:
            self.__gpa = value

    # #################### LOADING DATA FROM DATABASE ####################

    # -----------------------------------------------------------------------------------------------------------------
    def load(self, db_config : dict):
        """
        Loads the data for the current object. Assume id is loaded in the object.
        :param db_config: a dictionary as described in Readme.md with the connection information.
        """
        try:
            cont =  mysql.connector.connect(user=db_config["user"], password=db_config["password"],
                              host=db_config["host"],
                              database=db_config["database"])
            cursor = cont.cursor()
            query = ("SELECT id, name, email, standing, gpa FROM university.student WHERE id = \"%s\"")
            cursor.execute(query,self.__id)
            for (id,name,email,standing,gpa) in cursor:
                self.__name = name
                self.__email = email
                self.__standing = standing
                self.__gpa = gpa
                break
            cursor.close()
            cont.close()
        except:
            raise ValueError
        return db_config

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def load_all(db_config : dict) -> []:
        """
        Class method.
        Loads all the students and returns the list
        :param db_config: a dictionary as described in Readme.md with the connection information.
        :return the list of all loaded students from the db.
        """
        res = list()
        try:
            cont =  mysql.connector.connect(user=db_config["user"], password=db_config["password"],
                              host=db_config["host"],
                              database=db_config["database"])
            cursor = cont.cursor()
            query = ("SELECT id, name, email, standing, gpa FROM university.student")
            cursor.execute(query)
            for (id,name,email,standing,gpa) in cursor:
                res.append(Student(id,name,email,standing,gpa))
            cursor.close()
            cont.close()
        except:
            raise ValueError

        return res

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def load_by_name(db_config : dict, name: str) -> []:
        """
        Class method.
        Loads all the students with "name" in the student's name.
        The search should be done in the DB and is case insensitive.
            Hint: remember that `like "%abc%"` will return all rows where abc is anywhere in the column.
        :param db_config: a dictionary as described in Readme.md with the connection information.
        :param name: student's name to search for.
        :return: the list of all loaded students from the db.
        """
        res = list()
        try:
            cont =  mysql.connector.connect(user=db_config["user"], password=db_config["password"],
                              host=db_config["host"],
                              database=db_config["database"])
            cursor = cont.cursor()
            query = ("SELECT id, name, email, standing, gpa FROM university.student WHERE upper(name) like \"%s\"")
            cursor.execute(query,name)
            for (id,name,email,standing,gpa) in cursor:
                res.append(Student(id,name,email,standing,gpa))
            cursor.close()
            cont.close()
        except:
            raise ValueError

        return res

    pass

