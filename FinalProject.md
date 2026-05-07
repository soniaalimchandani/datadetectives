# Environmental Complaints and ENERGY Efficiency Scores in Chicago

# Contributors
## Sonia Alimchandani
- Summary
- Data Profile
- Data Cleaning (Energy Benchmarking 2023 Data)
- Challenges
- Reproducing
## Olivia Cieplak
- Summary
- Data Quality
- Data Cleaning (CDPH Environmental Complaints)
- Metadata

# Summary
For our project we took two datasets from the City of Chicago Data Portal to find information on ENERGY STAR Scores of buildings in Chicago and if there was a relation between these scores and Environmental Complaints in the city. Our main research question was: ‘Is there an association between energy rating and the number of environmental complaints for different neighborhoods in Chicago?’.  To answer this question, we took datasets through the data lifecycle to generate insights and visualizations. 
Once we determined what datasets we were interested in analyzing for the project, we looked for what aspects of the sets were connected and how we could relate features of the sets together. We conceptualized our research question after consulting with each other and course instructors. After we had formed our concept, we extracted the relevant observations from our datasets. For the Environmental Concerns dataset, we only wanted complaints from 2023 as the ENERGY STAR Score dataset we used was from 2023. When we had the appropriate data for our research, we finished cleaning and processing the data which we will explain in greater detail later in the report. The final step we had to perform in order to begin our analysis was merging the datasets. A spatial join was performed by matching complaint records to the nearest benchmarked building based on latitude and longitude proximity. In cases where exact coordinate matches were not available, a distance threshold (such as within a small radius or matching ZIP code support) was used to associate complaints with nearby buildings. This integration allows us to analyze whether buildings with higher energy usage or emissions are located in areas with more environmental complaints. It also helps identify patterns between sustainability performance and community-reported environmental concerns across Chicago neighborhoods. The final merged dataset is 412 rows, with 26 columns.

To derive final insights and analyze our data, we created a few visualizations of data looking for trends and associations to draw conclusions. These will be explained in greater detail later in the report.



# Data Profile

This project combines two open municipal datasets from the City of Chicago to investigate whether there is an association between building energy efficiency (ENERGY STAR ratings) and the number of environmental complaints reported in surrounding areas. Both datasets are structured tabular datasets in CSV format and are processed through a fully automated Snakemake workflow.

## Dataset 1: Environmental Complaints

Location in repository:

data/raw/environmental_complaints.csv

data/cleaned/cleaned_environmental_complaints_2023.csv

This dataset contains individual environmental complaint records submitted by residents in Chicago. Each row represents a single complaint event.

Key variables include:

- Complaint ID (unique identifier)
- Complaint type (e.g., sanitation, air quality, noise)
- Complaint date and resolution date
- Address information
- Latitude and longitude coordinates
- Inspector and resolution metadata

Characteristics:

- High granularity (individual complaint-level observations)
- Contains categorical, temporal, and geospatial variables
- Some missing or inconsistent address and coordinate fields
- Requires spatial aggregation to derive neighborhood-level complaint counts

Ethical and Legal Constraints:

- Publicly available under Chicago’s open data portal licensing
- No personally identifiable information is included
- However, fine-grained geolocation data could potentially be sensitive when combined with other datasets

## Dataset 2: Energy Benchmarking Data

Location in repository:

data/raw/energy_benchmark_2023.csv

data/cleaned/cleaned_energy_benchmarking.csv

This dataset contains building-level energy performance data for Chicago properties. Each row corresponds to a single building.

Key variables include:

- Property name and address
- Building type (commercial, residential, institutional, etc.)
- ENERGY STAR score (1–100 efficiency rating)
- Greenhouse gas emissions (CO₂ equivalent)
- Energy consumption indicators
- Latitude and longitude coordinates

The ENERGY STAR score is the primary variable of interest, representing energy efficiency.

Characteristics:

- Building-level granularity
- Mix of numeric (energy use, emissions, score) and categorical variables (building type)
- Some missing values in energy performance indicators
- Spatial attributes enable geolocation-based merging with complaint data

Ethical and Legal Constraints:

