## ENERGY TRANSPARENCY AND BUILDING PERFORMANCE IN CHICAGO

## Overview

The goal of our project is to research the Chicago ENERY STAR Scores for large buildings of different property types over recent years and identify trends and connections in the data to answer questions. There will be multiple steps and approaches we will have to perform in the analysis of this data. Merging the datasets from each year will help us see how scores for buildings changed year to year. We will also have to clean the data as there are missing datapoints from buildings that were exempt from submitting certain years and from buildings that just simply failed to submit. Using the data, we want to explore if certain Chicago neighborhoods and property types play a role in building energy use performance.

This project builds on Chicago’s energy transparency policies, including the Chicago Energy Benchmarking Ordinance and the Chicago Energy Rating System. The benchmarking ordinance, enacted in 2013, requires large buildings to measure and report their annual energy use. To expand this effort, the Energy Rating System was introduced in 2017 and began assigning buildings a 0–4 star energy rating in 2019. These ratings must be displayed publicly and disclosed during property sales or leases, with the goal of increasing transparency and encouraging property owners to improve energy efficiency. Ultimately, this analysis aims to provide insight into how energy transparency policies may influence building efficiency and contribute to broader climate and sustainability goals.


### Team Members and Responsibilities

#### Olivia Cieplak
- **Data lifecycle (cf. Module 1):** Relate your project to one or more of the lifecycle models discussed in class.
- **Ethical data handling (cf. Module 3):** Identification of all ethical, legal, or policy constraints and how they were addressed. This includes issues related to consent, privacy/confidentiality, copyright, licenses, and terms of use.
- **Data quality (cf. Module 10):** Document data quality assessment results.
- **Data cleaning (cf. Modules 11–12):** Describe any data cleaning methods applied (e.g., missing values, outliers, syntactic or semantic cleaning).
- Work on interim status report and submit it.
- **Workflow automation and provenance (cf. Module 13):** Provide an automated end-to-end workflow.
- **Metadata and data documentation (cf. Module 15):** Metadata and data documentation to support discovery, understandability, and reuse.
- Work on putting together the final project and submitting.

#### Sonia Alimchandani
- **Files storage and organization (cf. Module 2):** Select and describe what kind of files and data types you are working with. Describe a specific storage and organization strategy. This may include use of tabular, relational, or semi-structured models. Describe the specific organization strategy you are using.
- **Data collection and acquisition (cf. Module 4):** Collection or acquisition of at least 2 different datasets from trustworthy sources. Selected datasets should either have different access methods (e.g., APIs) or formats/schemas.
- **Extraction and enrichment (optional, cf. Module 5).**
- **Data integration (cf. Modules 7–8):** Integration of datasets (Python/Pandas or SQL).
- **Data cleaning (cf. Modules 11–12):** Describe any data cleaning methods applied (e.g., missing values, outliers, syntactic or semantic cleaning).
- Work on interim status report and submit it.
- **Workflow automation and provenance (cf. Module 13):** Provide an automated end-to-end workflow.
- **Reproducibility and provenance (cf. Module 14):** Your project must provide sufficient information to allow someone else to reproduce your workflow and analysis.
- Work on putting together the final project and submitting.


### Research/Business Question(s)

How has monitoring energy use and posting public placards on buildings affected energy efficiency in large Chicago buildings?

Are there property types or neighborhoods that were more likely to improve energy efficiency scores?

What types of properties had better energy usage in the first place?

Is there an association between energy rating and the number of environmental complaints?


### Datasets

Our project uses datasets from the Chicago Energy Benchmarking Data, which report annual energy performance metrics for large buildings in Chicago. These datasets include information such as ENERGY STAR scores, Energy Use Intensity (EUI), greenhouse gas emissions, water use, building characteristics, and Chicago Energy Ratings. The data is on buildings larger than 50,000 square-feet and it tracks full-building energy use.

Each dataset represents the energy usage for a specific year but is released the following year after reporting and validation. The datasets used in this project include:

