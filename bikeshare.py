import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_selection = True
    valid_city_list = ["1", "2", "3", "chicago", "new york city", "washington"]

    while(city_selection):    
        response="no"
        city = input("Please select the city: \n\n 1. Chicago\n 2. New York City\n 3. Washington\n\n").strip().lower()
    
        if(city in valid_city_list):
        
            if(city == "1"):
                city = "chicago"
            elif(city == "2"):
                city = "new york city"
            elif(city == "3"):
                city = "washington"

    # get user input for approval
            response = input("You have selected {}, type 'yes' to approve or type anything to start over.\n\n".format(city.title())).strip().lower()
            if(response == "yes"):
                city_selection = False

        else:
            print("\n!!! Please enter 1/2/3 or city name !!!\n")


    # get user input for month (all, january, february, ... , june)

    month_selection = True
    valid_month_list = ["0", "1", "2", "3", "4", "5", "6", "all", "jan", "feb", "mar", "apr", "may", "jun", "january", "february", "march", "april", "may", "june"]

    while(month_selection):    
        response="no"
        month = input("Please select month: \n\n 0. All\n 1. January\n 2. February\n 3. March\n 4. April\n 5. May\n 6. June\n\n").strip().lower()
    
        if(month in valid_month_list):
        
            if(month == "0"):
                month = "all"
            elif(month == "1" or month == "jan"):
                month = "january"
            elif(month == "2" or month == "feb"):
                month = "february"
            elif(month == "3" or month == "mar"):
                month = "march"
            elif(month == "4" or month == "apr"):
                month = "april"
            elif(month == "5" or month == "may"):
                month = "may"
            elif(month == "6" or month == "jun"):
                month = "june"

    # get user input for approval
            response = input("You have selected {}, type 'yes' to approve or type anything to start over.\n\n".format(month.title())).strip().lower()
            if(response == "yes"):
                month_selection = False

        else:
            print("\n!!! Please enter 0/1/2/3/4/5/6 or month name !!!\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_selection = True
    valid_day_list = ["0", "1", "2", "3", "4", "5", "6", "7", "all", "mon", "tue", "wed", "thu", "fri", "sat", "sun", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    while(day_selection):    
        response="no"
        day = input("Please select day: \n\n 0. All\n 1. Monday\n 2. Tuesday\n 3. Wednesday\n 4. Thursday\n 5. Friday\n 6. Saturday\n 7. Sunday\n\n").strip().lower()
    
        if(day in valid_day_list):
        
            if(day == "0"):
                day = "all"
            elif(day == "1" or day == "mon"):
                day = "monday"
            elif(day == "2" or day == "tue"):
                day = "tuesday"
            elif(day == "3" or day == "wed"):
                day = "wednesday"
            elif(day == "4" or day == "thu"):
                day = "thursday"
            elif(day == "5" or day == "fri"):
                day = "friday"
            elif(day == "6" or day == "sat"):
                day = "saturday"
            elif(day == "7" or day == "sun"):
                day = "sunday"

    # get user input for approval
            response = input("You have selected {}, type 'yes' to approve or type anything to start over.\n\n".format(day.title())).strip().lower()
            if(response == "yes"):
                day_selection = False

        else:
            print("\n!!! Please enter 0/1/2/3/4/5/6/7 or day name !!!\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()


    if(month != 'all'):
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        df = df[df['Month'] == month]


    if(day != 'all'):
        df = df[df['Day of Week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['all', 'January', 'February', 'March', 'April', 'May', 'June']
    month_common = df['Month'].mode()[0]
    print("Most common month: {}".format(months[month_common].title()))

    # display the most common day of week
    day_common = df['Day of Week'].mode()[0]
    print("Most common day: {}".format(day_common))

    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    hour_common = df['Hour'].mode()[0]
    print("Most common hour: {}".format(hour_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    df.drop('Month',axis=1,inplace=True)
    df.drop('Day of Week',axis=1,inplace=True)
    df.drop('Hour',axis=1,inplace=True)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_common = df['Start Station'].mode()[0]
    print("Most common Start Station is {}".format(start_station_common))


    # display most commonly used end station
    end_station_common = df['End Station'].mode()[0]
    print("Most common End Station is {}".format(end_station_common))


    # display most frequent combination of start station and end station trip
    df['Comb Station'] = 'Start Station: ' + df['Start Station'] + '\n' + 31*' ' + 'End Station: ' + df['End Station']
    comb_station_common = df['Comb Station'].mode()[0]
    print("Most frequent combination is {}".format(comb_station_common))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    df.drop('Comb Station',axis=1,inplace=True)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = int(df['Trip Duration'].sum())
    trip_seconds = total_trip_duration % 60

    if(total_trip_duration > 86400):
       trip_days = total_trip_duration / 86400
       total_trip_duration = total_trip_duration % 86400
    else:
        trip_days = 0

    if(total_trip_duration > 3600):
       trip_hours = total_trip_duration / 3600
       total_trip_duration = total_trip_duration % 3600
    else:
        trip_hours = 0

    if(total_trip_duration > 60):
       trip_minutes = total_trip_duration / 60
    else:
        trip_minutes = 0

    print("Total trip duration: {} days {} hours {} minutes {} seconds.".format(int(trip_days), int(trip_hours), int(trip_minutes), int(trip_seconds)))




    # display mean travel time
    mean_trip_duration = int(df['Trip Duration'].mean())
    mean_seconds = mean_trip_duration % 60

    if(mean_trip_duration > 86400):
       mean_days = mean_trip_duration / 86400
       mean_trip_duration = mean_trip_duration % 86400
    else:
        mean_days = 0

    if(mean_trip_duration > 3600):
       mean_hours = mean_trip_duration / 3600
       mean_trip_duration = mean_trip_duration % 3600
    else:
        mean_hours = 0

    if(mean_trip_duration > 60):
       mean_minutes = mean_trip_duration / 60
    else:
        mean_minutes = 0

    print("Mean trip duration: {} days {} hours {} minutes {} seconds.".format(int(mean_days), int(mean_hours), int(mean_minutes), int(mean_seconds)))




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    total_utype_count = 0
    user_type = df.groupby('User Type',as_index=False).count()
    for i in range(len(user_type)):
        print('{} count: {}'.format(user_type['User Type'][i], user_type['Trip Duration'][i]))
        total_utype_count += user_type['Trip Duration'][i]
    print('Missing user type data count: {}'.format(len(df) - total_utype_count))


    # Display counts of gender
    print("\n")
    """
    First of all we need to check whether Gender data present or not
    """

    if 'Gender' in df:
        total_gender_count = 0
        user_gender = df.groupby('Gender',as_index=False).count()
        for i in range(len(user_gender)):
            print('{} count: {}'.format(user_gender['Gender'][i], user_gender['Trip Duration'][i]))
            total_gender_count += user_gender['Trip Duration'][i]
        print('Missing gender data count: {}'.format(len(df) - total_gender_count))
    else:
        print('No gender data for this city')


    # Display earliest, most recent, and most common year of birth
    print("\n")
    """
    First of all we need to check whether Birth Year data present or not
    """

    if 'Birth Year' in df:
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("Earliest Birth Year: {}\nMost Recent Birth Year: {}\nMost Common Birth Year: {}".format(int(min_birth_year), int(max_birth_year), int(common_birth_year)))
    else:
        print('No birth year data for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
