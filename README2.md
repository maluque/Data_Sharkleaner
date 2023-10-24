![shark](images/shark_pic.jpg)


# Data_Sharkleaner
A pandas project to clean a shark attack database (kaggle)


# INDEX:

## 1. Set working directory, load modules and set global ipynb properties

## 2. Load raw data frame

## 3. Explore basic properties

## 4. Cleaning steps

### 4.0 Remame columns if neccessary

I replaced the column name "se" for "sex"

### 4.1 NA'S per row - drop rows with 100% of NA's

### 4.2 Check and drop duplicated rows


### Investigate the columns by their unique_count/freq ratio

Top rows: indicate there are MANY LEVELS with very LOW FREQ:

 * 'case_number' should be an identifier and not present duplicated values!!!

 * That behavior is expected for 'case_number' and 'date' data types
     
 * According to wikipedia, there only exists 195 countries in the world
    but this column contains 212 unique values!!!!
    Check in the next cell bellow.
         
 * Same suspicion wiht "species" or "activity"
 
         
Bottom rows: indicate there is ONE LEVEL with EXCESIVE FREQ:

 * "unnamed_22" and "unnamed_23" should be deleted in a real job task
    
 * "case_number_1" and "case_number_2" should also be deleted cause they seem copies of "case_number"
   
 * For the moment, I will also ignore "href" and "href_formula" cause they seems uninformative links

 ### 4.3 Investigate the relationship between: "case_number", "case_number_1",  "case_number_2" and "original_order" 

 ### 4.4 Correct "date" column

* 4.4.1 Remove "Reported"
* 4.4.2 Transform to "uncertain" the cells including the following keywords:
    "Before" or "No date", " or ", "A.D"
* 4.4.3 Clean terms as Ca.


Drop "uncertain" values 

Keep it on-hold and continue cleaning other columns

### 4.5 Correct "type" column

* 4.5.1 Unify the following keywords: Boating == Boat == Boatomg

* 4.5.2 Transform to uncertain's the cells including the following keywords: 
    Questionable, Invalid


Drop uncertain values

Keep it on-hold and continue cleaning other columns

### 4.6 Correct "country" column

* 4.6.1 Clean when the name start with spaces

* 4.6.2 Transform to uncertain cells including "/", "?"


Drop records referring to countries mentioned less than 20 times since 
these could noy be statistically compared against anything

Drop "uncertain" and "nan" values

Keep it on-hold and continue cleaning other columns

### 4.7 Correct "age" column


* 4.7.1  Drop NAN's

* 4.7.2 Transform to "uncertain" the cells including NON DIGIT"

* 4.7.3 Drop "uncertain" values 

Keep it on-hold and continue cleaning other columns


### 4.8 Correct "fatal_y_n" column


* 4.8.1 Transform to "UNKNOWN" the cells = " N", "M" and "2017"

* 4.8.2 Drop "UNKNOWN" values 

Keep it on-hold and continue cleaning other columns


<span style="font-size:18px; color: #e74c3c"><b> AT THIS POINT I HAVE A RELATIVELY CLEAN DATAFRAME WITH: 2869 rows and 24 columns!!
    
LAST CLEANING PROCESSES WITHOUT DROPING ROWS:

* 4.9 Clean misspelled SEX column
    
* 4.10 Transform to " " long ACTIVITY descriptions (i.e., > word by cell)
    
* 4.11 Clean "time" column by replacing "h" for nothing and keeping only values with 4 digits 
  
* 4.12 Clean "injury" column to keep only the top 5 types of lessions
    
    
I WILL IGNORE THE FOLLOWING COLUMNS:
Reason: too dirty or uninformative
   
    time 	specie 	investigator_or_source 	pdf 	href_formula 	href
    
    
TO CONCLUDE I WILL:
    
* 4.13 Transform redundant columns into constant NA columns
    
        case_number case_number_1 case_number_2 unnamed_22 unnamed_23

* 4.14 Change NANs to zeroes those columns that I would prefer to cast as numeric
    
* 4.15 Downcast the dataframe to decrease memory use
    
    
* Save this file as first task ---> data/sharks_clean1.csv

### 4.9 Clean misspelled SEX column

### 4.10 Clean long ACTIVITY descriptions (i.e., > word by cell)

### 4.11 Clean "time" column 

### 4.12 Clean "injury" column to keep only the top 5 types of lessions

### 4.13 Transform redundant columns into constant NA columns

### Last check on NA's distribution

### 4.14 Change NANs to zeroes those columns that I would prefer to cast as numeric

### 4.15 Downcast the dataframe to decrease memory use

### 5 Data Analysis


Previous to the analysis itself:

* I will filter only the relevant columns

* Transform sex and fatal_y_n to "binary" (0/1) columns

* To define a simple analysis with enought statistical power, I will focus on columns with few levels with high frequency

* get_dummy variables from categorical columns

Exemplary analyses:

* a) Top 20 deadliest countries
* b) Correlation


### a) Top 20 deadliest countries

Countries with highest fatality ratio

As expected when dealing with statistical analysis, the ratio is high in countries with low sample size

However, it serves as example

### b1) Correlation between quantitative and/or binary variables

### b2) Correlation between dummy variables