import argparse
import requests
import dotenv


args = argparse.ArgumentParser("This is a programme to choose a date and select a year and will provide a playlist during that year")

args.add_argument("-d", "--date", required=True, help="Can you do this in this format: YYYY-MM-DD")

