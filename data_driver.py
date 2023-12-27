# ==================================================================
#
#
#   Name: data_driver.py
#
#   Author: DG
#
#   Purpose: This file is meant to handle the data cleaning process
#
#
#
# ==================================================================

import pandas as pd
import logging
import sys
import datetime
from envir_vars import *


def run_proc(run_steps):
    # This is the driver function where the different data functions are controlled by the run_steps parameter

    if "DATA-METRICS" in run_steps:
        # This is going to be the clearing house of the data set metrics

        raw_data = pd.read_csv(f'{datadir}\\RAW\\sentiment_140.csv', header=False)

        raw_data.columns = ['target', 'ids', 'date', 'flag', 'user', 'text']

        logging.info(raw_data.shape)



if __name__ == '__main__':

    cur_ts = datetime.datetime.now()

    run_steps = sys.argv[1:]

    log_fl_nm = 'data_{run_steps[0]}_{str(cur_ts.year)}{str(cur_ts.month).zfill(2)}{str(cur_ts.day).zfill(2)}_{str(cur_ts.hour).zfill(2)}{str(cur_ts.minute).zfill(2)}{str(cur_ts.second).zfill(2)}.log'

    logging.basicConfig(filename=f'{logdir}/{log_fl_nm}', level=logging.DEBUG)

    run_proc(run_steps=run_steps)
