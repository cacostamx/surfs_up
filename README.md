# Surfs Up Analysis

## Overview

The purpose of this analysis is to have a better undestanding of the weather in the island of Oahu, Hawaii.  After performing some analysis for the whole year weather, we are analyzing the months of June and December, in order to determine if the surf and ice cream shop business is sustainable year-round.

For this we made some queries to the weather database to extract the information by the months of study, convert the results to lists and then to dataframes in order to obtain the statistics.

### Resources

- Data source: Analysis was performed in the SQLite database 'hawaii.sqlite'.

- Software use to perform the analysis: Python 3.7.11, Anacoda 4.11, Jupyter Notebook 6.4.6


## Results

- ***Statistics comparison***. Although the temperature differencies are not big, we found the following:
    - The count of data is less for December than June's.  This could be attributed to some weather stations not working.
    - The mean temperature is almost 4° F lower in December than in June.
    - Although maximum temperatures seem around the same levels, minimum temperatures have a significant difference of 8° F, with December reaching really low temperatures for Hawaii.
    - Standard deviation seems a little higher for December, maybe due to the observations difference.

        |**June Statistics**                     |**December Statistics**                    |
        |:--------------------------------------:|:-----------------------------------------:|
        |![June Stats](/Resources/june_stats.png)|![December Stats](/Resources/dec_stats.png)|


### Additional graphs and findings

- ***Histogram comparison***.  When looking at the histogram we can see that December has less spread around the mean temperature, whereas June does show a wider spread around the mean. This would suggest that temperature in June is a little more fluctuating.

        |**June Temp Histogram**                    |**December Temp Histogram**                   |
        |:-----------------------------------------:|:--------------------------------------------:|
        |![June Histogram](/Resources/hist_june.png)|![December Histogram](/Resources/hist_dec.png)|


- ***Distribution and outliers***. Box plots show that both months have some outliers, but December has more. Also it is more evident that June temperature is around 73° and 77° F, whereas December's is around 69° and 74° F.

        |**June Box Plot**                       |**December Box Plot**                      |
        |:--------------------------------------:|:-----------------------------------------:|
        |![June Boxplot](/Resources/box_june.png)|![December Boxplot](/Resources/box_dec.png)|

## Summary

- It seems from this analysis that Oahu's temperature in June and December varies little and stays warm enough in December to keep the surf visitors coming and having and ice cream shop open all year-round.  Of course, there are some outliers in December suggesting that in some years, extreme weather could  also affect the island and could affect business. In the same token, there are also outliers, for both months, towards higher temperatures which are good for the shop.

### Further queries

- With the information provided a query regarding precipation could be useful to determine if there are other weather conditions that could affect tourism in both months and hence the business.

- Since there was a noticeable decrease in the number of observations for December, a query to determine the number of observations per station in each month could bring additional information as to determine station measurement reliability.