import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
from PIL import Image
import requests
import pandas as pd
import numpy as np
from model import Data, model_suite


@st.cache(allow_output_mutation=True)
def loadData():
    #loads the data
    data = pd.read_csv('data/clean_data_large.csv')
    return data
data= loadData()

@st.cache(allow_output_mutation=True)
def trainModel():
    #Creates linear regression models for each NFT project
    data = Data()
    data.dataAllocation('data/clean_data_large.csv')
    data.trainSets()
    models = model_suite()
    models.project_seperator_and_builder(data.x_train, data.x_test, data.y_train, data.y_test)
    return models
models = trainModel()
#models is a dictionary of {project:linear regression model}


#Add title
st.title("NFT Price Valuation Tool", anchor=None)
st.write('By: Federico Ceccagnoli, Whit Blass, Jarod Thornton, Gidon Kowalsky, and Isaac Zelcer')


#Get input from user to use in regression model
with st.form('inputs', clear_on_submit=True):
    st.write("Hello! Welcome to our NFT price valuation app. We use a a Linear Regression model to value your NFTs. Get started by entering the information below.")
    options = np.array(['', 'boredapeyachtclub', 'cool-cats-nft', 'pudgypenguins', 'lazy-lions', 'deadfellaz', 'robotos-official', 'world-of-women-nft'])
    project = st.selectbox("Select the NFT Project.", options)
    tokenId = st.text_input("Enter the token Id. (Ex: 89)")
    date = st.text_input("Enter today's date. (Ex: 04-21-2022)")
    priceOfEth = st.text_input("Enter the current price of Ethereum in USD (Ex: 3000)")
    submitted = st.form_submit_button("Predict")

if submitted:
# When the submit buttin is clicked, the image and graoh is displayed

    if tokenId == '' or date == '' or priceOfEth == '' or project == '':
        # If any field is left blank, tell the user to fill it in
        st.write('Please enter all the fields')
    else:
        #If all the fields are filled in, pull up past transactions for the specified NFT projct, NFT token
        data["tokenId"] = data['tokenId'].astype('string')
        transactions = data[data['project_'+ project] == 1]
        transactions = transactions[transactions['tokenId'] == tokenId].sort_values(by="createdAt")
        transactions['createdAt'] = pd.to_datetime(transactions['createdAt'])
        transactions['createdAt'] = transactions['createdAt'].dt.strftime("%m/%d/%Y, %H:%M:%S")

        if len(transactions) == 0:
            #If there are no transactions in our database, tell the user a valuation ould not be made
            st.write("You either entered an invalid NFT or we cannot value this NFT because we do not have any transactions of this NFT in our database.")

        else:
            #Get the regression model fir the specified NFT project
            regressor = models.models['project_' + project]
            #create list "a" to tell the regression model which project is being passed in
            if project == 'boredapeyachtclub':
                a = [1, 0, 0, 0, 0, 0, 0, 0]
            elif project == 'cool-cats-nft':
                a = [0, 1, 0, 0, 0, 0, 0, 0]
            elif project == 'deadfellaz':
                a = [0, 0, 0, 1, 0, 0, 0, 0]
            elif project == 'lazy-lions':
                a = [0, 0, 0, 0, 1, 0, 0, 0]
            elif project == 'pudgypenguins':
                a = [0, 0, 0, 0, 0, 1, 0, 0]
            elif project == 'robotos-official':
                a = [0, 0, 0, 0, 0, 0, 1, 0]
            elif project == 'world-of-women-nft':
                a = [0, 0, 0, 0, 0, 0, 0, 1]

            #create an image object from the image url
            url = transactions['image_url_BIG'].iloc[0]
            im = Image.open(requests.get(url, stream=True).raw)

            #Format the data to make the interactive chart
            chartData = transactions[["createdAt", "listing_usd_price"]]
            chartData = chartData.rename(columns={chartData.columns[0]: 'Date', chartData.columns[1]: 'Price'})
            chartData['Date'] = chartData['Date'].astype('string')

            #Get the features to pass into the regression model
            lastSalePrice = transactions['listing_usd_price'].iloc[len(transactions['listing_usd_price']) - 1]
            rarity = transactions['rarity'].iloc[0]
            rarityPercentile = transactions['rarityPercentile'].iloc[0]
            rarityRank = transactions['rarityRank'].iloc[0]
            transactions['createdAt'] = pd.to_datetime(transactions['createdAt'])
            transactions['date_delta'] = (transactions['createdAt'] - transactions['createdAt'].min())  / np.timedelta64(1,'D')
            firstTransactionDate = pd.to_datetime(pd.to_datetime(transactions['createdAt'].iloc[0]).strftime("%d/%m/%Y"))
            today = pd.to_datetime(pd.to_datetime(date).strftime("%d/%m/%Y"))
            dateDelta = (today - firstTransactionDate)  / np.timedelta64(1,'D')

            x = [[lastSalePrice, rarity, dateDelta, rarityPercentile, rarityRank, int(priceOfEth)] + a]
            #pass in array x into the regression model to get the predicion.
            y = regressor.predict(x)[0]

            #plot
            lastTransactionDate = transactions['createdAt'].iloc[-1].strftime("%m/%d/%Y, %H:%M:%S")
            lastTransactionPrice = transactions['listing_usd_price'].iloc[-1]
            plot = px.line(chartData, x="Date", y="Price", markers=True, title='Past transactions for ' + project + ' #' + tokenId + '.')
            plot.add_traces(go.Scatter(x=[lastTransactionDate, 'Predicted'], y=[lastTransactionPrice, y], showlegend=False))
            plot.add_traces(go.Scatter(x=chartData["Date"], y=chartData["Price"], showlegend=False))
            plot.update_traces(hovertemplate='Date: %{x} <br>Price: $%{y}')

            st.header("Your NFT is valued at " + "${:,.2f}".format(y) + " USD")
            st.image(im)
            st.plotly_chart(plot)