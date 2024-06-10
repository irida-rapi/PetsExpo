from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Pet:
    db_name='petsExpo'
    def __init__(self,data):
        self.id = data['id'],
        self.name = data['name'],
        self.origin = data['origin'],
        self.type = data['type'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def create_pet(cls,data):
        query = 'INSERT INTO pets (name, origin, type, user_id) VALUES ( %(name)s, %(origin)s, %(type)s, %(user_id)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def getAllPets(cls,data):
    #     query= 'SELECT pets.id, pets.name, users.id AS user_id, users.first_name, users.last_name FROM pets LEFT JOIN users ON users.id = pets.user_id LEFT JOIN favorites ON favorites.book_id = books.id GROUP BY books.id;'
    #     results =  connectToMySQL(cls.db_name).query_db(query, data)
    #     books= []
    #     if results:
    #         for row in results:
    #             books.append(row)
    #         return books
    #     return books

    @classmethod
    def get_pet_by_id(cls, data):
        query= 'SELECT * FROM pets WHERE pets.id = %(pet_id)s;'
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results[0]

    # @classmethod
    # def get_all_book_info(cls, data):
    #     query= 'SELECT users.id, first_name, last_name, books.id as book_id, books.created_at, books.updated_at FROM books LEFT JOIN users on users.id = books.user_id LEFT JOIN favorites on favorites.book_id = books.id WHERE books.id = %(book_id)s GROUP BY users.id;'
    #     results = connectToMySQL(cls.db_name).query_db(query, data)
    #     who_fav = []
    #     if results:
    #         for row in results:
    #             who_fav.append(row)
    #         return who_fav
    #     return who_fav

    # @classmethod
    # def addFavor(cls, data):
    #     query= 'INSERT INTO favorites (book_id, user_id) VALUES ( %(book_id)s, %(user_id)s );'
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def update_pet(cls, data):
        query = 'UPDATE pets SET name = %(name)s, origin = %(origin)s, type = %(type)s WHERE pets.id = %(pet_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def deletePet(cls, data):
        query= 'DELETE FROM pets WHERE pets.id = %(pet_id)s;'
        return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def deleteAllFavorites(cls, data):
    #     query= 'DELETE FROM favorites WHERE favorites.book_id = %(book_id)s;'
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    # @classmethod
    # def removeFavor(cls, data):
    #     query= 'DELETE FROM favorites WHERE book_id = %(book_id)s and user_id = %(user_id)s;'
    #     return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_pet(pet):
        is_valid = True
        if len(pet['name']) < 2:
            flash("*Name is required!", 'name')
            is_valid = False
        if len(pet['origin']) < 2:
            flash("*Origin is required!", 'origin')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_update(update):
        is_valid = True
        if len(update['name']) < 2:
            flash("*Name is required!", 'update_name')
            is_valid = False
        if len(update['origin']) < 2:
            flash("*Origin is required", 'update_origin')
            is_valid = False
        return is_valid
