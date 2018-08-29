## TODO: import all necessary packages and functions
import csv # read and write csv files
import time
from datetime import datetime # operations to parse dates
from pprint import pprint # use to print data structures like dictionaries in
                          # a nicer way than the base print function.

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'
test = 'test.csv'

glb_month_filter = ""
glb_day_filter = 0

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
        if city.lower() not in ('chicago', 'new york', 'washington'):
                print("Not an appropriate choice.")
        else:
            break    
 
    if city.lower()=='chicago':
        filename=chicago
    elif city.lower()=='new york':
        filename=new_york_city
    elif city.lower()=='washington':
        filename=washington
    else:
        filename=test
        
    return filename


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) the filter option, month, day, both, or none
    '''
  
    while True:
        time_period = input('\nWould you like to filter the data by month, day, both, or not at'
                        ' all? Type "none" for no time filter.\n')
        if time_period.lower() not in ('month', 'day', 'both', 'none'):
                print("Not an appropriate choice.")
        else:
            break
    
    #set global variable for the actual month or day of the week
    global glb_month_filter
    global glb_day_filter
    
    if time_period.lower() =='month':
        glb_month_filter=get_month().lower()
    elif time_period.lower() == 'day':
        glb_day_filter=int(get_day())
    elif time_period.lower() == 'both':
        glb_month_filter=get_month().lower()
        glb_day_filter=int(get_day())      
    else:
        glb_month_filter=''
        glb_day_filter=0
        
    return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
       (str) a string representing one of the months included in the data
        
    '''
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')
        if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june'):
                print("Not an appropriate choice.")
        else:
            break

    return month


