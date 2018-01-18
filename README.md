# Haystax MongoDB Word Frequency

### Prerequisites
* Python 3.6.X
* `pip`

### Overview

This application allows the user to determine word trends over a number of days, given a set of words, and the timestamps associated with them. The timestamps (and the words correlating to them) are arranged by hour on the day that they've been generated for, and the "days" are searched for certain trends, as shown in the report generation.

### Usage

To use this application, first run `pip install -r requirements.txt` to install the requirements associated with the project. Next, run the `run.sh` script provided, as such:

`$ ./run.sh`

This will seed the Mongo database associated with this application (hosted by mLab), and then run the metrics on the generated words.