import pandas as pd
import configparser as cp
from sqlalchemy import create_engine

config = cp.ConfigParser()
config.read('config.ini')


def database_config():
    """
    Creating database connection using config.ini file.
    """
    user = config['mysqlDB']['user']
    pwd = config['mysqlDB']['pass']
    host = config['mysqlDB']['host']
    db_name = config['mysqlDB']['db']

    db_connection_str = 'mysql+pymysql://{user}:{pwd}@{host}:3306/{db_name}'.format(user=user, pwd=pwd, host=host,
                                                                                    db_name=db_name)

    engine = create_engine(db_connection_str)
    return engine


def df_to_db(engine, df, table_name, INDEX=False):
    """ Takes 3 input

    engine: database engine i.e. database_config return
    df: dataframe with data
    table_name: name of the table where dataframe's data need to be pushed into.

    Will be passing database engine details to make connection with MySQL database with table name where dataframe's
    data need to be pushed into. """
    try:
        df.to_sql(table_name, con=engine, index=INDEX, if_exists='append')
        return True
    except:
        return False


if __name__ == "__main__":

    # engine = database_config()
    df_excelWithAccount = pd.read_excel("Data/EXCEL LIST.xlsx")

    account_details = pd.read_csv("Data/Data - DF/Accounts_001.csv")
    contact_details = pd.read_csv("Data/Data - DF/Contacts_001.csv")
    lead_details = pd.read_csv("Data/Data - DF/Leads_001.csv")
    potential_details = pd.read_csv("Data/Data - DF/Potentials_001.csv")
    visits_details = pd.read_csv("Data/Data - DF/Visite_C_001.csv")
    user_details = pd.read_csv("Data/Data - DF/Users_001.csv")
    notes_details = pd.read_csv("Data/Data - DF/Notes_001.csv")
    attachments_details = pd.read_csv("Data/Data - DF/Attachments_001.csv")
    call_details = pd.read_csv("Data/Data - DF/Calls_001.csv")
    email_details = pd.read_csv("Data/Data - DF/Emails_001.csv")
    event_details = pd.read_csv("Data/Data - DF/Events_001.csv")
    forecast_details = pd.read_csv("Data/Data - DF/Forecasts_001.csv")
    tasks_details = pd.read_csv("Data/Data - DF/Tasks_001.csv")
    solutions_details = pd.read_csv("Data/Data - DF/Solutions_001.csv")
    potentialProject_details = pd.read_csv("Data/Data - DF/Potential_Projects_C_001.csv")
    potentialCopyC_details = pd.read_csv("Data/Data - DF/Potentials_Copy_C_001.csv")

    # 1. findAllAccounts

    accountname_tofilter = df_excelWithAccount['Account Name'].tolist()
    account_details_filtered = account_details[account_details['Account Name'].isin(accountname_tofilter)]
    account_details_filtered.to_csv('Output/account_details_filtered.csv')

    #/***************************************************************************
    #
    # #This will write filtered account name in the MySQL
    # database under given "table_name"
    #
    # df_to_db(engine, account_details_filtered, 'table_name')
    # /***************************************************************************

    # 2. findAllContactsForAccount
    contact_tofilter = account_details_filtered['Account ID'].tolist()
    contact_details_filtered = contact_details[contact_details['Account ID'].isin(contact_tofilter)]
    contact_details_filtered.to_csv('Output/contact_details_filtered.csv')

    # 3. findAllleadsForAccount
    leads_tofilter = account_details_filtered['Account ID'].tolist()
    leads_details_filtered = lead_details[lead_details['Account ID'].isin(leads_tofilter)]
    leads_details_filtered.to_csv(
        'Output/Leads_details_filtered.csv')

    # 4. findAllPotentialsForAccount
    potential_tofilter = account_details_filtered['Account ID'].tolist()
    potential_details_filtered = potential_details[potential_details['Account ID'].isin(potential_tofilter)]
    potential_details_filtered.to_csv(
        'Output/potential_details_filtered.csv')

    # 5. findAllVisitesForAccount
    visits_tofilter = account_details_filtered['Account ID'].tolist()
    visits_details_filtered = visits_details[visits_details['Account ID'].isin(visits_tofilter)]
    visits_details_filtered.to_csv(
        'Output/visits_details_filtered.csv')


    # 6. findAllUsersForAccount
    users_tofilter = account_details_filtered['Account Owner ID'].tolist()
    users_details_filtered = user_details[user_details['Added By Id'].isin(users_tofilter)]
    users_details_filtered.to_csv(
        'Output/users_details_filtered.csv')

    # 7. findAllNotesForAccount
    notes_tofilter = users_details_filtered['User ID'].tolist()
    notes_details_filtered = notes_details[notes_details['Note Owner ID'].isin(notes_tofilter)]
    notes_details_filtered.to_csv(
        'Output/notes_details_filtered.csv')

    # 8. findAttachmentsForAccount
    attachments_tofilter = users_details_filtered['User ID'].tolist()
    attachments_details_filtered = attachments_details[attachments_details['Attachment Owner ID'].isin(attachments_tofilter)]
    attachments_details_filtered.to_csv(
        'Output/attachments_details_filtered.csv')

    # 9. findAllCallsForAccount
    calls_tofilter = users_details_filtered['User ID'].tolist()
    calls_details_filtered = call_details[call_details['Call Owner Id'].isin(calls_tofilter)]
    calls_details_filtered.to_csv(
        'Output/calls_details_filtered.csv')

    # 10. findAllEmailsForAccount
    emails_tofilter = users_details_filtered['User ID'].tolist()
    emails_details_filtered = email_details[email_details['Email Owner Id'].isin(emails_tofilter)]
    emails_details_filtered.to_csv(
        'Output/emails_details_filtered.csv')

    # 11. findAllEventsForAccount
    events_tofilter = users_details_filtered['User ID'].tolist()
    events_details_filtered = event_details[event_details['Event Owner ID'].isin(events_tofilter)]
    events_details_filtered.to_csv(
        'Output/events_details_filtered.csv')

    # 12. findAllForecastsForAccount
    forecast_tofilter = users_details_filtered['User ID'].tolist()
    forecast_details_filtered = forecast_details[forecast_details['Forecast Owner ID'].isin(forecast_tofilter)]
    forecast_details_filtered.to_csv(
        'Output/forecast_details_filtered.csv')

    # 13. findAllTasksForAccount
    tasks_tofilter = users_details_filtered['User ID'].tolist()
    tasks_details_filtered = tasks_details[tasks_details['Task Owner ID'].isin(tasks_tofilter)]
    tasks_details_filtered.to_csv(
        'Output/tasks_details_filtered.csv')

    # 14. findAllSolutionsForAccount
    solutions_tofilter = users_details_filtered['User ID'].tolist()
    solutions_details_filtered = solutions_details[solutions_details['Solution Owner ID'].isin(solutions_tofilter)]
    solutions_details_filtered.to_csv(
        'Output/solutions_details_filtered.csv')

    # 15. findAllPotentialProjectsForAccount
    potentialProject_tofilter = users_details_filtered['User ID'].tolist()
    potentialProject_details_filtered = potentialProject_details[potentialProject_details['Potential Projects Owner ID'].isin(potentialProject_tofilter)]
    potentialProject_details_filtered.to_csv(
        'Output/potentialProject_details_filtered.csv')

    # 16. findAllPotentialCopyCForAccount
    potentialCopyC_tofilter = users_details_filtered['User ID'].tolist()
    potentialCopyC_details_filtered = potentialCopyC_details[potentialCopyC_details['Potential Copy Owner ID'].isin(potentialCopyC_tofilter)]
    potentialCopyC_details_filtered.to_csv(
        'Output/potentialCopyC_details_filtered.csv')



