import numpy as np
def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        tempor_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        tempor_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        tempor_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        tempor_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag == 1:
        x = tempor_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = tempor_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                        ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x

def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                             ascending=False).reset_index()

    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']


    return medal_tally

def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0,'Overall')

    return years,country

def countries_over_time(df):
    countries_over_time = df.drop_duplicates(['Year', 'region'])['Year'].value_counts().reset_index().sort_values(
        'Year')
    return countries_over_time
def events_over_time(df):
    events_over_time = df.drop_duplicates(['Year', 'Event'])['Year'].value_counts().reset_index().sort_values(
        'Year')
    return events_over_time

def athletes_over_time(df):
    athletes_over_time = df.drop_duplicates(['Year', 'Name'])['Year'].value_counts().reset_index().sort_values(
        'Year')
    return athletes_over_time

def most_champion(df,sport):
  tempor_df = df.dropna(subset=['Medal'])
  if sport != 'Overall':
    tempor_df = tempor_df[tempor_df['Sport'] == sport]
  a = tempor_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='Name', right_on='Name', how='left')[['Name', 'count', 'Sport', 'region']].drop_duplicates('Name')
  a.rename(columns={'count':'No of medals'}, inplace=True)
  return a

def year_wise_tally(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)

    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()
    return final_df


def most_champion_country_wise(df, country):
    tempor_df = df.dropna(subset=['Medal'])

    tempor_df = tempor_df[tempor_df['region'] == country]

    a = tempor_df['Name'].value_counts().reset_index().head(10).merge(df, left_on='Name', right_on='Name', how='left')[
        ['Name', 'count', 'Sport']].drop_duplicates('Name')
    a.rename(columns={'count': 'No of medals'}, inplace=True)
    return a