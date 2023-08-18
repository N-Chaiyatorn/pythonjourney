
import pandas

class DataManager():
    def __init__(self):
        self.data_dict = {}
        self.column_list = []
        self.dataframe = None
        self.lastest_row_dict = {}

    def is_reset_data(self, file_name):
        reset = input(f"Do you want to reset your data in {file_name} (Type 'y' or 'n'): ")
        if reset != 'y' and reset != 'n':
            print(f"Your answer {reset} is invalid, please only type 'y' or 'n'.")
            raise ValueError()
                
        if reset == 'y':
            return True
        elif reset == 'n':
            return False

    def set_column_list(self, weather_data):
        """Determine dataframe column."""
        self.column_list.append('date')
        self.column_list.append('time')

        for weather_col in weather_data:
            self.column_list.append(weather_col)

    def getting_repeatly_dataframe(self):
        repeatly_time_dataframe = self.dataframe[self.dataframe["time"] == self.lastest_row_dict["time"][0]]
        repeatly_time_and_date_dataframe = repeatly_time_dataframe[repeatly_time_dataframe["date"] == self.lastest_row_dict["date"][0]]

        return repeatly_time_and_date_dataframe

    def creating_empty_data_dict(self):
        """Creating initial data dictionary."""
        return {column:[] for column in self.column_list}

    def update_lastest_row_dict(self, weather_data_in_each_hours, time_data):
        """Update data dictionary in each hour."""
        self.lastest_row_dict = self.creating_empty_data_dict()
        self.lastest_row_dict['date'].append(str(time_data.date()))
        self.lastest_row_dict['time'].append(str(time_data.hour) + ':00')

        for col in weather_data_in_each_hours:
            self.lastest_row_dict[col].append(weather_data_in_each_hours[col])

    def getting_raining_time_dataframe(self):
        return self.dataframe[self.dataframe["main"] == "Rain"]

    def creating_dataframe(self):
        self.dataframe = pandas.DataFrame(self.data_dict)
