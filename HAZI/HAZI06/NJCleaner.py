import pandas as pd

class NJCleaner():

    def __init__(self,csv_path: str):
        self.data = pd.read_csv(csv_path)


    def order_by_scheduled_time(self):
        order = self.data.sort_values(by=['scheduled_time'])
        return order


    def drop_columns_and_nan(self):
        dropped = self.data.drop(['from','to'], axis= 1)
        dropped = dropped.dropna()
        return dropped
    
    def convert_date_to_day(self):
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data['day'] = self.data['date'].dt.day_name()
        days = self.data.drop(['date'],axis=1)
        return days
    

    def convert_scheduled_time_to_part_of_the_day(self):
        self.data['scheduled_time'] = pd.to_datetime(self.data['scheduled_time'])
        self.data['scheduled_time'] = self.data['scheduled_time'].dt.hour
        self.data['part_of_the_day'] = pd.cut(self.data['scheduled_time'], bins=[-1,3.9,7.9,11.9,15.9,19.9,23.9], labels=['late_night', 'early_morning', 'morning', 'afternoon', 'evening','night'])
        converted = self.data.drop(['scheduled_time'],axis = 1)
        return converted
    
    def convert_delay(self):
        delay = self.data
        delay['delay'] = [0 if x < 5 else 1 for x in delay['delay_minutes']]
        return delay
    
    def drop_unnecessary_columns(self):
        necessary = self.data.drop(['train_id','actual_time','delay_minutes'],axis=1)
        return necessary
    
    def save_first_60k(self,path: str):
        first_60k = self.data.head(60000)
        first_60k.to_csv(path,index=False)


    def prep_df(self,path = 'data/NJ.csv'):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()
        self.save_first_60k(path)
