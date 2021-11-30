import os
import mysql.connector as m
from datetime import date


con=m.connect(host='localhost',user='root',password='1234')

ex='n'

def database():
    c=con.cursor()
    sql="create database IF NOT EXISTS event"
    c.execute(sql)
    con.commit()

    sql="use event"
    c.execute(sql)

    sql="create table IF NOT EXISTS booking(e_id INTEGER(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,\
        e_district varchar(30),\
        e_name varchar(30),\
        e_type varchar(30),\
        e_date date,\
        e_venue varchar(30),\
        e_guests int)"
    c.execute(sql)

def addEvent():
    c=con.cursor()
    eventDistrict = input("District: ")
    eventName = input("Event Name: ")
    eventType = input("Event Type(Marriage, Birthday, etc): ")
    eventDate = input("Date(yyyy-mm-dd): ")
    eventVenue = input("Venue: ")
    eventGuests = input("No. of Guests: ")

    sql = "insert into booking(e_district, e_name, e_type, e_date, e_venue, e_guests) values('%s', '%s', '%s', '%s', '%s', %s)"
    c.execute(sql % (eventDistrict, eventName, eventType, eventDate, eventVenue, eventGuests))
    con.commit()

    print("\nEvent added successfully!")

def allEvents():
    c=con.cursor()
    sql = "select * from booking"
    c.execute(sql)
    all_events = c.fetchall()
    for i in all_events:
        print (i)

def upcomingEvents():
    today = date.today()

    c=con.cursor()
    sql = "select e_id, e_date from booking"
    c.execute(sql)
    all_events = c.fetchall()
    for i in all_events:
        if (i[1]>=today):
            sql = "select * from booking where e_id = %s"
            c.execute(sql % i[0])
            upcoming = c.fetchone()
            print (upcoming)

def pastEvents():
    today = date.today()

    c=con.cursor()
    sql = "select e_id, e_date from booking"
    c.execute(sql)
    all_events = c.fetchall()
    for i in all_events:
        if (i[1]<today):
            sql = "select * from booking where e_id = %s"
            c.execute(sql % i[0])
            upcoming = c.fetchone()
            print (upcoming)    


#Main
database()

while ex=='n' or ex=='N':
        os.system('cls')
        print ("""\n\n                * * * * * * * * * * * * * * * * * *
                *          Event Booking          *
                * * * * * * * * * * * * * * * * * *
                * 1. * ADD EVENT                  *
                * 2. * ALL EVENTS                 *
                * 3. * UPCOMING EVENTS            *
                * 4. * PAST EVENTS                *
                * 5. * EXIT                       *
                * * * * * * * * * * * * * * * * * *
                    """)
        def inp():
                        ch=input("Enter(1-5): ")
                        return ch
        r=inp()
        if r.isnumeric():
                r = int(r)

        if r==1:
                        addEvent()
        elif r==2:
                        allEvents()
        elif r==3:
                        upcomingEvents()
        elif r==4:
                        pastEvents()
        elif r==5:
                        exit()
        else :
                        print ('Try again!')
        ex=input('Exit?(y/n): ')
