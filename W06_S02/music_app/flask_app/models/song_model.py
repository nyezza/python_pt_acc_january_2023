from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import singer_model


class Song:

    def __init__(self, data):
        self.id = data['id']
        self.singer_id = data['singer_id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.singer = None
        #  - READ ALL
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM songs JOIN singers on singers.id  = songs.singer_id;
        """
        results  = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_songs = []
        for row in results :
            # all_songs.append(cls(row))
            this_song = cls(row)
            singer_data = {
                "id": row['singers.id'],
                "image": row['image'],
                "name": row['name'],
                "nationality": row['nationality'],
                "rate": row['rate'],
                "created_at": row['singers.created_at'],
                "updated_at": row['singers.updated_at'],
            }
            this_singer = singer_model.Singer(singer_data)
            this_song.singer = this_singer
            all_songs.append(this_song)
        return all_songs
    
    # CREATE
    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO songs (singer_id, title) 
            VALUES (%(singer_id)s, %(title)s) ;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(f" this is the return after INSERT one Song == {result} ******** ")
        return result
    
    #  Read One 
    @classmethod
    def get_by_singer(cls, data):
        query = """
            SELECT * FROM songs WHERE singer_id  = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        singer_songs = []
        if results:
            for row in results:
                singer_songs.append(cls(row))
        print("One Song ==  ", results, "-"*20) 
        return singer_songs
    #  Read One 
    @classmethod
    def get_by_id(cls, data):
        query = """
            SELECT * FROM songs WHERE id  = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        print("One Song ==  ", results, "-"*20) 
        return cls(results[0])

      # Update 
    @classmethod
    def update(cls, data):

        query = """
            UPDATE songs SET title = %(title)s WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM songs WHERE id  = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)