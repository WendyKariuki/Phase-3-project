from lib.config import CONN, CURSOR
class Event:

    #add an event
    @classmethod
    def insert(cls, name, location, date):
        sql = """INSERT INTO events (name, location, date) VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (name, location, date))
        CONN.commit()
        result = CURSOR.lastrowid
        return result
        

    #update an event
    @classmethod
    def update(cls, id, name, location, date):
        sql = """UPDATE events SET name=?, location=?, date=? WHERE id=?"""
        CURSOR.execute(sql, (name, location, date, id))
        CONN.commit()
        CURSOR.execute("SELECT * FROM events WHERE id = ?", (id, ))
        return CURSOR.fetchone()

    # get_event by id
    @classmethod
    def get_event_by_id(cls, id):
        sql = """SELECT * FROM events WHERE id = ?"""
        CURSOR.execute(sql, (id, ))
        return CURSOR.fetchone()
    
    # get all events
    @classmethod
    def get_all_events(cls):
        sql = """SELECT * FROM events"""
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    # count events
    @classmethod
    def count_events(cls):
        sql = """SELECT COUNT(*) FROM events"""
        CURSOR.execute(sql)
        return CURSOR.fetchone()
    
    #delete an event  
    @classmethod
    def delete(cls, id):
        sql = """DELETE FROM events WHERE id=?"""
        CURSOR.execute(sql, (id,))
        CONN.commit()

    
#insert a table
# event1 = Event.insert('Octoberfest', 'uhuru gardene', '2024-10-10')
# event2 = Event.insert('Halloween', 'mombasa', '2024-9-10')
# event3 = Event.insert('Christmas', 'nairobi', '2024-12-12')
# event4 = Event.insert('Easter', 'kisumu', '2024-4-10')
# event5 = Event.insert('New Year', 'nairobi', '2024-1-1')
# event6 = Event.insert('sip and code', 'nairobi', '2024-28-06')
# event7 = Event.insert('New Year', 'nairobi', '2024-1-1')
# event8 = Event.insert('New Year', 'nairobi', '2024-1-1')
# event9 = Event.insert('New Year', 'nairobi', '2024-1-1')
# event10 = Event.insert('New Year', 'nairobi', '2024-1-1')

#update an event
# Event.update(6, 'Career Fair', 'Diamond plaza', '2024-09-12')

#delete an event
# Event.delete(7)

# get event by id
# event = Event.get_event_by_id(2)
# print(event)

# get all events
# event = Event.get_all_events() 
# for event in event:
#     print(event)

# count events
# Event.count_events()