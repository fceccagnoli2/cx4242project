DESCRIPTION
- This package allows users to get a valuation of their NFTs. Current supported NFT projects include: Bored Ape Yacht
Club, Cool Cats NFT, Pudgy Penguins, Lazy Lions, Dead Fellaz, Robots Official, and World of Women NFT. Users need to
input 4 fields to get their valuation: nft project, token id, current date, and current price of Ethereum in
USD. The Ethereum price in USD can be found online (ex google search: ethereum to usd). When the inputs are entered, a
linear regression model predicts the valuation of the NFT and this valuation is displayed in large text on the screen.
Under the valuation, an image of that specific NFT is displayed. Under the image, an interactive plot of past
transactions for that NFT is displayed. The current valuation is also displayed on the same plot as a forecasted data
point.

INSTALLATION
- make sure to have pip, anaconda, and git installed.

-  Download required files by using the command below. This will donwload the folder cx4242project. This folder
 holds: model.py, visualizations.py, analysis.py, data_cleaning.py, requirements.txt, and README.md. 
 data_cleaning.py was used to clean our data. analysis.py was used for the analysis of our data. requirements.txt 
 describes the requirements needed to run the program. visualizations.py and model.py are the 2 files actually neeed 
 for our visualizations. 

git clone git@github.com:fceccagnoli2/cx4242project.git

- move into the project directory

cd cx4242project

- Create the environment by using:

conda create --name cx4242project

conda activate cx4242project

pip3 install -r requirements.txt                        

- Run the program by using:

streamlit run visualizations.py

EXECUTION
- Begin by entering the four required fields: nft project, token id, current date, and current price of
Ethereum in USD. If any of the fields are left blank, the user will be asked to make sure all the fields are entered.
If incorrect data types are entered (for example: entering letters for the token id or price of ETH), an error message
will appear and the user will be asked to re-enter the information. When the information is entered, click 'Predict'.
If there are no transactions of this NFT in our database, we are unable to value the NFT and the user will be asked to
try a different NFT. Otherwise, the program will continue successfully.

There are a few ways to interact with the graph that is displayed. First, users can hover over data points
to see the date and specific price of the transaction. Users can also zoom in on any area of the chart by clicking on
the chart and making a box over the area they would like to zoom in on. To zoom back out, double click on the chart.
Users can also zoom in and out by clicking the zoom in and zoom out buttons above the cart. Users can navigate around
the chart by clicking the 'pan' button above the chart and dragging to where they want to navigate. Users can also
download the plot by clicking 'Download plot as a png' above the chart.

To see the valuation of a different NFT, simply fill in the form again and click submit. The new information will
appear.