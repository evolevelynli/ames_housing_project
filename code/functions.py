import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def remove_outlier(data, variable, upper, lower):
    lower_bool = data[variable] > lower
    upper_bool = data[variable] < upper
    data = data[lower_bool & upper_bool]

    return data


def ext_cat_features(data):
    return data.select_dtypes(exclude=[float,int]).columns

#extract Numerical features
def ext_num_features(data):
    return data.select_dtypes(include=[float,int]).columns


#fill Na function
def fill_na(data):
    cat_df = data[ext_cat_features(data)]
    cat_df_name = cat_df.columns

    numeric_df = data[ext_num_features(data)]
    numeric_df_name = numeric_df.columns

    for name in numeric_df_name:
        fill_value_num = numeric_df[name].mean()
        numeric_df[name] = numeric_df[name].fillna(fill_value_num)

    for name in cat_df_name:
        fill_value_cat = f"No_{name}"
        cat_df[name] = cat_df[name].fillna(fill_value_cat)

    return cat_df.join(numeric_df)


#change street to dummy
def convert_to_dummy(data):
    cat_col = data.select_dtypes(exclude=[float,int]).columns

    data = pd.get_dummies(data, columns = cat_col)

    return data





def rail_or_road(data):
    rail_1 = np.where(data["Condition 1"]. isin(["RRNn", "RRAn", "RRNe", "RRAe"]), 1, 0)
    rail_2 = np.where(data["Condition 2"]. isin(["RRNn", "RRAn", "RRNe", "RRAe"]), 1, 0)
    data['close_to_rail'] = rail_1 + rail_2

    norm_1 = np.where(data["Condition 1"]. isin(["Norm"]), 1, 0)
    norm_2 = np.where(data["Condition 2"]. isin(["Norm"]), 1, 0)
    data['normal'] = norm_1 + norm_2

    off_site_1 = np.where(data["Condition 1"]. isin(["PosN", "PosA"]), 1, 0)
    off_site_2 = np.where(data["Condition 2"]. isin(["PosN", "PosA"]), 1, 0)
    data['off_site'] = off_site_1 + off_site_2

    street_1 = np.where(data["Condition 1"]. isin(["Artery", "Feedr"]), 1, 0)
    street_2 = np.where(data["Condition 2"]. isin(["Artery", "Feedr"]), 1, 0)
    data['street'] = street_1 + street_2

    data = data.drop(['Condition 1','Condition 2'],axis=1)

    return data


#function to combine baths
def combine_bath(data):
    full_bath = data['Bsmt Full Bath'] + data['Full Bath']
    half_bath = data['Bsmt Half Bath'] + data['Half Bath']
    total_bath = full_bath + 0.5*half_bath
    data.drop(columns = ['Bsmt Full Bath', 'Bsmt Half Bath', 'Full Bath','Half Bath'], inplace = True)
    data['total_bath'] = total_bath
    return data


#function to create newer built
def add_new_build(data):

    data['newer_build'] = np.where(data['Year Built']>1980,1,0)

    #data = data.drop('Year_Built',axis=1)

    return data

#Data with First Stage Feature Engineering
def process_data_fun(data):
    df = data[['Id','PID']]
    data = data.drop(['Unnamed: 0','Id','PID'], axis = 1)
    data = combine_bath(data)
    data = add_new_build(data)
    data = rail_or_road(data)
    data = convert_to_dummy(data)
    data = data.join(df)

    return data

#convert exter quality to numerical
def exter_to_scale(data):
    extr_dic = {
        'Ex': 2,
        'Gd': 1,
        'TA': 0,
        'Fa': -1,
        'Po': -2
    }

    data['Exter Qual'] =  data['Exter Qual'].map(extr_dic)
    data['Exter Cond'] =  data['Exter Cond'].map(extr_dic)

    return data

#convert exter Condition to numerical
def bsmt_to_scale(data):
    bsmt_dic = {
        'Ex': 3,
        'Gd': 2,
        'TA': 1,
        'Fa': 0,
        'Po': -1,
        'NA': -1
    }

    bsmt_exp_dic = {
        'Gd': 2,
        'Av': 1,
        'Mn': 0,
        'No': -1,
        'NA': -2
    }

    data['Bsmt Cond'] =  data['Bsmt Cond'].map(bsmt_dic)
    data['Bsmt Qual'] =  data['Bsmt Qual'].map(bsmt_dic)
    data['Bsmt Exposure'] = data['Bsmt Exposure'].map(bsmt_exp_dic)

    return data



#convert heating QC to numerical
def heating_to_scale(data):
    heating_dic = {
        'Ex': 3,
        'Gd': 2,
        'TA': 1,
        'Fa': 0,
        'Po': -1
    }

    data['Heating QC'] =  data['Heating QC'].map(heating_dic)

    return data

#convert Kitchen QC to numerical
def kitchen_to_scale(data):
    kitchen_dic = {
        'Ex': 3,
        'Gd': 2,
        'TA': 2,
        'Fa': 0,
        'Po': -1
    }

    data['Kitchen Qual'] =  data['Kitchen Qual'].map(kitchen_dic)

    return data


#converting Fireplace Qu to scale
def fireplace_to_scale(data):
    fire_dic = {
        'Ex': 4,
        'Gd': 2,
        'TA': 1,
        'Fa': 0,
        'Po': -1,
        'NA': 0
    }

    data['Fireplace Qu'] =  data['Fireplace Qu'].map(fire_dic)

    return data


#converting Garage Qu to scale
def garage_to_scale(data):
    garage_dic = {
        'Ex': 7,
        'Gd': 4,
        'TA': 2,
        'Fa': 0,
        'Po': -1,
        'nan': 0
    }

    data['Garage Qual'] =  data['Garage Qual'].map(garage_dic)
    data['Garage Cond'] =  data['Garage Cond'].map(garage_dic)

    return data


#converting Pool Qu to scale
def pool_to_scale(data):

    data['Pool QC'].fillna("NA", inplace=True)
    pool_dict = {
        'NA': 0,
        'Fa': 1,
        'Gd': 2,
        'Ex': 4,
        'TA': 0
    }

    data['Pool QC'] = data['Pool QC'].map(pool_dict)

    return data


#combinding all ordinal variable to numeric scale
def ordinal_to_scale(data):
    data = exter_to_scale(data)
    data = bsmt_to_scale(data)
    data = heating_to_scale(data)
    data = kitchen_to_scale(data)
    data = fireplace_to_scale(data)
    data = garage_to_scale(data)
    data = pool_to_scale(data)

    return data
