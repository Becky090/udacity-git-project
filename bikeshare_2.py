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
    citys = ('chicago', 'new york city','washington')
    monthss = ('january','february','march','april','may','june')
    dayss = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    explore = "\nEnter the city you want to explore,"
    explore += "\nLet your answer be chicago, new york city or washington: "
    city = ""
    months = "\nEnter month you're interested in, "
    months += "\nMonth must be between january and june. if interested in all, type 'all': "
    month =""
    days = "\nwhat day are you interested in,"
    days += "\nDay must be written in full eg 'Monday' if interested in all, type 'all': "
    day = ""
    #while True:
    city = input(explore).lower()
    while city not in citys:
        city = input(explore).lower()
    else:
        print(city)

    # get user input for month (all, january, february, ... , june)
    month = input(months).lower()
    while month not in monthss and month != 'all':
        month = input(months).lower()
    else:
        print(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(days).lower()
    while day not in dayss and day != 'all':
        day = input(days).lower()
    else:
        print(day)

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

    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()
    print('Most common Start month:',common_month)

    # display the most common day of week

    most_common_day = df['day_of_week'].mode()
    print('Most common Start day:',most_common_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()
    print('Most common Start Hour:',common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('Hey you! yeah!! Keep on exploring !!!')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_station = df['Start Station'].mode()
    print('Most popular start station:',common_station)


    # display most commonly used end station
    end_station = df['End Station'].mode()
    print('Most popular end station:',end_station)

    print('breaking')
    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station']+","+df['End Station']
    frequent_combination = df['Start End'].mode()
    print('Most Frequently combined start and end station is :',frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:',total_travel_time)


    # display mean travel time
    total_travel_mean = df['Trip Duration'].mean()
    print('Total travel mean is:',total_travel_mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_of_user_type = df['User Type'].value_counts()
    print('count of user type:',count_of_user_type)


    # Display counts of gender
    if city != 'washington':
        count_of_gender = df['Gender'].value_counts()
        print('count of gender:',count_of_gender)

        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min()
        print('Earliest year of birth:',earliest_year_of_birth)

        print()

        recent_year_of_birth = df['Birth Year'].max()
        print('Recent year of birth:',recent_year_of_birth)

        print()

        most_common_birth_year = df['Birth Year'].mode()
        print('Most common birth year:',most_common_birth_year)
    else:
        print('Sorry,the city Washignton does not have the Gender and Birth year column.')

        print()

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def only_five_rows(df):
    i = 0
    stop = input('Are you interested in just five rows of the output ?Type Yes or No: ').lower()
    if stop not in ['yes','no']:
        stop = input('Are you interested in just five rows of  the output?Type Yes or No: ').lower()
    else:
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            stop = input('Are you interested in just five rows of the output?Type Yes or No: ').lower()
            if stop != 'yes':
                print('Have a nice time.')
                break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        only_five_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
