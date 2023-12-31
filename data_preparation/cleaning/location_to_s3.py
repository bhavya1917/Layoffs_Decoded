import pandas as pd
import numpy as np
import re
import pandas as pd
import s3fs

AWS_S3_BUCKET = "layoffs-decoded-master"
AWS_ACCESS_KEY_ID = "AKIAUHN3JA72IHF7WP6J"
AWS_SECRET_ACCESS_KEY = "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"

folder_path = "training_data_q3"
csv = "employee_location_locationiq2.csv"


# loading training data from AWS S3
df = pd.read_csv(
    f"s3://{AWS_S3_BUCKET}/{folder_path}/{csv}",
    storage_options={
        "key": AWS_ACCESS_KEY_ID,
        "secret": AWS_SECRET_ACCESS_KEY
    },  usecols=['country']
)


# remove blank entries and strip spaces

df = df.apply(lambda x: x.str.strip())
country_counts = df['country'].value_counts()



folder_path = "feature_results/q3_location"  #you can create your own folder in S3 for each question and put all the tables csv in #that
csv = "test.csv" #give the name of csv that would want in S3

# writing dataframes covid training data to AWS S3
country_counts.to_csv(
    f"s3://{AWS_S3_BUCKET}/{folder_path}/{csv}",
    storage_options={
        "key": AWS_ACCESS_KEY_ID,
        "secret": AWS_SECRET_ACCESS_KEY,
    },
)