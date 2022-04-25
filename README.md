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
- If you don't have them already, download python, anaconda, homebrew, and git. They can be installed on their websites. 
If you have not used github before, you will need to create an account and get a public key. Instructions for getting a 
public key can be found at:
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

- install lfs, a large file storage service from github. This allows you to pull our large dataset from github. Use the 
command below in command line

brew install git-lfs

-  Download required files by using the command below. This will download the folder cx4242project. This folder
 holds: model.py, visualizations.py, analysis.ipynb, data_cleaning.ipynb, requirements.txt, README.md, and a data
 folder which holds clean_data_large.csv. data_cleaning.py was used to clean our data. analysis.py was used for 
 the analysis of our data. requirements.txt describes the requirements needed to run the program. visualizations.py and 
 model.py are the 2 files actually needed for our visualizations. 

git clone git@github.com:fceccagnoli2/cx4242project.git

- move into the project directory

cd cx4242project

- Create the environment by using:

conda create --name cx4242project

conda activate cx4242project

pip3 install -r requirements.txt                        

- Run the program by using:

streamlit run visualizations.py

- If for some reason any of the above steps fail, you can donwload all of the required files to run the app from the 
github page. Click code -> download zip. The requirements to run the file are in requirements.txt. 
https://github.com/fceccagnoli2/cx4242project

EXECUTION
- Begin by entering the four required fields: nft project, token id, current date, and current price of
Ethereum in USD. If any of the fields are left blank, the user will be asked to make sure all the fields are entered.
If incorrect data types are entered (for example: entering letters for the token id or price of ETH), an error message
will appear and the user will be asked to re-enter the information. When the information is entered, click 'Predict'.
If there are no transactions of this NFT in our database, we are unable to value the NFT and the user will be asked to
try a different NFT. Otherwise, the program will continue successfully.

- There are a few ways to interact with the graph that is displayed. First, users can hover over data points
to see the date and specific price of the transaction. Users can also zoom in on any area of the chart by clicking on
the chart and making a box over the area they would like to zoom in on. To zoom back out, double click on the chart.
Users can also zoom in and out by clicking the zoom in and zoom out buttons above the cart. Users can navigate around
the chart by clicking the 'pan' button above the chart and dragging to where they want to navigate. Users can also
download the plot by clicking 'Download plot as a png' above the chart.

- To see the valuation of a different NFT, simply fill in the form again and click submit. The new information will
appear.