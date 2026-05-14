import pandas as pd
import os

input_path = "data/raw/data_jobs.csv" 
output_path = "data/processed/jobs_transformed.csv"


def transform_data():

    #Load extracted dataset
    df = pd.read_csv(data_jobs_path)

    #Remove rows where city is null
    df = df[df["city"].notna()]

    #Split city column into city and region
    split_cols = df["city"].str.split(",", expand=True)

    df["city_clean"] = split_cols[0].str.strip()

    if split_cols.shape[1] > 1:
        df["region"] = split_cols[1].str.strip()

    else:
        df["region"] = None

    #Drop original city column
    df.drop(columns=["city"], inplace=True, errors="ignore")

    #Clean text fields
    df["role"] = df["role"].str.title()
    df["title"] = df["title"].str.strip()
    df["city_clean"] = df["city_clean"].str.title()
    df["company"] = df["company"].str.strip()

    #Remove records with null values in specified columns
    df = df.dropna(subset=["title", "company", "city_clean"])

    #Add derived fields
    df["country"] = "Germany"
    df["job_count"] = 1

    #Reset dataframe index
    df.reset_index(drop=True, inplace=True)

    #Create an output folder if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    #Export transformed dataset
    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print("Transformation completed")
    print(f"Final records: {len(df)}")


if __name__ == "__main__":
    transform_data()
