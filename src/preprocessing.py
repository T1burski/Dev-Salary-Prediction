import numpy as np

class Preprocess:

    def __init__(self, data):
        self.raw_data = data
        self.processed_data = None
        self.cols = ["Country", "DevType", "EdLevel", "YearsCodePro", "Salary"]

    def initial_treatments_ingestion(self):
        self.raw_data = self.raw_data.rename({'ConvertedComp': 'Salary'}, axis = 1)
        self.raw_data = self.raw_data.dropna()
        self.raw_data = self.raw_data.loc[self.raw_data['Employment'] == "Employed full-time"]
        self.raw_data["DevType"] = self.raw_data["DevType"].str.split(";")
        self.raw_data['DevType'] = self.raw_data['DevType'].str[0]

        def remove_minor_types(df, feature, cutoff=100):

            # function created to classify values from column
            # with way too few instances based on threshold

            types_to_remove = []

            for a, b in dict(df[feature].value_counts()).items():
                if b <= cutoff:
                    types_to_remove.append(a)
            
            df[feature] = np.where(df[feature].isin(types_to_remove), 'Other', df[feature])
            
            return df
        
        self.raw_data = remove_minor_types(self.raw_data, 'DevType')
        self.raw_data = remove_minor_types(self.raw_data, 'Country', cutoff=400)

        self.raw_data = self.raw_data[self.cols]

        self.raw_data = self.raw_data[self.raw_data['Salary'] <= 250000]
        self.raw_data = self.raw_data[self.raw_data['Salary'] >= 5000]
        self.raw_data = self.raw_data[self.raw_data['Country'] != 'Other']
        self.raw_data = self.raw_data[self.raw_data['DevType'] != 'Other']
        self.raw_data = self.raw_data[self.raw_data['DevType'] != 'Other (please specify):']

        return self.raw_data
    
    def years_correction(self, df):
        if df["YearsCodePro"] == 'Less than 1 year':
            return 0.5
        if df["YearsCodePro"] == 'More than 50 years':
            return 50
        return float(df["YearsCodePro"])

    def edu_level_adjust(self, df):
        if 'Bachelor’s degree' in df["EdLevel"]:
            return 'Bachelor’s degree'
        if 'Master’s degree' in df["EdLevel"]:
            return 'Master’s degree'
        if 'Professional degree' in df["EdLevel"] or 'Other doctoral' in df["EdLevel"]:
            return 'Post grad'
        return 'Less than a Bachelors'
    
    def total_preprocess(self):
        
        self.processed_data = self.initial_treatments_ingestion()

        self.processed_data["YearsCodePro"] = self.processed_data.apply(lambda x: self.years_correction(df = x), axis=1)
        self.processed_data["EdLevel"] = self.processed_data.apply(lambda x: self.edu_level_adjust(df = x), axis=1)

        return self.processed_data