- Publicly released by the City of Chicago under open data policies
- No individual-level personal data is included
- Data is used for research and educational purposes only

## Data Integration

The two datasets are joined using a spatial approximation approach based on rounded latitude and longitude values (to 3 decimal places). This allows linking environmental complaints to nearby buildings with recorded energy performance.

`data/merged_dataset/integrated_dataset.csv`

## Relationship to Research Question

The integration of these datasets directly supports the research question:

**Is there an association between energy rating and the number of environmental complaints?**

This is operationalized as follows:

- Environmental complaints are aggregated geographically to represent local environmental burden
- ENERGY STAR scores represent building-level energy efficiency
- The merged dataset allows comparison of complaint frequency against nearby energy performance

This enables analysis of whether areas with lower energy efficiency (lower ENERGY STAR scores) tend to experience higher numbers of environmental complaints, suggesting a potential relationship between infrastructure performance and reported environmental issues.

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

## CDPH Environmental Complaints Data
For data cleaning of the CDPH Environmental Complaints data, we first made sure all dates were in the same formatting in OpeRefine by converting all values in the complaint date column to standardized Date values. Then we removed all rows without complaint dates. Then we removed all rows with complaint dates outside of 2023 as the other dataset uses only 2023 data, so we wanted the timeframes to match between the datasets. The dataset originally had over 50,000 rows, but this contained information ranging from 1993-2025. After removing other years and only keeping complaints reported from 2023, we were left with 1,994 rows. 

The values in most columns seemed to all have the same syntax, we suspect most questions on the complaint form had a dropdown menu to submit address, complaint type, and more. The `COMPLAINT DETAIL`, though, were typed out by the person submitting the complaints, so we used this column to look for duplicate rows. If an observation had the exact same `COMPLAINT DETAIL`, `COMPLAINT DATE`, `ADDRESS`, and `COMPLAINT ID`, we considered those duplicate rows and dropped them from the dataset as well. After removing duplicate complaints, our final Environmental Complaints dataset was clean with 1,876 rows remaining. These observations were all unique complaints from 2023 with standardized syntactics ready to be used for further analysis.

The OpenRefine json history is linked in the repository: environmentalcomplaintshistory.json

## Energy Benchmarking 2023 Data

For data cleaning for the Energy Benchmarking 2023 data, we first removed approximately 854 incomplete records, about 25% of the dataset. These rows had a Reporting Status of either “Not Submitted” or “Not Covered 2024” and were missing important fields such as floor area, energy use, EUI, GHG emissions, and year built. Since these were structural non-reporters rather than data errors, we excluded them from the main analysis. This improved completeness by removing records with excessive missing data. Afterward, we dropped the Reporting Status column because all remaining rows were marked as “Submitted,” making it redundant and improving consistency.

We then removed columns with excessive missing values or limited relevance. `All Other Fuel Use (kBtu)` (100% null), `District Steam Use (kBtu)` (98.5% null), and `District Chilled Water Use (kBtu)` (97.5% null) were dropped because they were nearly empty. We also removed `Row_ID` since the dataset already included an `ID` column. Columns such as `Electricity Use (kBtu)`, `Natural Gas Use (kBtu)`, and `Water Use (kGal)` were removed because they were either highly incomplete or less useful than summary measures like EUI and GHG emissions. We also dropped `Source EUI`, `Weather Normalized Source EUI`, and `Weather Normalized Site EUI`, keeping only `Site EUI` to reduce redundancy and improve consistency. The `Location` column was removed since latitude and longitude were already available separately.

We standardized the `Exempt From Chicago Energy Rating` column by converting values to consistent TRUE or FALSE entries, improving syntactic accuracy. Records marked TRUE were removed because exempt properties were outside the scope of our analysis and often had missing Chicago Energy Ratings. After filtering, we deleted the column since it was no longer needed.

To improve formatting consistency, we removed commas from numeric fields such as `Gross Floor Area - Buildings (sq ft)` and `Total GHG Emissions (Metric Tons CO2e)` using GREL transformations so values could be treated correctly as numeric data. We also removed periods from `Property Name` and `Address` fields and fixed inconsistent capitalization in `Property Name`, `Address`, `Community Area`, and `Primary Property Type`. These steps improved syntactic accuracy and consistency across the dataset.

