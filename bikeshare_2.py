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

    while True:
        city = input("\n Choose a citiy for which you would like to research some Data on. chicago, new york city or washington\n")
        if city not in ('chicago', 'new york city', 'washington'):
            print ("Please try again and choose one of the following three cities: chicago, new york city or washington.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input ("\n Which month do you want to use for your data? January, February, March, April, May, June or type 'all' if you want all the months\n")
        if month not in ('January','February', 'March', 'April', 'May', 'June', 'all'):
            print ("Please try again and input one of the choices above.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Now enter a specific day of the week you want to look at or type 'all' if you want to look at all the days\n")
        if day not in ('Monday','monday', 'Tuesday', 'tuesday', 'Wednesday', 'wednesday','Thursday', 'thuesday', 'Friday', 'friday', 'Saturday', 'saturday', 'Sunday', 'sunday', 'all'):
            print ("\n Please try again and input one of the choices above.")
            continue
        else:
            break

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

    # Load Data File into Dataframe ( Information on this steps in Udacity Bikeshare Project Practice quiz 3)
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime (Information on this steps in Udacity Bikeshare Project Practice quiz 3)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns (Information on this steps in Udacity Bikeshare Project Practice quiz 3)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable (Information on this steps in Udacity Bikeshare Project Practice quiz 3)
    if month != 'all':

    # use the index of the months list to get the corresponding int (Information on this steps in Udacity Bikeshare Project Practice quiz 3)
       months = ['January', 'February', 'March', 'April', 'May', 'June']
       month = months.index(month) + 1

    # filter by month to create the new dataframe (Information on this steps in Udacity Bikeshare Project Practice quiz 3)
       df = df[df['month'] == month]

    # filter by day of week if applicable(Information on this steps in Udacity Bikeshare Project Practice quiz 3)
    if day != 'all':

    # filter by day of week to create the new dataframe(Information on this steps in Udacity Bikeshare Project Practice quiz 3)
       df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month. Use mode function to get the solution.
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['Start Time'].dt.month.mode())
    common_month = months[index-1]
    print('The most common month is {}.'.format(common_month))


    # display the most common day of week.  Use mode function to get the solution.
    common_day = df['day_of_week'].mode()[0]
    print('The most comon day of the week is:', common_day)

    # display the most common start hour.(Similar to Udacity Bikeshare Project Practice quiz 1)
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most comon start hour is:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print('The most used Start Station is:', Start_Station)

    # display most commonly used end station
    End_Station = df['End Station'].mode()[0]
    print('The most used End Station is:', End_Station)

    # display most frequent combination of start station and end station trip
    df['Combination']=df['Start Station'] + df['End Station']
    Comb_Station = df['Combination'].value_counts().idxmax()
    print('\n The most used combination is:', Comb_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('The total travel time is:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types. (Information on this steps in Udacity Bikeshare Project Practice quiz 2)
    user_types = df['User Type'].value_counts()
    print('The User Types:\n', user_types)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('The Gender Type is:\n', gender_count)
    except KeyError:
        print("\n The Gender Type is: \n No Data available at this moment.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('The earliest year is:', earliest_year)
    except KeyError:
        print("\n The Gender Type is: \n No Data available at this moment.")

    #Most recent Year of Birth
    try:
        most_recent_year = df['Birth Year'].max()
        print('The most recent year is:', most_recent_year)
    except KeyError:
        print("\n The Gender Type is: \n No Data available at this moment.")

    #Most common Year of birth
    try:
        most_common_year = df['Birth Year'].mode()[0]
        print('The most common year is:', most_common_year)
    except KeyError:
        print("\n The Gender Type is: \n No Data available at this moment.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    #This will show raw data to the user 5 rows at a time for as long as he keeps requesting it.

    #Definition of starting and ending rows of data to be Display.
    start_loc = 0
    end_loc = 10

    data = input("Would you like to see 5 rows of raw data? ")

    #use df.shape to get the number of rows and columns.  iloc selects the row and columns in Panda Dataframe.
    if data == 'yes':
        while end_loc <= df.shape[0] -1:
            print(df.iloc[start_loc:end_loc, :])
            start_loc += 10
            end_loc +=10

            stop_data = input("Do you want to continue?")
            if stop_data == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