- 2021 data (reported in 2023)
- 2022 data (reported in 2023)
- 2023 data (reported in 2024)
- CDPH Environmental Complaints


Combining these datasets allows us to analyze multi-year trends in building energy performance and track changes across building types and neighborhoods.


### Timeline
Project Plan Deadline: Thursday March 12 @ 11:59 PM

Interim Status Report Deadline: March 31

Final Project Submission: May 3

| Week | Tasks |
|-----|------|
| **March 22–28** | Data lifecycle (cf. Module 1): Relate your project to one or more of the lifecycle models discussed in class.<br><br>Files storage and organization (cf. Module 2): Select and describe what kind of files and data types you are working with. Describe a specific storage and organization strategy. This may include use of tabular, relational, or semi-structured models. Describe the specific organization strategy you are using.<br><br>Ethical data handling (cf. Module 3): Identification of all ethical, legal, or policy constraints and how they were addressed. This includes issues related to consent, privacy/confidentiality, copyright, licenses, and terms of use.<br><br>Data collection and acquisition (cf. Module 4): Collection or acquisition of at least 2 different datasets from trustworthy sources. Selected datasets should either have different access methods (e.g., APIs) or formats/schemas.<br><br>Extraction and enrichment (optional, cf. Module 5).<br><br>Data integration (cf. Modules 7–8): Integration of datasets (Python/Pandas or SQL).<br><br>Data quality (cf. Module 10): Document data quality assessment results. |
| **March 29–April 4** | Data cleaning (cf. Modules 11–12): Describe any data cleaning methods applied (e.g., missing values, outliers, syntactic or semantic cleaning).<br><br>Work on interim status report and submit it. |
| **April 5–11** | Workflow automation and provenance (cf. Module 13): Provide an automated end-to-end workflow. |
| **April 12–18** | Workflow automation and provenance (cf. Module 13): Provide an automated end-to-end workflow. |
| **April 19–25** | Reproducibility and provenance (cf. Module 14): Your project must provide sufficient information to allow someone else to reproduce your workflow and analysis.<br><br>Metadata and data documentation (cf. Module 15): Metadata and data documentation to support discovery, understandability, and reuse. |
| **April 26–May 3** | Work on putting together the final project and submitting. |

### Constraints

We anticipate there to be some challenges and constraints when working with the data for this project. There may be inconsistent schemas between the datasets, and we will have to ensure that we can accurately match up variables and/or observations that represent the same things. Also, we are contrained based on the information reported by the city ordinance and cannot see how external forces and factors may be affecting building energy efficiencies. 

In terms of ethical constraints, we do not want to damage the image or reputation of the buildings that we are analyzing if they have low energy scores. If certain neighborhoods have a majority of buildings, we also don't want to create stereotypes or negative connotations connected to them. Our goal is to make observations and turn them into insights about Chicago buildings and the effect of publicly displayed energy score placards, not influence reputations.



### Gaps

After beginning analysis on the year by year Chicago Energy Benchmark Report datasets, we have determined some gaps that may be present in the data. Since the Chicago Energy Rating System began in 2019, there is not extensive history on the energy efficiency of these buildings. This will make it difficult to determine trends and changes over the years. Making a building more energy efficient could be costly and timely, so even if there are changes being put into place for buildings, the actions taken may not be shown in their numbers yet. 

Additionally, some buildings have been able to receive exemptions from receiving an energy score. Without information on exempt buildings, the data for those property types and neighborhoods could be scewed. We will need to clean the datasets potentially dropping rows or columns if they do not containt consistent information. 

Another gap in our information is that we only have information on the primary property type of each building. We don't know how many companies may be operating in the same buildings. It also would be informative to know if occupancy and usage rates of buildings have changed. For example, the COVID-19 pandemic led to many people in Chicago working from home instead of office buildings, did this social change affect Chicago building energy usage disproportionately?

There are areas and topics of this project that we would like more information on that we do not have from the datasets. Additional research may be necessary in order to draw more confident insights in our analysis.
