from lib.config import CURSOR, CONN

class Participant:

    #add an participant
    @classmethod
    def insert(cls, name, email, event_id):
        sql = """INSERT INTO participants (name, email, event_id) VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (name, email, event_id))
        CONN.commit()
        result = CURSOR.lastrowid
        return result

    #update an participant
    @classmethod
    def update(cls, id, name, email, event_id):
        sql = """UPDATE participants SET name=?, email=? WHERE id=?"""
        CURSOR.execute(sql, (id, name, email, event_id))
        CONN.commit()

    # get_participant by id
    @classmethod
    def get_participant_by_id(cls, id):
        sql = """SELECT * FROM participants WHERE id = ?"""
        CURSOR.execute(sql, (id, ))
        return CURSOR.fetchone()
    
    # get participants by event id
    @classmethod
    def get_participants_by_event_id(cls, event_id):
        sql = """SELECT * FROM participants WHERE event_id = ?"""
        CURSOR.execute(sql, (event_id, ))
        return CURSOR.fetchall()
    
    # get all participants
    @classmethod
    def get_all_participants(cls):
        sql = """SELECT * FROM participants"""
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    # count participants
    @classmethod
    def count_participants(cls):
        sql = """SELECT COUNT(*) FROM participants"""
        CURSOR.execute(sql)
        return CURSOR.fetchone()
    
    #delete an participant  
    @classmethod
    def delete(cls, id):
        sql = """DELETE FROM participants WHERE id=?"""
        CURSOR.execute(sql, (id,))
        CONN.commit()
    
#insert a table
participant1 = Participant.insert('Wendy Kariuki', 'wendykariuki@gmail.com' , 1)
participant2 = Participant.insert('John Doe', 'johndoe@gmail.com' , 2)
participant3 = Participant.insert('Jane Doe', 'janedoe@gmail.com' , 3)
participant4 = Participant.insert('Sir Henry', 'sirhenry@gmail.com' , 4)
participant5 = Participant.insert('Ferdinand Porscher', 'ferdinandporscher@gmail.com' , 5)
participant6 = Participant.insert('Mark Zucherberg', 'markzucherberg@gmail.com' , 6)
participant7 = Participant.insert('Mark Zucherberg', 'markzucherberg@gmail.com' , 6)
participant8 = Participant.insert('Mark Zucherberg', 'markzucherberg@gmail.com' , 6)
participant9 = Participant.insert('Mark Zucherberg', 'markzucherberg@gmail.com' , 6)
participant10 = Participant.insert('Mark Zucherberg', 'markzucherberg@gmail.com' , 6)


#update an participant
# participant.update(6, 'Career Fair', 'Diamond plaza', '2024-09-12')

#delete an participant
# participant.delete(7)

# get participant by id
# participant = participant.get_participant_by_id(2)
# print(participant)

# get participants by event id
# participant = Participant.get_participants_by_event_id(5)
# for participant in participant:
#     print(participant)

# get all participants
# participant = participant.get_all_participants() 
# for participant in participant:
#     print(participant)

# count participants
# participant.count_participants()