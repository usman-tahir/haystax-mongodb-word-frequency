#!/bin/bash

# Seed the Mongo Database with data
# Remember to manually remove the existing data first
python3 Utility.py mongodb://admin:password@ds251197.mlab.com:51197/word_frequencies

# Run the Application
python3 App.py mongodb://admin:password@ds251197.mlab.com:51197/word_frequencies