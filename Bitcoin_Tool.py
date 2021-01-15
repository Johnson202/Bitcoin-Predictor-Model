from scipy.special import inv_boxcox
#simple algorithm to combine all of available tools!



def BTC_assist_tool(df, best_model, lmda):
    #df = df_btc_CCC_dummies from this .ipynb
    #best_model = log_likelihood_model
    
    #assess VWAP vs. Close Price
    if df['10_Day_VWAP'][len(df)-1] > df['Close'][len(df)-1]:
        if df['10_Day_VWAP'][len(df)-2] < df['Close'][len(df)-2]:
            print('10-day VWAP is above Close Price and crossing above Close Price (SELL).')
        else:
            print('10-day VWAP is above Close Price (SELL).')
    
    elif df['10_Day_VWAP'][len(df)-1] < df['Close'][len(df)-1]:
        if df['10_Day_VWAP'][len(df)-2] > df['Close'][len(df)-2]:
            print('10-day VWAP is below Close Price and crossing below Close Price (BUY).')
        else:
            print('10-day VWAP is below Close Price (BUY).')
    
    #assess MACD vs. Signal
    if df['MACD'][len(df)-1] > df['Signal'][len(df)-1]:
        if df['MACD'][len(df)-2] < df['Signal'][len(df)-2]:
            print('MACD is above Signal and crossing above Signal (BUY).')
        else:
            print('MACD is above Signal (BUY).')
    elif df['MACD'][len(df)-1] < df['Signal'][len(df)-1]:
        if df['MACD'][len(df)-2] > df['Signal'][len(df)-2]:
            print('MACD is below Signal and crossing below Signal (SELL).')
        else:
            print('MACD is below Signal (SELL).')
            
    #assess RSI
    if df['Biweekly_RSI'][len(df)-1] >= 70:
        print('RSI is above 70 (SELL).')
    elif df['Biweekly_RSI'][len(df)-1] <= 30:
        print('RSI is below 30 (BUY).')
    
    #today's prediction vs. yesterday's price
    pred_transf = best_model.predict(len(df)).values[0]
    pred_untransf = inv_boxcox(pred_transf, lmda)
    yesterday = df['Close'][len(df)-1]
    
    print(f'Today\'s predicted BTC-USD Close Price is ${pred_untransf:.2f}. Yesterday\'s BTC-USD Close Price was ${yesterday:.2f}.')

if __name__ == '__main__':
    pass
