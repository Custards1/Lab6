import mysql.connector


class Course:
    def __init__(self, subject: str, number: int, title: str = ""):
        self.__subject = subject
        self.__number = number
        self.__title = title

    def __str__(self):
        return f"""{self.subject}:{self.__number:04}"""
        pass

    @property
    def subject(self):
        return self.__subject

    @property
    def number(self):
        return self.__number

    @property
    def title(self):
        return self.__title

    # #################### LOADING DATA FROM DATABASE ####################
    # -----------------------------------------------------------------------------------------------------------------

    def load(self, db_config : dict):
        """
        Loads the data for the current object. Assume subject and number is loaded in the object.
        :param db_config: a dictionary as described in Readme.md with the connection information.
        """
        try:
            cont =  mysql.connector.connect(user=db_config["user"], password=db_config["password"],
                              host=db_config["host"],
                              database=db_config["database"])
            cursor = cont.cursor()
            query = ("SELECT subject, number, title FROM university.course WHERE subject = \"%s\" and number = %d")
            cursor.execute(query,self.__subject,self.__number)
            for (subject,number,title) in cursor:
                self.__number = number
                self.__subject = subject
                self.__title = title
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
        Loads all the courses and returns the list
        :param db_config: a dictionary as described in Readme.md with the connection information.
        :return the list of all loaded courses from the db.
        """
        res = list()
        try:
            cont =  mysql.connector.connect(user=db_config["user"], password=db_config["password"],
                              host=db_config["host"],
                              database=db_config["database"])
            cursor = cont.cursor()
            query = ("SELECT subject, number, title FROM university.course")
            cursor.execute(query)
            for (subject,number,title) in cursor:
                res.append(Course(subject,number,title))
            cursor.close()
            cont.close()
        except:
            raise ValueError
        return res

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def load_all_subject(db_config : dict, subject: str) -> []:

        """
        Class method.
        Loads all the courses with "subject" in the course's subject.
        The search should be done in the DB and is case insensitive.
            Hint: remember that `like "%abc%"` will return all rows where abc is anywhere in the column.
        :param db_config: a dictionary as described in Readme.md with the connection information.
        :param subject: subject to search for.
        :return: the list of all loaded courses from the db.
        """
        res = list()
        try:
            cont =  mysql.connector.connect(user=db_config["user"], password=db_config["password"],
                              host=db_config["host"],
                              database=db_config["database"])
            cursor = cont.cursor()
            query = ("SELECT subject, number, title FROM university.course WHERE upper(subject) like \"%s\"")
            cursor.execute(query,subject.upper())
            for (subject,number,title) in cursor:
                res.append(Course(subject,number,title))
            cursor.close()
            cont.close()
        except:
            raise ValueError
        return res

    pass
