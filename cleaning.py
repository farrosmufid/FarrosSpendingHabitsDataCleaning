import numpy as np
import pandas as pd

column_names = ['Date', 'Amount', 'Description', 'Balance']

# 01 Jan 2024 - 30 Jun 2024
df1 = pd.read_csv('CSVData.csv', header = None, names = column_names)

# 01 July 2024 - 12 Sep 2024
df2 = pd.read_csv('CSVData2.csv', header = None, names = column_names)

# Concat both datasets
df = pd.concat([df1, df2], ignore_index = True)

def categorise_description(description):
    """
    This function categorises a given description string into predefined subcategories
    based on keywords found in the description

    Parameters:
    ----------
    description: str
        A string representing the description of a transaction or item. The 
        function converts the description into lowercase to ensure case-insensitive
        matching of the keywords.
    
    Returns:
    -------
    str
        A string represnting the subcategory that corresponds to the keywords found in the description.
        If no matching keyword is found, it returns the string 'Other'

    """
    description = description.lower()

    if 'provender' in description:
        return 'Vending Machine'
    elif any(keyword in description for keyword in [
        'fruitezy', 'woolworths', 'ezymart', 'parra', 'tsg central', 'tsg dixon'
    ]):
        return 'Grocery'
    elif any(keyword in description for keyword in [
        'sudata', 'sydney royal east', 'ticketmasterau', 'easter show sendrat',
        'kellys on king', 'party @ manning','teenage fan club', 'transfer to praddeep',
        'sydney olympi', 'ticketek', 'sumarto', 'katoomba', 'the lookout', 'transfer to agnes lin',
        'taronga zoo mosman', 'westshell pty ltd sydney'
    ]):
        return 'Events'
    elif 'carriageworks' in description:
        return 'Stationery'
    elif 'chemist warehouse' in description or 'pline ph central' in description or 'burwood pharmacy' in description:
        return 'Pharmacy'
    elif any(keyword in description for keyword in [
            'surfish', 'pie cafe', 'sushi', 'sweet town',
            'enjoy mie', 'fish market', 'nandos', 'ho jiak',
            'chicken v seoul', 'pancakes on the rocks', 'fat fish',
            'haymarket seafood', 'yunnn', 'gourmet', 'mcdonalds',
            'roll\'d westfield', 'pepper lunch', 'peko peko', 'kebab', 
            'antico woodfired', 'spago', 'brazilian flame', 
            'pmc golden tower', 'nene chicken', 'umma kitchen', 
            'mom recipes', 'quality burger', 'ozeki bowl',
            'hungry jacks', 'malatang', 'asian cuisine', 'adanos', 
            'yb corporate', 'oiden', 'spicy hotp', 'kfc', 'shalom',
            'time for thai', 'andiamo', 'rice bowl', 'ff darling harbour', 
            'ed ae unique thai', 'hurricanes grill', 'jordans seafood',
            'noddles', 'noodles your way', 'rio recipe', 'mappen 10',
            'holy basil', 'golden tower', 'cellini\'s sydney', 'sixprogression',
            'concrete jungle', 'the sambal', 'carmel dyer', 'talays thai', 
            'im angus', 'carvery catering', 'ramen', 'ong thai', 'tb_haymarket_3114',
            'crocodile junior', 'ls baia', 'pirhana fish', 'leclover', 'grilld pty',
            'little indo town', 'qonus* hiw so chatswood', 'redfern fish and chips',
            'geprek in sydney', 'restaurant and b', 'racha thani pty', 'ls slaps',
            'bowls & burger', 'slar group pty', 'sunflower taiwanese ultimo', 
            'exquisite dining pl', 'broad wave pty ltd', 'chicken factory pty ']):
        return 'Restaurants'
    elif any(keyword in description for keyword in [
        'medibank', 'international transaction fee', 'uni of sydney',
        'testing exam', 'university of sydney', 'sydney university', 'alliance opco pty'
    ]):
        return 'Student Fees'
    elif any(keyword in description for keyword in [
            'a medium', 'symbolab.com', 'openai', 'scrimba', 'language academy', 
            'adobe systems','linkedin', 'crunchyroll', 'grammarly', 'google storage mountain',
            'spotify', 'canva', 'adobe', 'chatgpt', 'aust federal', 'google one mountain'
            ]):
        return 'Online Subscriptions'
    elif any(keyword in description for keyword in [
        'ref', 'fast transfer', 'return 11/04/24 direct debit'
    ]):
        return 'Credit'
    elif 'apple' in description:
        return 'Apple'
    elif 'starbucks' in description:
        return 'Coffee'
    elif 'icc' in description or 'timezone' in description or 'palace cinemas' in description:
        return 'Entertainment'
    elif 'kinokuniya' in description or 'dymocks' in description or 'qbd the bookshop broadway' in description:
        return 'Book'
    elif 'iglu' in description or 'kensington investment chippendale au' in description:
        return 'Rent'
    elif any(keyword in description for keyword in [
        'transportfornsw', 'didichuxing', 'uber', 'didimobility sydney'
    ]):
        return 'Transport'
    elif any(keyword in description for keyword in [
        'between the flags', 'australian collection sydney', 'xin mei fashion',
        'red eye records', 'cotton on market', 'authentics factory', 'jb hi fi'
    ]):
        return 'Shopping'
    elif 'vodafone' in description:
        return 'Mobile Services'
    elif any(keyword in description for keyword in [
        'dessert dealer', 'andersens', 'tsg broadway', 'macchiato sydney', 'chatime',
        'gelato', 'sharetea', 've-sweet', 'andersen\'s of denmar', 'max brenner',
        'ice cream','royal copenhagen cir', 'tsg quay', 'tobacco station', 
        'off broadway hotel ultimo', 'your dessert stati', 'yomie\'s rice x yogurt',
        'krispy kreme central 2 '
    ]):
        return 'Food and Beverage'
    elif any(keyword in description for keyword in [
        'debit', 'overdraw', 'unpaid payment'
    ]):
        return 'Debit'
    elif 'cash deposit' in description:
        return 'Cash Deposit'
    elif 'salons' in description:
        return 'Salon'
    else:
        return 'Other'

df['Subcategory'] = df['Description'].apply(categorise_description)

# Maps a subcategory to a category
subcategory_to_category = {
    'Restaurants': 'Food',
    'Coffee': 'Food',
    'Vending Machine': 'Food',
    'Food and Beverage': 'Food',
    'Grocery': 'Food',
    'Rent': 'Living Expenses',
    'Transport': 'Living Expenses',
    'Online Subscriptions': 'Technology and Services',
    'Apple': 'Technology and Services',
    'Mobile Services': 'Technology and Services',
    'Student Fees': 'Education',
    'Book': 'Education',
    'Stationery': 'Education',
    'Events': 'Activities',
    'Entertainment': 'Activities',
    'Credit': 'Financial Transactions',
    'Debit': 'Financial Transactions',
    'Cash Deposit': 'Financial Transactions',
    'Shopping': 'Financial Transactions',
    'Pharmacy': 'Personal Care',
    'Salon': 'Personal Care'
}

df['Category'] = df['Subcategory'].map(subcategory_to_category)

# Convert to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

df.to_csv('transactions2024.csv', index = False)



