
from flask import Flask, render_template, json
import numpy as np
import pandas as pd
import os,sys
from datetime import datetime
from datetime import timedelta
from __future__ import print_function
import time
from google.cloud import bigtable
from google.cloud.bigtable.row_set import RowSet
from google.cloud.bigtable.row_set import RowRange
from collections import defaultdict


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


def query_builder():
    all_pairs = ["LTC/USD", "BTC/GBP", "XLM/USD", "BTC/JPY", "BTC/EUR", "XRP/USD", "XRP/BTC", "XMR/USD", "XLM/BTC",
             "BTC/USD", "LTC/BTC", "XRP/EUR", "XMR/BTC", "XTZ/BTC"]
    pairs = ["BTC/USD"]
    exchanges = ["bitfinex", "bitStamp", "poloniex", "gemini", "hitBTC", "okCoin"]

    rowset = RowSet()
    for pair in pairs:
        for exchange in exchanges:
            startkey = "{}#{}#{}".format(pair, exchange,
                                         int(time.mktime((datetime.now() - timedelta(seconds=3)).timetuple())))
            endkey = "{}#{}#{}".format(pair, exchange,
                                           int(time.mktime((datetime.now() + timedelta(seconds=1)).timetuple())))
            rowrange = RowRange(start_key=startkey, end_key=endkey)
            rowset.add_row_range(rowrange)
    return rowset

def callable_defaultdict_list():
    return defaultdict(list)

def query_data():
    starttime = time.time()
    trades_values = defaultdict(callable_defaultdict_list)
    trades_timestamps = defaultdict(callable_defaultdict_list)
    for row in table.read_rows(row_set=query_builder()):
        date_string = datetime.fromtimestamp(
            int(row.row_key.decode('utf-8').split("#")[-2][0:-3])
            )
        for column_family, cell in row.cells.items():
            trades_values[column_family]["key"].append(row.row_key.decode('utf-8'))
            for column_name, cell_value in cell.items():
                trades_values[column_family][column_name].append(cell_value[0].value.decode('utf-8'))
                trades_timestamps[column_family][column_name].append(date_string)

    trades_values_numpy = defaultdict(callable_defaultdict_list)
    trades_timestamp_values_numpy = defaultdict(callable_defaultdict_list)
    endbigtabletime = time.time()
    print ("Done Retrieving from BigTable in ")
    print (endbigtabletime - starttime)

    # SAMPLING
    SAMPLE_SIZE = 5000
    for trades, columns in trades_values.items():
        for column_name, values in columns.items():
            trades_values_numpy[trades][column_name] = np.array(values)[::max(len(values)/SAMPLE_SIZE,1)]
    for trades, columns in trades_timestamps.items():
        for column_name, values in columns.items():
            trades_timestamp_values_numpy[trades][column_name] = np.array(values)[::max(len(values)/SAMPLE_SIZE,1)]
    endsamplingtime = time.time()
    print ("Done Sampling in ")
    print (endsamplingtime - endbigtabletime)
    return (trades_values_numpy, trades_timestamp_values_numpy)

@app.route("/stream")
def stream():
    return render_template('streamingvisjs.html', **locals())

@app.route("/getStreamingData")
def getStreamingData():
    trades_tuple = query_data()
    return json.dumps(pd.Series(trades_tuple).to_json(orient='index'))

def main(argv):
    project_name = argv[0]
    bigtable_instance = argv[1]
    bigtable_table = argv[2]
    bigtable_family = argv[3]
    global client
    global instance
    global table
    global family
    client = bigtable.Client(project=project_name, admin=True)
    instance = client.instance(bigtable_instance)
    table = instance.table(bigtable_table)
    family = bigtable_family

if __name__ == "__main__":
    main(sys.argv[1:])
    app.run(port=5000,debug=True,host="0.0.0.0")
