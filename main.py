from lib.event import Event
from lib.tickets import Ticket
from lib.participant import Participant
import sys

# menu-driven interface for performing various operations(main menu)
def main_menu():
    while True:
        print("============MAIN MENU===============") 
        print("1. Manage events") 
        print("2. Manage participants")
        print("3. Manage tickets")
        print("4. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            return event_operations()

        elif choice == "2":
            return participant_operations()
        
        elif choice == "3":
            return tickets_operations()

        elif choice == "4":
            sys.exit()
        
        else:
            print("Invalid Input")

# menu-driven interface for performing various event operations
def event_operations():
   while True:
       print("============EVENT OPERATIONS============")
       print("1.Add an event")
       print("2.Update an event")
       print("3.Get an event by id")
       print("4.Get all events")
       print("5.Count all events")
       print("6.Delete an event")
       print("7.Return to main menu")

       choice = input("\nEnter your choice: ")

       event = Event() # Create an Event object to perform operations based on user choice

        #add an event
       if choice == "1":
           name = input("Enter event name: ")
           location = input("Enter event location: ")
           date = input("Enter event date: ")
           event_id = event.insert(name, location, date)
           print(f"Event with id {event_id} added successfully")

        #update event
       elif choice == "2":
            event_id = input("Enter the id of the event you want to update: ")
            name = input("Enter new name: ")
            location= input("Enter new location: ")
            date = input("Enter new date: ")

            eventId = event.update(event_id , name, location, date)
            print(f"Event with id {eventId} updated successfully")

        #get event by id
       elif choice == "3":
            event_id = input("Enter the id of the event you want to get")
            one_event = event.get_event_by_id(event_id)
            print(one_event)
            
        #get all events
       elif choice == "4":
            all_events = event.get_all_events()
            print("\nAll events")
            for event in all_events:
                print(event)

        #count events
       elif choice == "5":
            event_count = event.count_events()
            print(event_count)

        #delete an event
       elif choice == "6":
            event_id = input("Enter the id of the event you want to delete: ")
            event.delete(event_id)
            print(f"Event with id {event_id} deleted successfully")

        #return to main menu
       elif choice == "7":
            return main_menu()
       
        #error if input is not valid(number not in 1-8)
       else:
            print("Invalid Input")
           
# menu-driven interface for performing various operations on participants.
def participant_operations(): 
    while True:
        print("============PARTICIPANT OPERATIONS============")
        print("1.Add a participant")
        print("2.Update a participant")
        print("3.Get a participant by id")
        print("4.Get participants by event id")
        print("5.Get all participants")
        print("6.Count all participants")
        print("7.Delete a participant")
        print("8.Return to main menu")

        choice = input("\nEnter your choice: ")

        participant = Participant() # Create a Participant object to perform operations based on user choice

        #add participant
        if choice == "1":
            name = input("Enter participant name: ")
            email = input("Enter participant email: ")
            event_id = input("Enter event id: ")

            new_participant_id = participant.insert(name, email, event_id)
            print(f"Participant with id {new_participant_id} added successfully")

        elif choice == "2":
            participant_id = input("Enter the id of the participant you want to update: ")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            event_id = input("Enter new event id: ")

            participant = Participant()
            participantId = participant.update(participant_id, name, email, event_id)
            print(f"Participant with id {participantId} updated successfully")

        #get a participant by id
        elif choice == "3":
            participant_id = input("Enter the id of the participant you want to get: ")
            one_participant = participant.get_participant_by_id(participant_id)
            print(one_participant)
        
        #get participants by event id
        elif choice == "4":
            event_id = input("Enter the id of the event you want to get participants: ")
            participants = participant.get_participants_by_event_id(event_id)
            print(participants)

        #get all participants
        elif choice == "5":
            all_participants = participant.get_all_participants()
            print("\nAll participants")
            for participant in all_participants:
                print(participant)

        #count all participants
        elif choice == "6":
            participant_count = participant.count_participants()
            print(participant_count)

        #delete a participant
        elif choice == "7":
            participant_id = input("Enter the id of the participant you want to delete: ")
            participant.delete(participant_id)
            print(f"Participant with id {participant_id} deleted successfully")
        
        #return to main menu
        elif choice == "8":
                return main_menu()
        
        #error if input is not valid(number not in 1-8)
        else:
                print("Invalid Input")

 # menu-driven interface for performing various operations on tickets.       
def tickets_operations():
    while True:
        print("============TICKET OPERATIONS============")
        print("1.Add a ticket")
        print("2.Update a ticket")
        print("3.Get a ticket by id")
        print("4.Get tickets by event id")
        print("5.Get tickets by participant id")
        print("6.Get all tickets")
        print("7.Count all tickets")
        print("8.Delete a ticket")
        print("9.Return to main menu")

        choice = input("\nEnter your choice: ")

        ticket = Ticket() # Create a Ticket object to perform operations based on user choice

        #add ticket
        if choice == "1":
            ticket_number = input("Enter ticket number: ")
            price = input("Enter price: ")
            participant_id = input("Enter participant id: ")
            event_id = input("Enter event id: ")

            new_ticket_id = ticket.insert(ticket_number, price, participant_id, event_id)
            print(f"Ticket with id {new_ticket_id} added successfully")

        #update ticket
        elif choice == "2":
            ticket_id = input("Enter the id of the ticket you want to update: ")
            ticket_number = input("Enter new ticket number: ")
            price = input("Enter new price: ")
            participant_id = input("Enter new participant id: ")
            event_id = input("Enter new event id: ")

            ticket.update(ticket_id, ticket_number, price, participant_id, event_id)
            print(f"Ticket with id {ticket_id} updated successfully")

        #get a ticket by id
        elif choice == "3":
            ticket_id = input("Enter the id of the ticket you want to get: ")
            one_ticket = ticket.get_ticket_by_id(ticket_id)
            print(one_ticket)
        
        #get tickets by event id
        elif choice == "4":
            event_id = input("Enter the id of the event you want to get tickets: ")
            tickets = ticket.get_tickets_by_event_id(event_id)
            print(tickets)
        
        #get tickets by participant id
        elif choice == "5":
            participant_id = input("Enter the id of the participant you want to get tickets: ")
            tickets = ticket.get_tickets_by_participant_id(participant_id)
            print(tickets)

        #get all tickets
        elif choice == "6":
            all_tickets = ticket.get_all_tickets()
            print("\nAll tickets")
            for ticket in all_tickets:
                print(ticket)
            
        #count all tickets
        elif choice == "7":
            ticket_count = ticket.count_tickets()
            print(ticket_count)

        #delete a ticket
        elif choice == "8":
            ticket_id = input("Enter the id of the ticket you want to delete: ")
            ticket.delete(ticket_id)
            print(f"Ticket with id {ticket_id} deleted successfully")

        #return to main menu
        elif choice == "9":
            return main_menu()
        
main_menu()