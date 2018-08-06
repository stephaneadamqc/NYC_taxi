from sklearn.linear_model import LinearRegression
from sklearn.model_selection import ShuffleSplit, cross_validate
from sklearn.metrics import mean_squared_error, make_scorer
import pandas as pd
from x_commun.NYT_Paths import *

'''
Documentation
'''
if __name__ == '__main__':
    from Models_data_prep.NYTaxi_cross_ref_data_split_train_test import X_train, Y_train
    mse = make_scorer(mean_squared_error, greater_is_better=False)
    seed = 42
    n_split = 10

    dirname = 'linear_regression'
    reportname = 'RMSE_scores_{}.csv'.format(datetime)

    try:
        os.mkdir(os.path.join(Path_Reports, dirname))
    except Exception as e:
        pass

    cv = ShuffleSplit(n_splits=n_split, test_size=0.2, random_state=seed)
    model = LinearRegression()
    scores = cross_validate(model, X_train.reshape(-1, 1), Y_train, scoring=mse, cv=cv, verbose=1, return_train_score=True)

    df = pd.DataFrame.from_dict(scores)
    # df.test_mean_squared_error = np.sqrt(df.test_score)
    # df.train_mean_squared_error = np.sqrt(df.train_score)
    df.to_csv(os.path.join(Path_Reports, dirname, reportname))
