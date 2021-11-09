
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    month = ''
    day = ''
    while (True): 
        city = input("Enter your desired city (chicago, new york city, washington) : ").lower()
        if (city == 'chicago' or city == 'new york city' or city == 'washington'):
            break
        else:
            print("Oops! you have entered an invalid city, please enter one of the mentioned cities")

    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
         month = input("Enter your desired month (all, january,february,march,april,june) : ").lower()
         if(month == 'all' or month == 'january' or month =='february' or month == 'march' or month == 'april' or month =='june'):
            break
         else:
            print("Oops! you have entered an invalid month, please enter one of the mentioned months")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day = input("Enter the day of week (all,monday,tuesday,wednesday,thursday,friday,saturday,sunday) : ").lower()
        if(day == 'all' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday'):
            break
        else:
            print("Oops! you have entered an invalid day, please enter one of the mentioned days")
    

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

    #reading the file
    df = pd.read_csv(CITY_DATA[city])
    
    #converting start time to datetime
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    #defining a month from the start time column
    df['month'] = df['Start Time'].dt.month
    
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
      
    #defining a day from the start time column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("Most common month: "+ str(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]   
    print("Most common day of week: "+ common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common start hour: "+ str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].mode()[0]
    print("most commonly used start station: "+ start_station)

    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode()[0]
    print("most commonly used end station: "+end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination = (df['Start Station'] + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip: " + combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time: " + str(total_time))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print("mean travel time: " + str(mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("The counts of user types: " + str(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        # Only access Gender column in this case
        counts_gender = df["Gender"].fillna(0).value_counts()
        print("The counts of gender: "+ str(counts_gender))
        
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = min(df['Birth Year'])
        print(f"The earlies year of birth: {earliest}")

        most_recent = max(df['Birth Year'])
        print(f"The most recent year of birth: {most_recent}")

        common_year = df['Birth Year'].mode()[0]
        print(f"The most common year of birth: {common_year}")
    
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
def main():
        
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print(time_stats(df))
        print(station_stats(df))
        print(trip_duration_stats(df))
        print(user_stats(df))
        
        '''
        Displaying the retrieved data in the form of (rows x columns)
        '''
        view_data = ''
        while(True):    
            view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? : ").lower()
            if (view_data == 'yes' or view_data == 'no'):
                break
            else:
                print("Oops You have entered an invalid answer! Please Enter yes or no")
        start_loc = 0
        view_display = ''
        while (view_display != 'no'):
            if(view_data == 'no'):
                break
            else:
                print(df.iloc[0:5])
                start_loc += 5
                view_display = input("Do you wish to continue?: ").lower()
                
       
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
                    
    
    
        

if __name__ == "__main__":
	main()