def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (int) day of the week, 1=Sunday, 2=Monday, etc...
    '''
    while True:
        day = input('\nWhich day? Please type your response as an integer (e.g., 1=Sunday).\n')
        if day.lower() not in ('1', '2', '3', '4', '5', '6', '7'):
                print("Not an appropriate choice.")
        else:
            break
        
    return int(day)

def keywithmaxval(d):
    ''' Finds the key of a dictionary for the element with the highest value
    Args:
        an input dictionary.
    Returns:
        (varies) can return any data type that is valid for use as a dictionary key
    '''
    #create a list of the dict's keys and values; 
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))] #return the key with the max value
 
def popular_month(city_file, time_period):
    '''Question: What is the most popular month for start time?
    
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - the key associated with the maximum value
            element2 - the max value associated with the key
    '''
    
    month_cnts = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 'June':0}
    

    for row in city_file:
        dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')
        mon=dateobj.strftime('%B')
        month_cnts[mon] += 1
    
    max_key=keywithmaxval(month_cnts)    
    
    return(max_key,month_cnts[max_key])


def popular_day(city_file, time_period):
    '''
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - the key associated with the maximum value
            element2 - the max value associated with the key
    '''
    day_cnts = {'Sunday':0, 'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0, 'Friday':0, 'Saturday':0}
    #day_cvt = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}

    for row in city_file:
        dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')       
        if time_period=='month': #the most popular day in the month specified
            mon=dateobj.strftime('%B').lower()
            if mon==glb_month_filter:        
                day=dateobj.strftime('%A')
                day_cnts[day] += 1
        else: #the most popular day accros all in the months in the data set
            day=dateobj.strftime('%A')
            day_cnts[day] += 1
            
    max_key=keywithmaxval(day_cnts)    
    return (max_key,day_cnts[max_key])

def popular_hour(city_file, time_period):
    '''
    Question: What is the most popular hour of day for start time?
    
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - the key associated with the maximum value
            element2 - the max value associated with the key
    '''

    hr_cnts = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}
    #day_cvt = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}

    for row in city_file:
        dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')       
        if time_period=='month': #the most popular hour in the month specified
            mon=dateobj.strftime('%B').lower()
            if mon==glb_month_filter:        
                hr=dateobj.hour
                hr_cnts[hr] += 1
        elif time_period=='day': #the most popular hour in the day of the week specified
            day=int(dateobj.strftime('%w'))+1
            if day==glb_day_filter:        
                hr=dateobj.hour
                hr_cnts[hr] += 1
        elif time_period=='both': #the most popular hour in the day of the week specified within the slected month
            mon=dateobj.strftime('%B').lower()
            day=int(dateobj.strftime('%w'))+1
            if day==glb_day_filter and mon==glb_month_filter:        
                hr=dateobj.hour
                hr_cnts[hr] += 1            
        else: #the most popular hour across all the months in the dataset
            hr=dateobj.hour
            hr_cnts[hr] += 1
            
    max_key=keywithmaxval(hr_cnts)    
    return (max_key,hr_cnts[max_key] )

def trip_duration(city_file, time_period):
    '''
    Question: What is the total trip duration and average trip duration?
    
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - total accumulated trip durations
            element2 - total number of trips
            element3 - avg trip duration
    '''
    # initialize count variables
    n_trips = 0
    n_trip_length_totals = 0.0
    avg_trip_duration=0.0
    
    for row in city_file:  
        dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')       
        if time_period=='month': #the total trips and duration in the month specified
            mon=dateobj.strftime('%B').lower()
            if mon==glb_month_filter:        
                n_trips += 1
                n_trip_length_totals += float(row['Trip Duration'])
        elif time_period=='day': #the total trips and duration for the day of weeks specified
            day=int(dateobj.strftime('%w'))+1
            if day==glb_day_filter:        
                n_trips += 1
                n_trip_length_totals += float(row['Trip Duration'])
        elif time_period=='both': #the total trips and duration for the day of weeks specified within the selected month
            mon=dateobj.strftime('%B').lower()
            day=int(dateobj.strftime('%w'))+1
            if day==glb_day_filter and mon==glb_month_filter:        
                n_trips += 1
                n_trip_length_totals += float(row['Trip Duration'])           
        else: #the total trips and  duration across the entire data set
                n_trips += 1
                n_trip_length_totals += float(row['Trip Duration'])

        # compute avg duration and  pct over 30 mins
    avg_trip_duration = n_trip_length_totals / n_trips
    return(n_trip_length_totals,n_trips, avg_trip_duration)


def dictcount(StartDict, EndDict, StartStation, EndStation):
    '''
    This is a utility function used to avoid repeating code in caller
    This code increments the counts in the dictionaries
    Args:
        (dictionary) a dictionary containing the unique starting stations.
        (dictionary) a dictionary containing the unique ending stations.
        (str) the starting station name
        (str) the ending station name
    Returns:
        (nothing) 
    '''        
    if StartStation in StartDict:
        StartDict[StartStation] += 1
    else:
        StartDict[StartStation] = 1
    
    if EndStation in EndDict:
        EndDict[EndStation] += 1
    else:
        EndDict[EndStation] = 1 
    
    return
    
def popular_stations(city_file, time_period):
    '''
    Question: What is the most popular start station and most popular end station?
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - the key associated with the maximum start station value  
            element2 - the max start station value associated with the key
            element3 - the key associated with the maximum end station value
            element4 - the max end station value associated with the key
    '''
    StartDict={}
    EndDict={}
    # TODO: complete function
    for row in city_file:  
        dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S') 
        StartStation=row['Start Station']
        EndStation=row['End Station']
        if time_period=='month': #most popular station in the month specified
            mon=dateobj.strftime('%B').lower()
            if mon==glb_month_filter:        
                dictcount(StartDict, EndDict, StartStation, EndStation)
        if time_period=='day': #most popular station on the day of week specified
            day=int(dateobj.strftime('%w'))+1
            if day==glb_day_filter:        
                dictcount(StartDict, EndDict, StartStation, EndStation)
        if time_period=='both': #most popular station on the day of week specified with the month specified
            mon=dateobj.strftime('%B').lower()
            day=int(dateobj.strftime('%w'))+1
            if mon==glb_month_filter and day==glb_day_filter:        
                dictcount(StartDict, EndDict, StartStation, EndStation)                
        else: #most popular station across the entire data set irrespective of month or day of week
            dictcount(StartDict, EndDict, StartStation, EndStation)
    
    max_key1=keywithmaxval(StartDict)    
    max_key2=keywithmaxval(EndDict)    
           
    return(max_key1,StartDict[max_key1],max_key2,EndDict[max_key2])

def dicttripcount(TripDict, TripTupleKey):
    '''
    This is a utility function used to avoid repeating code in caller
    This code increments the counts in the dictionary
    Args:
        (dictionary) a dictionary containing the unique trips.
        (str) the trip name used as the dictionary key

    Returns:
        (nothing) 
    '''            
    if TripTupleKey in TripDict:
        TripDict[TripTupleKey] += 1
    else:
        TripDict[TripTupleKey] = 1
    
    return

def popular_trip(city_file, time_period):
    '''
    Question: What is the most popular trip?
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - the key associated with the maximum trip value  
            element2 - the max trip value associated with the key
    '''
    TripDict={}
    TripTupleKey = ();
    # use a tuple of start and end station as key in dictionary
    # add each unique start/end pair tuple to the dictionary
    #increment count associated with unique pairs and determine max dictionary element
    for row in city_file:  
        dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S') 
        StartStation=row['Start Station']
        EndStation=row['End Station']
        TripTupleKey = (StartStation,EndStation )
        if time_period=='month': #most popular trip in the month specified
            mon=dateobj.strftime('%B').lower()
            if mon==glb_month_filter:        
                dicttripcount(TripDict, TripTupleKey)
        elif time_period=='day':#most popular trip in the day of week specified (irrespective of month)
            day=int(dateobj.strftime('%w'))+1
            if day==glb_day_filter:        
                dicttripcount(TripDict, TripTupleKey)
        elif time_period=='both':#most popular trip in the day of week specified (within the slected month)
            mon=dateobj.strftime('%B').lower()
            day=int(dateobj.strftime('%w'))+1
            if mon==glb_month_filter and day==glb_day_filter:        
                dicttripcount(TripDict, TripTupleKey)                
        else: #most popular trip accross entire dataset irresctive of month or day of week
            dicttripcount(TripDict, TripTupleKey)
    
    max_key=keywithmaxval(TripDict)    

    return (max_key,TripDict[max_key])

def users(city_file, time_period):
    '''
    Question: What are the counts of each user type?
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - count of subscribers 
            element2 - count of customers
    '''
    user_cnts = {'Subscriber':0,'Customer':0}
    #day_cvt = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}

    for row in city_file:
        if row['User Type'] != '' and row['User Type'] != 'Dependent':
            dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')       
            if time_period=='month': #number of users types in a month selected
                mon=dateobj.strftime('%B').lower()
                if mon==glb_month_filter:        
                    user_cnts[row['User Type']] += 1
            elif time_period=='day': #number of users types in a day of week selected (irrespective of month)
                day=int(dateobj.strftime('%w'))+1
                if day==glb_day_filter:        
                    user_cnts[row['User Type']] += 1
            elif time_period=='both': #number of users types in on the day of week selected (within a specified month)
                mon=dateobj.strftime('%B').lower()
                day=int(dateobj.strftime('%w'))+1
                if mon==glb_month_filter and day==glb_day_filter:        
                    user_cnts[row['User Type']] += 1
            else: #number of users types across entire data set irrespective of month or day of week
                user_cnts[row['User Type']] += 1
            
    return (user_cnts['Subscriber'],user_cnts['Customer'])

def gender(city_file, time_period):
    '''
    Question: What are the counts of gender?
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - count of males
            element2 - count of females
    '''
    gender_cnts = {'Male':0,'Female':0}
    #day_cvt = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}

    for row in city_file:
        if row['Gender'] != '':
            dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S')       
            if time_period=='month': #gender of riders within the month specified
                mon=dateobj.strftime('%B').lower()
                if mon==glb_month_filter:        
                    gender_cnts[row['Gender']] += 1
            elif time_period=='day': #gender of riders on the day of week specified (irrespective of month)
                day=int(dateobj.strftime('%w'))+1
                if day==glb_day_filter:        
                    gender_cnts[row['Gender']] += 1
            elif time_period=='both': #gender of riders on the day of week specified (within the specified month)
                mon=dateobj.strftime('%B').lower()
                day=int(dateobj.strftime('%w'))+1
                if mon==glb_month_filter and day==glb_day_filter:        
                    gender_cnts[row['Gender']] += 1
            else: #gender of riders on the day of week specified (within the specified month)
                gender_cnts[row['Gender']] += 1
            
    return (gender_cnts['Male'], gender_cnts['Female'])

def birth_years(city_file, time_period):
    '''
    Question: What are the earliest, most recent, and most popular birth years?
    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
        (str) time_period, represents the filter option, month, day, both, or none
    Returns:
        (tuple) 
            element1 - earliest date of birth
            element2 - most ecent date of birth
            element3 - date of birth year associated with the most riders
            element4 - count of riders assocated with most popular date of birth
    '''
    BirthDict={}
    EarliestYear=3000.0
    LatestYear=0.0
    # TODO: complete function
    for row in city_file:
        if row['Birth Year'] != '':
            dateobj = datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M:%S') 
            if time_period=='month': #birth years in the month specified
                mon=dateobj.strftime('%B').lower()
                if mon==glb_month_filter:        
                    if row['Birth Year'] in BirthDict:
                        BirthDict[row['Birth Year']] += 1
                    else:
                        BirthDict[row['Birth Year']] = 1
                    if float(row['Birth Year']) > LatestYear: LatestYear=float(row['Birth Year'])
                    if float(row['Birth Year']) < EarliestYear: EarliestYear=float(row['Birth Year'])
            elif time_period=='day': #birth years in the day of week specified (irrespective of month)
                day=int(dateobj.strftime('%w'))+1
                if day==glb_day_filter:        
                    if row['Birth Year'] in BirthDict:
                        BirthDict[row['Birth Year']] += 1
                    else:
                        BirthDict[row['Birth Year']] = 1
                if float(row['Birth Year']) > LatestYear: LatestYear=float(row['Birth Year'])
                if float(row['Birth Year']) < EarliestYear: EarliestYear=float(row['Birth Year'])
            elif time_period=='both': #birth years in the day of week specified (within the selected month)
                mon=dateobj.strftime('%B').lower()
                day=int(dateobj.strftime('%w'))+1
                if mon==glb_month_filter and day==glb_day_filter:        
                    if row['Birth Year'] in BirthDict:
                        BirthDict[row['Birth Year']] += 1
                    else:
                        BirthDict[row['Birth Year']] = 1
                if float(row['Birth Year']) > LatestYear: LatestYear=float(row['Birth Year'])
                if float(row['Birth Year']) < EarliestYear: EarliestYear=float(row['Birth Year'])
            else: #birth years across the entire data set irrespectiv eof day of week or month
                if row['Birth Year'] in BirthDict:
                    BirthDict[row['Birth Year']] += 1
                else:
                    BirthDict[row['Birth Year']] = 1
                if float(row['Birth Year']) > LatestYear: LatestYear=float(row['Birth Year'])
                if float(row['Birth Year']) < EarliestYear: EarliestYear=float(row['Birth Year'])
    
    max_key=keywithmaxval(BirthDict)    

    return(EarliestYear,LatestYear,max_key,BirthDict[max_key])

def display_data(city_file):
    '''
    Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        (dictionary) a dictionary containing the rows of data read from the CSV file.
    Returns:
        none
    '''
    count = 0
        
    for row in city_file:
        pprint(row)
        count +=1
        if count==5:          
            while True:
                display = input('\nWould you like to view individual trip data?'
                                'Type \'yes\' or \'no\'.\n')
                if display.lower() not in ('yes', 'no'):
                        print("Not an appropriate choice.")
                else: break 
            
            if display.lower() == 'yes':
                count=0
                continue
            else: break   
    return

def csv_dict_list(variables_file):
    '''
    Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    Args:
        (variable-based csv) the CSV file.
    Returns:
        (dictionary) - map values to a list of dictionaries containing key/value pairs

    '''
        
    with open(variables_file, 'r') as f_in:
        reader = csv.DictReader(f_in)
        dict_list = []
        for line in reader:
            dict_list.append(line)  
    
    # the list comprehension approach is commented out below, the performace
    # was no better than the method I used above, in either case I am reading
    # the file once and storing it in a dictionary, the overall performance is
    # still impacted by the size of the file and the approach which is  
    # heavily dependent on looping           
    '''
    with open(variables_file) as f:
        dict_list  = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    '''   
    return dict_list 

def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    city_file=csv_dict_list(city)

    # Filter by time period (month, day, both, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')   
    
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        rtn = popular_month(city_file, time_period) 
        print("Most popular month:{0}, Count:{1}, Filter:{2}".format(rtn[0], rtn[1], time_period))
    
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        rtn=popular_day(city_file, time_period)
        print("Most popular day:{0}, Count:{1}, Filter:{2}".format(rtn[0], rtn[1], time_period))
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic......")   

    start_time = time.time()

    # What is the most popular hour of day for start time?
    rtn=popular_hour(city_file, time_period)
    print("Most popular hour:{0}, Count:{1}, Filter:{2}".format(rtn[0], rtn[1], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...trip_duration:")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    rtn=trip_duration(city_file, time_period)
    print("Total Duration:{0}, Count:{1}, Avg Duration:{2}, Filter:{3}".format(rtn[0], rtn[1], rtn[2], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...popular_station")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    rtn=popular_stations(city_file, time_period)
    print("Start Station:{0}, Count:{1} - End Station:{2}, Count:{3}, Filter:{4}".format(rtn[0], rtn[1], rtn[2], rtn[3], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...popular_trip")
    start_time = time.time()

    # What is the most popular trip?
    rtn=popular_trip(city_file, time_period)
    print("Trip:{0}, Count:{1}, Filter:{2}".format(rtn[0], rtn[1], time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...user_type")
    start_time = time.time()

    # What are the counts of each user type?
    rtn=users(city_file, time_period)
    print("Subscribers:{0}, Customers:{1}, Filter:{2}".format(rtn[0], rtn[1], time_period))

    if city.lower() != 'washington.csv':
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...gender")
        start_time = time.time()
    
        # What are the counts of gender?
        rtn=gender(city_file, time_period)
        print("Male:{0}, Female:{1}, Filter:{2}".format(rtn[0], rtn[1], time_period))
    
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...birth_year")
        start_time = time.time()
    
        # What are the earliest, most recent, and most popular birth years?
        rtn=birth_years(city_file, time_period)
        print("Birth Years: Earliest:{0}, Recent:{1}, Popular:{2}, Count:{3}, Filter:{4}".format(rtn[0], rtn[1], rtn[2], rtn[3],time_period))

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    statistics()