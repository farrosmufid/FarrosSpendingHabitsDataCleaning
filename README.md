# Farros Spending Habits Data Cleaning

This project involves cleaning and organising transaction data to understand better spending habits for the [Farros Spending Habits Dashboard](https://public.tableau.com/app/profile/farros.mufid/viz/FarrosSpendingHabits/SpendingHabitsDashboard).

- **Data Source**: The data comes from Commonwealth Bank's Transactions Smart Access Transactions (Farros' bank account), covering periods from 1 January - 30 June 2024 (`CSVData.csv` - First Account Statement) and from 1 July - 12 September 2024 (`CSVData2.csv` - Second Account Statement).
- **Data Processing**: Both datasets were concatenated, and new fields for categories and subcategories were created based on the descriptions in the transactions.
- **Output File**: The cleaned and processed data is saved in `transactions2024.csv`.
