
import pandas

class DataManager():
    def __init__(self):
        self.current_dataframe = None
        self.new_row_data_dict = {}
        self.dataframe_column_name_list = []
        self.data_frame = None

    def is_same_day_and_same_hours(self):
        repeatly_time_data_rows = self.current_dataframe[self.current_dataframe['time'] == self.new_row_data_dict['time'][0]]
        repeatly_time_and_date_data_rows = repeatly_time_data_rows[repeatly_time_data_rows['date'] == self.new_row_data_dict['date'][0]]

        if repeatly_time_and_date_data_rows.empty:
            return False
        elif not repeatly_time_and_date_data_rows.empty:
            return True

        


    def gets_dataframe_column_name_list(self, weather_in_hour_data):
        self.dataframe_column_name_list.append("date")
        self.dataframe_column_name_list.append("time")

        for col in weather_in_hour_data:
            self.dataframe_column_name_list.append(col)

    def create_empty_data_dict(self):
        return {column:[] for column in self.dataframe_column_name_list} 

    def update_each_hour_data_dict(self, weather_in_hour_data, twelve_hour_clock_time, date):
        self.new_row_data_dict = self.create_empty_data_dict()
        self.new_row_data_dict['date'].append(date)
        self.new_row_data_dict['time'].append(twelve_hour_clock_time)

        for col in weather_in_hour_data:
            self.new_row_data_dict[col].append(weather_in_hour_data[col])


    def gets_data_frame(self, data_dict):
        return pandas.DataFrame(data_dict)
 