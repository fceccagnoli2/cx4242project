import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


#Features to us in regression
features = [
'last_sale_price',
"rarity",
'date_delta',
"rarityPercentile",
"rarityRank",
"price_of_eth",
'project_boredapeyachtclub',
'project_cool-cats-nft',
'project_creatureworld',
'project_deadfellaz',
'project_lazy-lions',
'project_pudgypenguins',
'project_robotos-official',
'project_world-of-women-nft']


class Data():
    def __init__(self):
        self.x_data = None
        self.y_data = None
        self.x_train = None
        self.y_train = None
        self.x_test = None
        self.y_test = None

    def dataAllocation(self,path):
        #Separate out the x_data and y_data and return each
        all_data = pd.read_csv(path)[features+["listing_usd_price"]]
        clean_data = all_data.dropna()
        x_data = clean_data[features]
        y_data = clean_data["listing_usd_price"]
        # -------------------------------

        self.x_data = x_data
        self.y_data = y_data

    def trainSets(self):
        # Split data into train and test sets
        # return: pandas dataframe, pandas dataframe, pandas series, pandas series
        x_train, x_test, y_train, y_test = train_test_split(self.x_data,self.y_data, test_size=0.25, train_size=None, random_state=614, shuffle=True, stratify=None)
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test



class Regression():

    def linearRegression(self,x_train,x_test, y_train):
        #creates a linear regression object
        regressor = LinearRegression(fit_intercept=True, positive=False)
        regressor.fit(x_train, y_train)
        y_predict_train = regressor.predict(x_train)
        y_predict_test = regressor.predict(x_test)
        return regressor, y_predict_train, y_predict_test


class model_suite():
    def __init__(self):
        self.models = {}

    def builder(self, x_train, x_test, y_train):
        # -------------------------------
        linear_model = Regression()
        regressor, y_predict_train, y_predict_test = linear_model.linearRegression(x_train = x_train, x_test = x_test, y_train = y_train)
        return regressor

    def project_seperator_and_builder(self, x_train, x_test, y_train, y_test):
        #Creates a model for each the NFT project below and stores the models in self.models
        projects = [
            'project_boredapeyachtclub',
            'project_cool-cats-nft',
            # 'project_creatureworld',
            'project_deadfellaz',
            'project_lazy-lions',
            'project_pudgypenguins',
            'project_robotos-official',
            'project_world-of-women-nft'
        ]
        for project in projects:
            sep_x_train = x_train[x_train[project]==1]
            sep_y_train = y_train[sep_x_train.index]
            sep_x_test = x_test[x_test[project]==1]
            sep_y_test = y_test[sep_x_test.index]
            self.models[project] = self.builder(sep_x_train, sep_x_test, sep_y_train)


