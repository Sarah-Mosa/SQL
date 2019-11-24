import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
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
    city=input("please input name of the city : \n ").lower()
    while not city in CITY_DATA :
           city= input("please input name of the city again : \n").lower()

    # get user input for month (all, january, february, ... , june)
    month=input("please input name of the month : \n ").lower()
    while not month in months :
            month= input("please input name of the month again : \n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("please input name of the day : \n ").lower()
    while not day in days :
            day= input("please input name of the day again : \n").lower()

    print('-'*40)
    return city,month,day


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
    # TO DO: Load data to df
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # display the most common month

    months_count = df['month'].value_counts().idxmax()

    print('Most common month is {}.'.format(months_count))

    # display the most common day of week
    days_count = df['day_of_week'].value_counts().idxmax()
    print('Most common day of week is {}.'.format(days_count))

    # display the most common start hour
    df['Hours'] = pd.to_datetime(df['Start Time']).dt.hour
    hours_count = df['Hours'].value_counts()

    print('Most common hour is {}'.format(hours_count.idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station_counts = df['Start Station'].value_counts()
    print('Most commonly used start station is {}'.format(Start_Station_counts.idxmax()))
    # display most commonly used end station
    End_Station_counts = df['End Station'].value_counts()
    print('Most commonly used end station is {}'.format(Start_Station_counts.idxmax()))
    # display most frequent combination of start station and end station trip
    df['Start End stations'] = df['Start Station'] + df['End Station']
    Start_End_Station = df['Start End stations'].value_counts()

    print('Most commonly used start station and end station is {}.'.format(Start_End_Station.idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time_sum = df['Trip Duration'].sum()
    print('Total travel time is {}.'.format(total_time_sum))
    # display mean travel time
    total_time_mean = df['Trip Duration'].mean()
    print('Total traveling mean time is {}.'.format(total_time_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df['User Type'].value_counts()
    print('Total Counts of user type are {}.'.format(count_user))
    # Display counts of gender
    if 'Gender' in df:
        count_user_gender = df['Gender'].value_counts()
        print('Total Counts of user Gender type are \n{}.'.format(count_user_gender))
        # Display earliest, most recent, and most common year of birth
        print('Earliest, most recent, and most common year of births are {}, {} and {}.'.format(df['Birth Year'].min(),df['Birth Year'].max(), df['Birth Year'].mode()[0]))
    else:
        print("Gender and Birth Year data does not exist.")    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    show_row=5
    rows_start = 0
    rows_end = show_row - 1 
    
    while True :
        user_input= input('      (yes or no):  ')
        if user_input.lower() != 'no':
            print('\n    Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))
            print(df.iloc  [rows_start : rows_end + 1])
            rows_start += show_row
            rows_end += show_row
            print('\n    Would you like to see the next {} rows?'.format(show_row))
            continue

        else:
            break 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        # Here only Start

        # Hear Only End   
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
