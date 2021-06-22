# gc_bigquery_connector
Connect to BigQuery for both publice and private datasets

## Purpose
The purpose of this project is to connect to Google BigQuery via code. The intent is to connect to personal BQ account and perform basic CRUD operations on my own datasets. This is intended to be a command line tool for data analytics projects.

## Relies on
* google.cloud python package

## Goals
* Refactor handling of authentication json file with access key
* Connect to existing data set and ammend CSV data to specified table
* Add abilty to create, drop new or existing tables in a specified dataset
