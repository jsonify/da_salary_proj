#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 23:52:18 2021

@author: jruecke
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/usr/local/bin/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)