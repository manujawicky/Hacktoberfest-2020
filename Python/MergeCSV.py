import os, glob
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Get commnd line argument')

# Get command line arguments
parser.add_argument("-folder_path",
                    "--csv_folder_path",
                    help='get the splitted csv folder path',
                    required=True
                    )


args = parser.parse_args()

# Assign variables for commandline arguments and assign input and output paths
input_path = str(args.json_folder_path) + "/"

# merging operation
all_files = glob.glob(os.path.join(input_path, "/*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "merged.csv")