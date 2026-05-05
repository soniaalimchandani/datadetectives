# Environmental Complaints and ENERGY Efficiency Scores in Chicago

# Contributors
## Sonia Alimchandani
- Data Cleaning (Energy Benchmarking 2023 Data)
- 
## Olivia Cieplak
- Summary
- Data Quality

# Summary
For our project we took two datasets from the City of Chicago Data Portal to find information on ENERGY STAR Scores of buildings in Chicago and if there was a relation between these scores and Environmental Complaints in the city. Our main research question was: ‘Is there an association between energy rating and the number of environmental complaints for different neighborhoods in Chicago?’.  To answer this question, we took datasets through the data lifecycle to generate insights and visualizations. 
Once we determined what datasets we were interested in analyzing for the project, we looked for what aspects of the sets were connected and how we could relate features of the sets together. We conceptualized our research question after consulting with each other and course instructors. After we had formed our concept, we extracted the relevant observations from our datasets. For the Environmental Concerns dataset, we only wanted complaints from 2023 as the ENERGY STAR Score dataset we used was from 2023. When we had the appropriate data for our research, we finished cleaning and processing the data which we will explain in greater detail later in the report. The final step we had to perform in order to begin our analysis was merging the datasets. SONIA WRITE ABOUT MERGING STEPS HERE ex. 
- Merged based on coordinates,
- distance of points,
- how many rows we ended up with after merging…


Summarize visualization creation
-	Making neighborhoods based on coordinates
-	Etc
Analysis based on visualizations and final takeaways


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

## Energy Benchmarking 2023 Data

For data cleaning for the Energy Benchmarking 2023 data, we first removed approximately 854 incomplete records, about 25% of the dataset. These rows had a Reporting Status of either “Not Submitted” or “Not Covered 2024” and were missing important fields such as floor area, energy use, EUI, GHG emissions, and year built. Since these were structural non-reporters rather than data errors, we excluded them from the main analysis. This improved completeness by removing records with excessive missing data. Afterward, we dropped the Reporting Status column because all remaining rows were marked as “Submitted,” making it redundant and improving consistency.

We then removed columns with excessive missing values or limited relevance. `All Other Fuel Use (kBtu)` (100% null), `District Steam Use (kBtu)` (98.5% null), and `District Chilled Water Use (kBtu)` (97.5% null) were dropped because they were nearly empty. We also removed `Row_ID` since the dataset already included an `ID` column. Columns such as `Electricity Use (kBtu)`, `Natural Gas Use (kBtu)`, and `Water Use (kGal)` were removed because they were either highly incomplete or less useful than summary measures like EUI and GHG emissions. We also dropped `Source EUI`, `Weather Normalized Source EUI`, and `Weather Normalized Site EUI`, keeping only `Site EUI` to reduce redundancy and improve consistency. The `Location` column was removed since latitude and longitude were already available separately.

We standardized the `Exempt From Chicago Energy Rating` column by converting values to consistent TRUE or FALSE entries, improving syntactic accuracy. Records marked TRUE were removed because exempt properties were outside the scope of our analysis and often had missing Chicago Energy Ratings. After filtering, we deleted the column since it was no longer needed.

To improve formatting consistency, we removed commas from numeric fields such as `Gross Floor Area - Buildings (sq ft)` and `Total GHG Emissions (Metric Tons CO2e)` using GREL transformations so values could be treated correctly as numeric data. We also removed periods from `Property Name` and `Address` fields and fixed inconsistent capitalization in `Property Name`, `Address`, `Community Area`, and `Primary Property Type`. These steps improved syntactic accuracy and consistency across the dataset.

Lastly, we reviewed latitude and longitude values for accuracy. Two addresses initially appeared outside Chicago, but both belonged to records already removed under “Not Submitted” or “Not Covered 2024,” so no manual corrections were needed. For the environmental complaints dataset, we also removed rows missing Complaint Dates since we could not verify if they belonged to the 2023 analysis period. This improved completeness and timeliness. Although 690 rows still had blank Complaint Details, we kept them because the remaining complaint information was still useful for identifying patterns.

# Findings

# Future Work

# Challenges

# Reproducing

# Metadata

DCAT

# References
