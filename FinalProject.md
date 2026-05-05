# Environmental Complaints and ENERGY Efficiency Scores in Chicago

# Contributors
- Sonia Alimchandani
- Olivia Cieplak

# Summary
For our project we took two datasets from the City of Chicago Data Portal 

# Data Profile

# Data Quality
Data Quality is assessed based on 4 characteristics: Accuracy, Consistency, Timeliness, and Completeness.

Analysis on Environmental Concerns Data:

Completeness: 690 rows with blank 'Complaint Details.' These values being incomplete will make it harder to detect duplicate rows because identical details would be a high indicator of a duplicate complaint. We also had to delete all columns that were missing a Complaint Date. There is no way to tell if those complaints were from 2023, so they had to be dropped. Those rows could have been from 2023 and would have influenced our results, but they were empty.

Synctactic Accuracy: Dates in date columns are in the same format. Our analysis did not find many typos or errors in this dataset. All values in columns correspond with the domain that those columns cover.

Semantic Accuracy: To determine semantic accuracy of the data, we need to compare column values to true values. This is hard to verify as we cannot check these things.

Consistency: Formatting and values in different columns are consistent. The addresses all have street numbers, street directions, street names, and street types making the address information very consistent. Not all complaints have complaint details which is a big inconsistency in the data.

Timeliness (Currency): This dataset is updated very frequently on a daily or every few days basis. The data from the set that we are using, however, is pretty fixed. We are only extracting the rows with comlaints from 2023 for our analysis. All of the complaints have a 'RESOLVED DATE,' so the information is current and was updated promptly upon resolution of the complaint.

Analysis on Building Efficiency Scores Data:

Completeness: There are 353 blank Chicago Energy Ratings in the dataset for buildings that were exempt from reporting their information. Many columns in the dataset are missing information. We will most likely have to drop rows that were exempt from being rated and for buildings that did not report their information, so it will hurt the completeness and analysis for our final report.

Synctactic Accuracy: Property Names are not all business or property names, some are just addresses. Address values have different formats and are written out in various ways. Community Areas seem to be synctactically accurate which is one of the most important columns for our purposes.

Semantic Accuracy: To determine semantic accuracy of the data, we need to compare column values to true values. This is hard to verify as we cannot check these things.

Consistency: All rows have community areas, addresses, and property types. Not all buildings that submitted for a rating received one though. There are blank columns and '0.0' scores which is an inconsistency. All buildings that reported their information should have received a score. Also because a lot of columns are missing energy usage information we don't know how everything is weighed to give the buildings ratings.

Timeliness (Currency): The dataset has 2023 information and was reported in 2024. The dataset has not been updated since 2025 as it is fixed.


# Data Cleaning

Olivia - describe cleaning of environmental complaints data in OpenRefine & provide JSON receipts

# Findings

# Future Work

# Challenges

# Reproducing

# Metadata

DCAT

# References
