import os

PROJ_BASE_LOCATION = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_LOCATION = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                             '..', "Data", "GeoLife Challenge"))

data_pathlog = {
    "Climate": {
        "BioClimatic_Average_1981-2010" : os.path.join(DATA_LOCATION,
                                                       "Climate", "BioClimatic_Average_1981-2010"),
        "Climatic_Monthly_2000-2019" : os.path.join(DATA_LOCATION,
                                                    "Climate", "Climatic_Monthly_2000-2019"),
        "Climatic_Monthly_2000-2019_cubes": os.path.join(DATA_LOCATION,
                                                         "Climate", "Climatic_Monthly_2000-2019_cubes"),
        "PA_bioclimatic_avg_test": os.path.join(DATA_LOCATION,
                                                "Climate", "GLC24-PA-test-bioclimatic-average.csv"),
        "PA_bioclimatic_monthly_test": os.path.join(DATA_LOCATION,
                                                    "Climate", "GLC24-PA-test-bioclimatic-monthly.csv"),
        "PA_bioclimatic_avg_train": os.path.join(DATA_LOCATION,
                                                 "Climate", "GLC24-PA-train-bioclimatic-average.csv"),
        "PA_bioclimatic_monthly_train": os.path.join(DATA_LOCATION,
                                                     "Climate", "GLC24-PA-train-bioclimatic-monthly.csv"),
        "PO_bioclimatic_avg_train": os.path.join(DATA_LOCATION,
                                                 "Climate", "GLC24-PO-train-bioclimatic-average.csv"),
        "PO_bioclimatic_monthly_train": os.path.join(DATA_LOCATION,
                                                     "Climate", "GLC24-PO-train-bioclimatic-monthly.csv"),
    },
    "Elevation": {
        "ASTER_DEM_Elevation": os.path.join(DATA_LOCATION,
                                            "Elevation", "BioClimatic_Average_1981-2010"),
        "Elevation_PA_Test_data": os.path.join(DATA_LOCATION,
                                               "Elevation", "GLC24-PA-test-elevation.csv"),
        "Elevation_PA_Train_data": os.path.join(DATA_LOCATION,
                                                "Elevation", "GLC24-PA-train-elevation.csv"),
        "Elevation_PO_Train_data": os.path.join(DATA_LOCATION,
                                                "Elevation", "GLC24-PO-train-elevation.csv")
    },
    "Human_Footprint": {
        "summarized" : os.path.join(DATA_LOCATION, "HumanFootprint", "summarized"),
        "detailed" : os.path.join(DATA_LOCATION, "HumanFootprint", "detailed"),
        "GLC24-PA-test-human-footprint": os.path.join(DATA_LOCATION, "HumanFootprint",
                                                      "GLC24-PA-test-human-footprint.csv"),
        "GLC24-PA-train-human-footprint": os.path.join(DATA_LOCATION, "HumanFootprint",
                                                       "GLC24-PA-train-human-footprint.csv"),
        "GLC24-PO-train-human-footprint": os.path.join(DATA_LOCATION, "HumanFootprint",
                                                       "GLC24-PO-train-human-footprint.csv"),
    },
    "LandCover": {
        "GLC24-PA-test-landcover": os.path.join(DATA_LOCATION, "LandCover",
                                                "GLC24-PA-test-landcover.csv"),
        "GLC24-PA-train-landcover": os.path.join(DATA_LOCATION, "LandCover",
                                                 "GLC24-PA-train-landcover.csv"),
        "GLC24-PO-train-landcover": os.path.join(DATA_LOCATION, "LandCover",
                                                 "GLC24-PO-train     -landcover.csv"),
        "LandCover_Tif_file": os.path.join(DATA_LOCATION, "LandCover",
                                           "LandCover_MODIS_Terra-Aqua_500m.tif"),
    },
    "Soilgrids": {
        "SoilMapping": os.path.join(DATA_LOCATION, "Soilgrids",
                                    "SoilMapping"),
        "GLC24-PA-test-soilgrids": os.path.join(DATA_LOCATION, "Soilgrids",
                                                "GLC24-PA-test-soilgrids.csv"),
        "GLC24-PA-train-soilgrids": os.path.join(DATA_LOCATION, "Soilgrids",
                                                 "GLC24-PA-train-soilgrids"),
        "GLC24-PO-train-soilgrids": os.path.join(DATA_LOCATION, "Soilgrids",
                                                 "GLC24-PO-train-soilgrids"),
    }
}

if __name__ == "__main__":

    print(f"The Base directory of the project : {PROJ_BASE_LOCATION}")
    print(f"The Data directory of the project : {DATA_LOCATION}")

    print("#"*50)

    for i, k in data_pathlog.items():
        print(f"The {i} related files are", "\n")
        for files, path  in k.items():
            print(f"filename : {files}", "\n", f"Path : {path}", "\n")

