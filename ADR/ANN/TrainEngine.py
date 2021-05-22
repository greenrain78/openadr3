# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.externals import joblib
#
#
# def train():
#     # load data
#     dataset = pd.read_csv('ANN/api_sample_data_0307.csv', encoding='utf-8')  # 20210307 데이터
#     test_dataset = pd.read_csv('ANN/api_sample_data_0308.csv', encoding='utf-8')  # 20210307 데이터
#     score_dataset = pd.read_csv('ANN/api_sample_data_0308.csv', encoding='utf-8')  # 20210307 데이터
#
#     x_dataset = dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
#                          'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
#     y_dataset = dataset[['atvPower']]
#
#     x_test_dataset = test_dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
#                                    'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
#     y_test_dataset = test_dataset[['atvPower']]
#
#     x_score_dataset = score_dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
#                                      'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
#     y_score_dataset = score_dataset[['atvPower']]
#
#     # 훈련
#     model = LinearRegression()
#     model.fit(x_dataset, y_dataset)
#
#     # 예측
#     y_predict = model.predict(x_test_dataset)
#
#     print("학습")
#     print(model.coef_)
#     print(model.score(x_score_dataset, y_score_dataset))
#     joblib(model, 'model_save1.pkl')
#
#
# def predict():
#     model = joblib.load('model_save1.pkl')
#
#     score_dataset = pd.read_csv('ANN/api_sample_data_0308.csv', encoding='utf-8')  # 20210307 데이터
#     x_score_dataset = score_dataset[['ymdms', 'volTage', 'amPere', 'arPower', 'ratPower',
#                                      'pwFactor', 'accruePower', 'voltagerS', 'voltagesT', 'voltagetR', 'temperature']]
#     y_score_dataset = score_dataset[['atvPower']]
#     print("예측")
#     print(model.coef_)
#     print(model.score(x_score_dataset, y_score_dataset))
#
#
# """
# 다중 선형회귀 모델 작성
# 스코어가 1?
# 예측률 100% ?
# """
