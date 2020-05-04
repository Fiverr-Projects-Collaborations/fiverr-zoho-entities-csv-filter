import pandas as pd

if __name__ == "__main__":
    # engine = database_config()
    rootDataDir = "Data/"
    dataFilesDir = "Data - DF/"
    df_excelWithAccount = pd.read_excel(rootDataDir + "EXCEL LIST.xlsx")
    account_details = pd.read_csv(rootDataDir + dataFilesDir + "Accounts_001.csv")
    contact_details = pd.read_csv(rootDataDir + dataFilesDir + "Contacts_001.csv")
    lead_details = pd.read_csv(rootDataDir + dataFilesDir + "Leads_001.csv")
    potential_details = pd.read_csv(rootDataDir + dataFilesDir + "Potentials_001.csv")
    visits_details = pd.read_csv(rootDataDir + dataFilesDir + "Visite_C_001.csv")
    user_details = pd.read_csv(rootDataDir + dataFilesDir + "Users_001.csv")
    notes_details = pd.read_csv(rootDataDir + dataFilesDir + "Notes_001.csv")
    attachments_details = pd.read_csv(rootDataDir + dataFilesDir + "Attachments_001.csv")
    call_details = pd.read_csv(rootDataDir + dataFilesDir + "Calls_001.csv")
    email_details = pd.read_csv(rootDataDir + dataFilesDir + "Emails_001.csv")
    event_details = pd.read_csv(rootDataDir + dataFilesDir + "Events_001.csv")
    forecast_details = pd.read_csv(rootDataDir + dataFilesDir + "Forecasts_001.csv")
    tasks_details = pd.read_csv(rootDataDir + dataFilesDir + "Tasks_001.csv")
    solutions_details = pd.read_csv(rootDataDir + dataFilesDir + "Solutions_001.csv")
    potentialProject_details = pd.read_csv(rootDataDir + dataFilesDir + "Potential_Projects_C_001.csv")
    potentialCopyC_details = pd.read_csv(rootDataDir + dataFilesDir + "Potentials_Copy_C_001.csv")
    accounts_record_access_details = pd.read_csv(rootDataDir + dataFilesDir + "Accounts_RecordAccess_001.csv")
    calls_record_access_details = pd.read_csv(rootDataDir + dataFilesDir + "Calls_RecordAccess_001.csv")
    contacts_record_access_details = pd.read_csv(rootDataDir + dataFilesDir + "Contacts_RecordAccess_001.csv")
    events_record_access_details = pd.read_csv(rootDataDir + dataFilesDir + "Events_RecordAccess_001.csv")
    invitees_details = pd.read_csv(rootDataDir + dataFilesDir + "Invitees_001.csv")
    layout_details = pd.read_csv(rootDataDir + dataFilesDir + "Layout_001.csv")
    potential_record_access_details = pd.read_csv(rootDataDir + dataFilesDir + "Potentials_RecordAccess_001.csv")
    sticky_notes_details = pd.read_csv(rootDataDir + dataFilesDir + "StickyNotes_001.csv")
    tags_details = pd.read_csv(rootDataDir + dataFilesDir + "Tags_001.csv")
    tasks_record_access_details = pd.read_csv(rootDataDir + dataFilesDir + "Tasks_RecordAccess_001.csv")
    translation_language_details = pd.read_csv(rootDataDir + dataFilesDir + "Translation_Language_001.csv")
    competitors_details = pd.read_csv(rootDataDir + dataFilesDir + "Competitors_001.csv")
    pot_stage_history_details = pd.read_csv(rootDataDir + dataFilesDir + "PotStageHistory_001.csv")
    deal_contact_role_details = pd.read_csv(rootDataDir + dataFilesDir + "DealContactRole_001.csv")
    translation_codes_details = pd.read_csv(rootDataDir + dataFilesDir + "Translation_Codes_001.csv")

    # 1. findAllAccounts

    accountname_tofilter = df_excelWithAccount['Account Name'].tolist()
    account_details_filtered = account_details[account_details['Account Name'].isin(accountname_tofilter)]
    account_details_filtered.to_csv('Output/account_details_filtered.csv', index=False)

    # Filtered Account ID
    account_list = account_details_filtered['Account ID'].tolist()

    # 2. findAllContactsForAccount
    contact_details_filtered = contact_details[contact_details['Account ID'].isin(account_list)]
    contact_details_filtered.to_csv('Output/contact_details_filtered.csv', index=False)

    # 3. findAllleadsForAccount
    leads_details_filtered = lead_details[lead_details['Account ID'].isin(account_list)]
    leads_details_filtered.to_csv(
        'Output/Leads_details_filtered.csv', index=False)

    # 4. findAllPotentialsForAccount
    potential_details_filtered = potential_details[potential_details['Account ID'].isin(account_list)]
    potential_details_filtered.to_csv(
        'Output/potential_details_filtered.csv', index=False)

    # Filtered Potential ID
    potential_list = potential_details_filtered['Potential ID'].tolist()

    # 5. findAllVisitesForAccount
    visits_details_filtered = visits_details[visits_details['Account ID'].isin(account_list)]
    visits_details_filtered.to_csv(
        'Output/visits_details_filtered.csv', index=False)

    # 6. findAllUsersForAccount
    users_tofilter = account_details_filtered['Account Owner ID'].tolist()
    users_details_filtered = user_details[user_details['Added By Id'].isin(users_tofilter)]
    users_details_filtered.to_csv(
        'Output/users_details_filtered.csv', index=False)

    # Filtered User ID
    user_list = users_details_filtered['User ID'].tolist()

    # 7. findAllNotesForAccount
    notes_details_filtered = notes_details[notes_details['Note Owner ID'].isin(user_list)]
    notes_details_filtered.to_csv(
        'Output/notes_details_filtered.csv', index=False)

    # 8. findAttachmentsForAccount
    attachments_details_filtered = attachments_details[attachments_details['Attachment Owner ID'].isin(user_list)]
    attachments_details_filtered.to_csv(
        'Output/attachments_details_filtered.csv', index=False)

    # 9. findAllCallsForAccount
    calls_details_filtered = call_details[call_details['Call Owner Id'].isin(user_list)]
    calls_details_filtered.to_csv(
        'Output/calls_details_filtered.csv', index=False)

    # 10. findAllEmailsForAccount
    emails_details_filtered = email_details[email_details['Email Owner Id'].isin(user_list)]
    emails_details_filtered.to_csv(
        'Output/emails_details_filtered.csv', index=False)

    # 11. findAllEventsForAccount
    events_details_filtered = event_details[event_details['Event Owner ID'].isin(user_list)]
    events_details_filtered.to_csv(
        'Output/events_details_filtered.csv', index=False)

    # 12. findAllForecastsForAccount
    forecast_details_filtered = forecast_details[forecast_details['Forecast Owner ID'].isin(user_list)]
    forecast_details_filtered.to_csv(
        'Output/forecast_details_filtered.csv', index=False)

    # 13. findAllTasksForAccount
    tasks_details_filtered = tasks_details[tasks_details['Task Owner ID'].isin(user_list)]
    tasks_details_filtered.to_csv(
        'Output/tasks_details_filtered.csv', index=False)

    # 14. findAllSolutionsForAccount
    solutions_details_filtered = solutions_details[solutions_details['Solution Owner ID'].isin(user_list)]
    solutions_details_filtered.to_csv(
        'Output/solutions_details_filtered.csv', index=False)

    # 15. findAllPotentialProjectsForAccount
    potentialProject_details_filtered = potentialProject_details[
        potentialProject_details['Potential Projects Owner ID'].isin(user_list)]
    potentialProject_details_filtered.to_csv(
        'Output/potentialProject_details_filtered.csv', index=False)

    # 16. findAllPotentialCopyCForAccount
    potentialCopyC_details_filtered = potentialCopyC_details[
        potentialCopyC_details['Potential Copy Owner ID'].isin(user_list)]
    potentialCopyC_details_filtered.to_csv(
        'Output/potentialCopyC_details_filtered.csv', index=False)

    # 17. findAllAccountRecordAccessForAccount
    accounts_record_access_details_filtered = accounts_record_access_details[
        accounts_record_access_details['Shared By Id'].isin(user_list)]
    accounts_record_access_details_filtered.to_csv(
        'Output/accounts_record_access_details_filtered.csv', index=False)

    # 18. findAllCallRecordAccessForAccount
    calls_record_access_details_filtered = calls_record_access_details[
        calls_record_access_details['Shared By Id'].isin(user_list)]
    calls_record_access_details_filtered.to_csv(
        'Output/calls_record_access_details_filtered.csv', index=False)

    # 19. findAllContactsRecordAccessForAccount
    contacts_record_access_details_filtered = contacts_record_access_details[
        contacts_record_access_details['Shared By Id'].isin(user_list)]
    contacts_record_access_details_filtered.to_csv(
        'Output/contacts_record_access_details_filtered.csv', index=False)

    # 20. findAllEventsRecordAccessForAccount
    events_record_access_details_filtered = events_record_access_details[
        events_record_access_details['Shared By Id'].isin(user_list)]
    events_record_access_details_filtered.to_csv(
        'Output/events_record_access_details_filtered.csv', index=False)

    # 21. findAllInviteesForAccount
    invitees_details_filtered = invitees_details[invitees_details['User ID'].isin(user_list)]
    invitees_details_filtered.to_csv('Output/invitees_details_filtered.csv', index=False)

    # 22. findAllLayoutForAccount
    layout_details_filtered = layout_details[
        layout_details['Created by ID'].isin(user_list)]
    layout_details_filtered.to_csv(
        'Output/layout_details_filtered.csv', index=False)

    # 23. findPotentialRecordAccessForAccount
    potential_record_access_details_filtered = potential_record_access_details[
        potential_record_access_details['Shared By Id'].isin(user_list)]
    potential_record_access_details_filtered.to_csv(
        'Output/potential_record_access_details_filtered.csv', index=False)

    # 24. findAllStickyNotesForAccount
    sticky_notes_details_filtered = sticky_notes_details[
        sticky_notes_details['Created by ID'].isin(user_list)]
    sticky_notes_details_filtered.to_csv(
        'Output/sticky_notes_details_filtered.csv', index=False)

    # 25. findAllTagsForAccount
    tags_details_filtered = tags_details[
        tags_details['Created by ID'].isin(user_list)]
    tags_details_filtered.to_csv('Output/tags_details_filtered.csv', index=False)

    # 26. findAllTasksForAccount
    tasks_record_access_details_filtered = tasks_record_access_details[
        tasks_record_access_details['Shared By Id'].isin(user_list)]
    tasks_record_access_details_filtered.to_csv('Output/tasks_record_access_details_filtered.csv', index=False)

    # 27. findAllTranslationLanguageForAccount
    translation_language_details_filtered = translation_language_details[
        translation_language_details['Imported By Id'].isin(user_list)]
    translation_language_details_filtered.to_csv('Output/translation_language_details_filtered.csv', index=False)

    # 28. findAllCompetitorsForAccount
    competitors_details_filtered = competitors_details[
        competitors_details['Potential ID'].isin(potential_list)]
    competitors_details_filtered.to_csv(
        'Output/competitors_details_filtered.csv', index=False)

    # 29. findAllPotStageHistoryForAccount
    pot_stage_history_details_filtered = pot_stage_history_details[
        pot_stage_history_details['Potential ID'].isin(potential_list)]
    pot_stage_history_details_filtered.to_csv('Output/pot_stage_history_details_filtered.csv', index=False)

    # 30. findAllDealContactRoleForAccount
    deal_contact_role_details_filtered = deal_contact_role_details[
        deal_contact_role_details['Contact ID'].isin(contact_details_filtered['Contact ID'].tolist())]
    deal_contact_role_details_filtered.to_csv('Output/deal_contact_role_details_filtered.csv', index=False)

    # 31. findAllTranslationCodeForAccount
    translation_codes_details_filtered = translation_codes_details[
        translation_codes_details['Language Code Id'].isin(
            translation_language_details_filtered['Language Code Id'].tolist())]
    translation_codes_details_filtered.to_csv('Output/translation_codes_details_filtered.csv', index=False)