Lastly, we reviewed latitude and longitude values for accuracy. Two addresses initially appeared outside Chicago, but both belonged to records already removed under “Not Submitted” or “Not Covered 2024,” so no manual corrections were needed. For the environmental complaints dataset, we also removed rows missing Complaint Dates since we could not verify if they belonged to the 2023 analysis period. This improved completeness and timeliness. Although 690 rows still had blank Complaint Details, we kept them because the remaining complaint information was still useful for identifying patterns.

# Findings

Our final finding is that **there is a negative correlation** between number of environmental complaints and ENERY STAR ratings, but it is hard to say if these results are definitive or should be treated with high regard because of our limited sample size of 412 observations after merging the two datasets. There are some variations to the negative trend line and these results could be improved with more complaints per neighborhood because some of the neighborhoods have a very limited amount of complaints pertaining to them. Though, we do not know if it is a data weakness that some neighborhoods don't have many complaints or if that is an indication of high energy efficiency in that neighborhood.

Before we could begin creating visualizations, we had to create clusters of the data. We thought about going about this a few ways. First, we considered using DBSCAN and clustering based on density. This method wasn't ideal for our purposes because it resulted in over 100 observations being treated as 'noise' or outliers instead of data points used in the analysis. Next, we tried using K-Means clustering. This method worked better and we experimented with different numbers of clusters and minimum amount of observations in clusters. After trying many variations with this method, we felt it was subjective because we were essentially creating our own neighborhoods when Chicago has well-known neighborhoods and areas. The final clustering method we attempted, and the method we ended up using, was grouping the observations by coordinates into pre-established Chicago neighborhoods. We found approximate latitude and longitude coordinates for various Chicago neighborhoods, and we created a new column `neighborhood` that grouped all of the complaint locations. Using this method, we ended with 8 neighborhoods. 

Our first visualization we created is a map of Chicago that displays our 8 different neighborhoods with different colors noting the areas.
<img width="446" height="800" alt="newplot" src="https://github.com/user-attachments/assets/29687a86-fe7e-4563-9c39-fb86c57965cc" />

This map shows the location where complaints in the city took place that overlap with building ENERY STAR submissions from our merged datasets. Seeing this on a map helps us understand where the different neighborhoods are and how dense the number of complaints are per neighborhoods. It does not show ENERGY STAR ratings though, so we had to create more visuals for our analysis.

These are two visualizations that demonstrate our final findings and show the trends we have derived from our datasets. This bar chart shows the number of complaints per neighborhoods with the height of the bar and the black trend line shows the average ENERGY STAR score per neighborhood. As the line graph shows that shows the neighborhoods with low number of environmental complaints generally have higher energy efficiency scores and the neighborhoods with a high number of complaints generally have lower efficiency scores.

<img width="1389" height="690" alt="image" src="https://github.com/user-attachments/assets/2bd8b9c6-7316-4caa-8ed8-f517b49fcafc" />


This final visualization is just another depiction of the information shown in a different way with another set of bars instead of the trend line.

<img width="1585" height="844" alt="image" src="https://github.com/user-attachments/assets/0cc5226e-db77-4962-9d43-7136c6336b34" />


# Future Work

# Challenges
A lot of the challenges in this project weren’t really about the analysis itself, but more about getting everything to run smoothly and consistently. One of the biggest issues we ran into was making sure the workflow worked across different environments. For example, some libraries like plotly worked fine in our Jupyter Notebook, but when we tried to run the same code through Snakemake, it would crash because those packages weren’t installed in that environment. That led to errors like ModuleNotFoundError, which were frustrating at first because the code itself was fine. We ended up fixing this by being more explicit about dependencies and creating a requirements.txt file so everything needed is clearly listed and can be installed beforehand.

