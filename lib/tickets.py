from lib.config import CURSOR, CONN

class Ticket:

    #add an ticket
    @classmethod
    def insert(cls, ticket_number, price, participant_id, event_id):
        sql = """INSERT INTO tickets (ticket_number, price, participant_id, event_id) VALUES (?, ?, ?, ?)"""
        CURSOR.execute(sql, (ticket_number, price, participant_id, event_id))
        CONN.commit()
        result = CURSOR.lastrowid
        return result

    #update an ticket
    @classmethod
    def update(cls, id, ticket_number, price, participant_id, event_id):
        sql = """
        UPDATE tickets SET ticket_number=?, price=?, participant_id=?, event_id=? WHERE id=?"""
        CURSOR.execute(sql, (ticket_number, price, participant_id, event_id, id))
        CONN.commit()


    # get_ticket by id
    @classmethod
    def get_ticket_by_id(cls, id):
        sql = """SELECT * FROM tickets WHERE id = ?"""
        CURSOR.execute(sql, (id, ))
        return CURSOR.fetchone()
    
    # get all tickets by event id
    @classmethod
    def get_tickets_by_event_id(cls, event_id):
        sql = """SELECT * FROM tickets WHERE event_id = ?"""
        CURSOR.execute(sql, (event_id, ))
        return CURSOR.fetchall()
    
    # get all tickets by participant id
    @classmethod
    def get_tickets_by_participant_id(cls, participant_id):
        sql = """SELECT * FROM tickets WHERE participant_id = ?"""
        CURSOR.execute(sql, (participant_id, ))
        return CURSOR.fetchall()
    
    # get all tickets
    @classmethod
    def get_all_tickets(cls):
        sql = """SELECT * FROM tickets"""
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    # count tickets
    @classmethod
    def count_tickets(cls):
        sql = """SELECT COUNT(*) FROM tickets"""
        CURSOR.execute(sql)
        return CURSOR.fetchone()
    
    #delete an ticket  
    @classmethod
    def delete(cls, id):
        sql = """DELETE FROM tickets WHERE id=?"""
        CURSOR.execute(sql, (id,))
        CONN.commit()

    
#insert a table
# ticket1 = Ticket.insert('1', '1000' ,1, 1)
# ticket2 = Ticket.insert('2', '1500' ,1, 2)
# ticket3 = Ticket.insert('3', '2000' ,2, 3)
# ticket4 = Ticket.insert('4', '2500' ,1, 4)
# ticket5 = Ticket.insert('5', '3000' ,1, 5)
# ticket6 = Ticket.insert('6', '3500' ,1, 6)
# ticket7 = Ticket.insert('7', '4000' ,1, 7)
# ticket8 = Ticket.insert('8', '4500' ,1, 8)
# ticket9 = Ticket.insert('9', '5000' ,1, 9)


#update an ticket
# ticket.update(6, 'Career Fair', 'Diamond plaza', '2024-09-12')

#delete an ticket
# ticket.delete(7)

# get ticket by id
# ticket = ticket.get_ticket_by_id(2)
# print(ticket)

# get tickets by event id
# ticket = ticket.get_tickets_by_event_id(5)
# for ticket in ticket:
#     print(ticket)

# get tickets by participant id
# ticket = ticket.get_tickets_by_participant_id(1)
# for ticket in ticket:
#     print(ticket)

# get all tickets
# ticket = ticket.get_all_tickets() 
# for ticket in ticket:
#     print(ticket)

# count tickets
# ticket.count_tickets()