from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from . models import Tables
from django.urls import reverse

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def bookTable(request):
    template = loader.get_template('bookTable.html')
    return HttpResponse(template.render({}, request))

def reserveTable(request):
    # x = request.POST['TableID']
    x = 1
    y = request.POST['DineDateTime']
    z = request.POST['DineDuration']
    x1 = request.POST['DinerName']
    x2 = request.POST['DinerAge']
    x3 = request.POST['DinerGender']
    x4 = request.POST['DinerEmail']
    x5 = request.POST['DinerPhone_num']
    x6 = request.POST['DinerAddress']
    x7 = request.POST['Guests_num']
    x8 = request.POST['Guest_list']
    t = Tables(
        TableID=x, 
        BookDateTime=y, 
        BookDuration=z,
        DinerName=x1,
        DinerAge=int(x2),
        DinerGender=x3,
        DinerEmail=x4,
        DinerPhone_num=int(x5),
        DinerAddress=x6,
        Guests_num=int(x7),
        Guest_list=x8
        )
    t.save()
    return HttpResponseRedirect(reverse('TableRecords'))

def TableRecords(request):
    myTables = Tables.objects.all().values()
    template = loader.get_template('TableRecords.html')
    context = {
        'myTables' : myTables
    }
    return HttpResponse(template.render(context,request))

def unbook(request, BookingID):
    table = Tables.objects.get(BookingID=BookingID)
    table.delete()
    return HttpResponseRedirect(reverse('TableRecords'))

def updateBooking(request, BookingID):
    myTables = Tables.objects.get(BookingID=BookingID)
    template = loader.get_template('UpdateBooking.html')
    context = {
        'myTables' : myTables
    }
    return HttpResponse(template.render(context, request))

def saveUpdate(request, BookingID):
    table = Tables.objects.get(BookingID=BookingID)
    x = 1
    y = request.POST['DineDateTime']
    z = request.POST['DineDuration']
    x1 = request.POST['DinerName']
    x2 = request.POST['DinerAge']
    x3 = request.POST['DinerGender']
    # template = loader.get_template('a.html')
    # context = {
    #     'DinerGender': x3
    # }
    # return HttpResponse(template.render(context,request))
    x4 = request.POST['DinerEmail']
    x5 = request.POST['DinerPhone_num']
    x6 = request.POST['DinerAddress']
    x7 = request.POST['Guests_num']
    x8 = request.POST['Guest_list']
    table.TableID = x
    table.BookDateTime = y
    table.BookDuration = z
    table.DinerName=x1
    table.DinerAge=int(x2)
    table.DinerGender=x3
    table.DinerEmail=x4
    table.DinerPhone_num=int(x5)
    table.DinerAddress=x6
    table.Guests_num=int(x7)
    table.Guest_list=x8
    table.save()
    return HttpResponseRedirect(reverse('TableRecords'))

# def index(request):
    # myTables = Tables.objects.all().values()
    # output = ''
    # for x in myTables:
    #     output += "\n"+str(x['BookingID'])+"\t \n"+str(x['TableID'])+"\n"+str(x['BookDateTime'])+"\n"+x['BookDuration']+"\t \n"
    # return HttpResponse(output)

'''
0) Before the actual Table ID generation starts i need a text doc with all the column names 
    of my table, that i can make manully -> "records.txt" in static folder
    - Then i need to add values under that in the order of my booking id
        for that, Take Hint:
        def index(request):
            myTables = Tables.objects.all().values()
            output = ''
            for x in myTables:
                 output += "\n"+str(x['BookingID'])+"\t \n"+str(x['TableID'])+"\n"+str(x['BookDateTime'])+"\n"+x['BookDuration']+"\t \n"
            return HttpResponse(output)
    - So similarly i need to copy the same but after the for loop is complete, i should 
        split the output string into a list with multiple items using split()
    - Now as every record has the same number of values, each complete record will be 
        repeated after a specific no. of elements (say n)
    - So i need to divide the total list length with n to to get i
        then i will run a nested loop with 
        i as upper bound in the outer loop and
        n as upper bound in the ineer loop -> printing each element with spaces in b/w
        after each iteration of inner loop, the outer loop will print "\n"
    - All this will be written into records.txt file in static folder
    
1) So what i want is that whenever a new record is added its date time is matched with other 
    entries and checked how many entries have been made of the same date time 

    Note:
    If the function fetches epmty space then the entry being made is the first entry ever
    for this we can use a default Table ID of 1

2) The number of records will specify how many tables have been booked for that time out of 
    20 tables
3) After this the function will deduct these table numbers from a list of tables numbers
    from 1 to 20
4) From the new list of unbooked tables the first element will be picked
5) It is to keep in mind that for a Table to be booked its reservation should not conflict 
    with some other reservation
6) There are are also reservation duration now for that after a table no. is picked then 
    for the booking date time and 1,2,3 will be deducted fron the hour time of the record's 
    date time value 
7) When 1 is deducted:
    if there are entries with 2 hour duration time and and the set date time then new 
    entry cannot be made with the chosen table no..
    Again the chosen table will be dedycted from the unbooked tables list and recursively 
    new table no. will chosen and will go through the same checks
    the process will be repeated for 
    if 2 is deducted with check for duration 3 hours
    if 3 is deducted with check for duration 4 hours
8) after all these checks the table id value will be returned
9) This function will be used in the reserveTable view function
'''