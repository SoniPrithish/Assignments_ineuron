from src.logger import logging
from src.exception import CustomException
import pandas as pd
import requests

class Format_Data:
    def __init__(self):
        logging.info("Program has started")
        pass
       
    def get_and_transform(self,url):
        try:
            logging.info(f'Retrieving data from {url}')
            # Send a GET request to the URL and retrieve the JSON data
            response = requests.get(url)
            data = response.json()
            logging.info(f'Data Recieved')
            # Extracting the pokemon data from the JSON
            pokemon_data = data['pokemon']
            logging.info(f'Data Frame created')
            # Converting JSON data to a DataFrame
            df = pd.json_normalize(pokemon_data)
            logging.info(f'Data Formatted')
            return df
        except Exception as e:
            logging.info("Exception occured while formatting")
            raise CustomException(e,sys)
    def save_data(self,df):
        try:
            logging.info(f'Data has enteres into save stage')
            # Define the output file path
            output_file = 'pokemon_data.xlsx'
            logging.info(f'File will be created as {output_file}')
            # Saving the DataFrame to Excel format
            df.to_excel(output_file, index=False)
            logging.info(f'Data has been converted and saved to {output_file}')
            print("Data has been converted and saved to", output_file)
            return "Done Successfully"
        except Exception as e:
            logging.info(f'Failed to Save')
            raise CustomException(e,sys)

if __name__ == "__main__":
     # Define the URL of the JSON data
    url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
    obj=Format_Data()
    df=obj.get_and_transform(url)
    obj.save_data(df)