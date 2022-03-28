import pandas as pd
'''
I chose a dataset (CSV file) on traffic accidents in Virginia Beach, It was very big with 30 columns and 
so I reduced the number of columns by getting rid of the unnecessary ones and summarizing some important 
information by grouping, taking means, etc. After that I converted the updated dataset to a JSON file 
and saved it to my local desk.
'''

#Fetch / download / retrieve a remote data file by URL
url = "https://s3.amazonaws.com/vbgov-ckan-open-data/Police+Traffic+Crash+Reports.csv"
#Try / Catch with error messages
try:

	data = pd.read_csv(url)

	print("Data as read from the CSV URL file:")
	print(data.head())

	#Modify the number of columns from the source to the destination, reducing or adding columns. 
	data.drop('City', inplace=True, axis=1)
	data.drop('State', inplace=True, axis=1)
	data.drop('At Intersection', inplace=True, axis=1)
	data.drop('Nearest Street', inplace=True, axis=1)
	data.drop('Zone ID', inplace=True, axis=1)
	data.drop('Precinct', inplace=True, axis=1)
	data.drop('Location of First Harmful Event', inplace=True, axis=1)
	data.drop('Weather Condition', inplace=True, axis=1)
	data.drop('Traffic Control Device', inplace=True, axis=1)
	data.drop('Traffic Control Type', inplace=True, axis=1)
	data.drop('Roadway Alignment', inplace=True, axis=1)
	data.drop('Roadway Surface Condition', inplace=True, axis=1)
	data.drop('Roadway Surface type', inplace=True, axis=1)
	data.drop('Roadway Description', inplace=True, axis=1)
	data.drop('Roadway defects', inplace=True, axis=1)
	data.drop('Relation to Roadway', inplace=True, axis=1)
	data.drop('Intersection Type', inplace=True, axis=1)
	data.drop('Work Zone Related', inplace=True, axis=1)
	data.drop('Work Zone Location', inplace=True, axis=1)
	data.drop('Work Zone Type', inplace=True, axis=1)
	data.drop('Workers Present in Work Zone', inplace=True, axis=1)
	data.drop('School Zone', inplace=True, axis=1)


	print("Data after deleting 22 columns:")
	print(data.head())

	#Generate a brief summary of the data file ingestion 
	print("The number of columns: " + str(len(data.columns)))
	print("The number of records: " + str(len(data)))

	print("The average number of vehicles invloved in accidents: " + str(data["Number of Vehicles Involved"].mean()))
	print("The number of accidents that ocurred during the daylight: " + str((data["Light Conditions"]=="DAYLIGHT").sum()))
	print("The number of accidents that ocurred each day of the week: ")
	print(data.groupby(['Day of Week'])['Day of Week'].count())

	#convert csv to json - written to disk (local file) 
	try:
		data.to_json(r'/Users/saranasaif/Documents/Data Science/data.json')
		print("The JSON file has been successfully written to your local desk")

	except Exception:
		print("ERROR: An exception occured when trying to convert the file to JSON. Please double check the path")


except Exception:
    print("ERROR: Something went wrong. Double check the URL!")