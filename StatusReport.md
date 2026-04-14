# Interim Status Report #

## Plan for Final Deliverable ##

### End Deliverable: ### 
Report with all research and analysis + visualization showing if energy scores for businesses in different neighborhoods are associated with number of energy complaints in those neighborhoods.

## Update to Project Plan ##
Changed original project plan by adding additional dataset about environmental reports in the city of Chicago. This dataset had reports dating back to the 1990s, but we only need info from 2023. We also decided to only use one year of the business energy efficiency score datasets as one year is sufficient for our research question and will be much more manageable for us to analyze.

### Relate Project to Data Lifecycle ###

![image](https://github.com/user-attachments/assets/02450056-cca0-44ef-85ad-9ce2a659a15b)

If we look at the DataONE Data lifecycle, we can map our project down the chart. The data we are using has already been conceptualized and collected. Processing and cleaning must be done on the data before it can be further analyzed to answer questions. It has already been processed in some ways as it has been compiled into a structured format and distributed through the City of Chicago Data Portal. The majority of our project work is pertaining to the discovery and analysis stages of the DataONE lifecycle. We will be taking a deeper look at multiple aspects of our datasets to try to answer our research question. After our disscovery and analysis, the data will have been repurposed in our project. Then our findings will start the cycle over again for others to reference and learn from.


### File Storage and Organization ###

For our project, we’re working with two datasets saved as CSV files. Each file is a table where rows represent individual records and columns represent different attributes, which makes them easy to open and work with in tools like Excel and OpenRefine. The data includes a mix of types, like numbers, text, and some date-related fields. One important thing is that both files share a common columns of Longitude and Latitude which may allow us to connect them. In terms of organization, we’re treating the two CSVs like related tables. Instead of combining everything into one big file right away, we keep them separate and link them when needed using that shared key. This makes the data easier to manage and avoids duplicating information. We also will try to keep things consistent across both files, like making sure column names and formats match, so merging them later is straightforward. Before doing any analysis, we will clean the data by fixing formatting issues, handling missing values, and removing duplicates.

### Ethical Data Handling ###

To begin breaking down the ethical constraints, the first place to look is the data collection. From our analysis, the data from both datasets was acquired ethically and legally. All complaints were submitted voluntarily. Is the address corresponding to resident’s home or the business they are reporting? If it is their home than that could be considered an identifier and should be pseudo’d or perturbed to keep reporters anonymous. Concern for reputation of neighborhoods because ratings and complaints could be subjective.

### Data Collection and Acquisition ###

For our project, we are using two datasets from trustworthy public sources. The first dataset comes from the City of Chicago’s Energy Benchmarking Data, specifically the 2023 dataset (reported in 2024). This dataset is available through the Chicago Open Data Portal and is provided as a structured CSV file with standardized fields like energy usage, emissions, and building characteristics. The second dataset is the CDPH Environmental Complaints dataset, which is also sourced from the Chicago Open Data Portal. This dataset has a different structure, with more categorical and text-based fields related to complaint types, locations, and inspection details. Although both datasets are downloaded as CSV files, they differ in their schemas and the type of data they contain. The energy benchmarking dataset is more numeric and standardized, while the complaints dataset is more variable and descriptive. Both datasets were directly downloaded from the portal, ensuring they are reliable and up to date. Using two datasets with different structures allows us to bring together building-level energy data and environmental complaint data for a more well-rounded analysis.

#### Links: ####
Environmental Complaints: https://data.cityofchicago.org/Environment-Sustainable-Development/CDPH-Environmental-Complaints/fypr-ksnz/about_data

2023 Energy Benchmark Data: https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking-2023-Data-Reported-in-/3a36-5x9a/about_data

### Extraction and Enrichment ###

### Data Integration ###

### Data Quality ###

Data Quality is assessed based on 4 characteristics: Accuracy, Consistency, Timeliness, and Completeness.