Another major challenge was working on Windows. A lot of examples online use Unix-based commands, and we initially used things like cp in our Snakefile without realizing they wouldn’t work in PowerShell. That caused some confusing errors until we figured out the issue. We had to switch to more cross-platform solutions, like handling file copying in Python instead of relying on shell commands. On top of that, we kept running into permission errors, especially with Snakemake’s .snakemake folder. This got even worse because we were working inside a OneDrive folder, which constantly syncs files and can lock them in the background. That led to repeated “access denied” errors that weren’t really about our code at all. Once we understood what was happening, it made more sense, but it definitely slowed things down.

File organization was another area that caused problems early on. We had issues with inconsistent folder names, incorrect paths, and even small things like accidentally saving config files with double .json extensions. Those kinds of mistakes made Snakemake fail because it couldn’t find the right inputs. Cleaning up the folder structure and making everything consistent (like separating raw, cleaned, and merged data) made a big difference.

The last challenge was actually combining the datasets. The complaints data is at the level of individual reports, while the energy data is at the building level, and there’s no shared ID to connect them. We ended up using latitude and longitude to match them, rounding the coordinates to make it work. It’s not perfect, but it was a practical way to link the data and move forward with the analysis. Overall, most of the difficulty came from technical setup and making the workflow reliable, rather than from the actual research question.

# Reproducing

To reproduce this analysis, first clone or download the project repository to your local machine and ensure that it is stored in a standard local directory (it is recommended not to run the workflow inside cloud-synced folders such as OneDrive, as this can cause file locking errors). Open a terminal and navigate to the root project directory containing the Snakefile. Next, install the required Python dependencies by running pip install -r requirements.txt. This will install all necessary packages, including pandas, matplotlib, seaborn, and plotly. Once the environment is set up, run the full workflow using Snakemake with the command python -m snakemake --cores 1. This command will automatically execute all steps in the correct order, including downloading the raw datasets, applying data cleaning steps (or copying pre-cleaned data if OpenRefine is not installed), merging the datasets based on rounded latitude and longitude values, and running the analysis scripts to generate outputs. All final results, including summary statistics and visualizations, will be saved in the results/ folder. If the workflow fails due to an interrupted run or a locking issue, it can be reset by running python -m snakemake --unlock and then rerunning the workflow. To ensure a completely fresh run, users can optionally delete existing outputs or run python -m snakemake --delete-all-output before execution. All required input data is included in the repository under the data/raw/ directory, and all intermediate datasets are generated automatically by the workflow. By following these steps, a user should be able to reproduce the full pipeline and obtain identical results from start to finish.

# Metadata

Machine Readable Descriptive metadata file describing project in conformance with DCAT is linked in the repository: metadata.json

### Data Dictionary
| Column | Type | Description |
|--------|-------|-------------|
| **COMPLAINT ID** | Integer | Unique identifier for the environmental complaint |
| **COMPLAINT TYPE** | String | The type of complaint reported (Noise, Pollution, etc.) |
| **ADDRESS** | String | Street address linked with **environmental complaint** |
| **STREET NUMBER FROM** | Integer/String | Starting street number for location range |
| **STREET NUMBER TO** | Integer/String | Ending street number for location range (usually NaN if single address provided) |
| **DIRECTION** | String | Direction prefix of street (N, E, S, or W) |
| **STREET NAME** | String | Name of street where complaint is located |
| **STREET TYPE** | String | Suffix of street |
| **INSPECTOR** | Integer | ID of complaint inspector |
| **COMPLAINT DATE** | DateTime | Date when complaint was filed |
| **LOCATION** | String | Geospatial point coordinates of **environmental complaint** |
| **Property Name** | String | Name of building or property |
| **Address** | String | Address for building linked with **energy report** information |
| **ZIP Code** | Integer | 5-digit postal code of business/property |
| **Primary Property Type** | String | Main usage category of building from energy report |
| **ENERGY STAR Score** | Float | 1-100 rating of building energy efficiency |
| **Total GHG Emissions (Metric Tons CO2e)** | Float | Total greenhouse gas emmissions by property |
| **energy_lat** | Float | Latitude coordinate for **energy reporting** business/property |
| **energy_lon** | Float | Longitude coordinate for **energy reporting** business/property |
| **neighborhood** | String | Chicago community area/name of property; derived from latitude and longitude values |


# References
