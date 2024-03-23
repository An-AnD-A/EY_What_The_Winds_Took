import pandas as pd
import json
import rasterio


def read_csv_json(file_path: str, col_names= None):
    """
    The function reads a csv file as a pandas DataFrame.
    :param file_path: The path to the csv file location.
    :return: Pandas DataFrame
    """
    if file_path.endswith(".csv"):
        df = pd.read_csv(filepath_or_buffer=file_path)
    elif file_path.endswith(".json"):
        data = open(r"C:\Users\anand\Projects\Enefit\Data\county_id_to_name_map.json")
        data_dict = json.load(data)
        df = pd.DataFrame(data_dict.items(), columns=col_names)
    return df


def read_excel(file_path: str, **kwargs):
    """
    The function reads an Excel file as a pandas DataFrame.
    :param file_path: The path to the Excel file location.
    :param kwargs: Other parameters that can be passed on to pandas read_excel function.
    :return: Pandas DataFrame
    """
    df = pd.read_excel(io=file_path, **kwargs)
    return df


def read_json(file_path):
    """
    The function reads json files as a Dictionary object.

    # Needs improvements. Dataframe is not made correctly.
    :param file_path: The path to the json file location.
    :return: Dictionary object
    """
    json_data = open(file_path)
    json_dict = json.load(json_data)
    df = pd.DataFrame(json_dict.items())
    return df


def read_tif(file_path):
    """
    This function reads a tif file and returns the image as a ndarray.
    :param file_path:
    :return:
    """

    arr = rasterio.open(file_path)
    return arr


def read_df(file_path: str, col_name=[]):
    """
    The function reads different file formats. Currently functional for csv and excel files.
    :param file_path: The path location to the desired file
    :return: A pandas DataFrame.
    """
    try:
        df = read_csv_json(file_path=file_path,col_names=col_name)
        print("csv file detected and read.")
    except OSError:
        print("The given file is not a csv file")
        try:
            df = read_excel(file_path=file_path)
            print("excel file detected amd read.")
        except OSError:
            print("The given file path is not a csv or excel file")
            df = None
            try:
                df = read_json(file_path=file_path)
                print("Json file detected and read")
            except OSError:
                print("The given file is not a csv, excel or json type file")

    return df

