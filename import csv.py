import pandas as pd

def getLinesOnlyInA(dfa, dfb, result):
    # iterate over all lines in file a
    for index1, row1 in dfa.iterrows():
        aLineIsEqual = False
        # iterate over all lines in file b
        for index2, row2 in dfb.iterrows():
            thisLineIsDifferent = False
            # for each column, check if they are different
            for column in columns:
                if row1[column] != row2[column]:
                    thisLineIsDifferent = True
                    # ionly continue when the fields are the same
                    break
            if not thisLineIsDifferent:
                aLineIsEqual = True
                # only continue when no equal line was found
                break
        # when no equal line was found, add that line to the result
        if not aLineIsEqual:
            result.append(row1)
            
            
df1 = pd.read_csv('C:/Users/iraku/Desktop/Книга1.csv', encoding="cp1251", delimiter=";")
df2 = pd.read_csv('C:/Users/iraku/Desktop/Книга2.csv', encoding="cp1251", delimiter=";")
columns = ['contract_no', 'contract_code', 'autocall_guide', 'fixing_date', 'payment_date', 'action_text', 'coupon_payoff_volume', 'payment_ccy', 'recall_payoff_volume', 'exercise_delivery_volume', 'asset_isin']     # columns to be compared
results = []

getLinesOnlyInA(df1, df2, results)        # find all lines only existing in file 1
getLinesOnlyInA(df2, df1, results)        # find all lines only existing in file 2
dfResult = pd.DataFrame(results)          # cast all lines into a dataframe

print(dfResult.to_string())   
dfResult.to_csv('C:/Users/iraku/Desktop/output.csv', encoding="cp1251")