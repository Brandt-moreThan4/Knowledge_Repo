<!-- ```{r setup, include=FALSE} -->
<!-- # knitr::opts_chunk$set(echo = FALSE,message = FALSE, warning = FALSE) -->
<!-- ``` -->

Most of this is stolen from my former professor’s book:

[Data Science in R: A Gentle
Introduction](Data%20Science%20in%20R:%20A%20Gentle%20Introduction)

-   *James Scott*

## Linear Regression

Linear regression and plot, using only base R

``` r
# Load one of R's built-in data sets about cars
data(mtcars)

# Fit a straight line for mpg vs hp and plot the result.

mpg_model = lm(mpg ~ hp, data=mtcars) # Fit Linera Model
plot(mtcars$hp, mtcars$mpg) # Plot Linear Model
abline(mpg_model) # Draw the best fit line
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-2-1.png)

``` r
print(coef(mpg_model)) # Print the coefficients to command line
```

    ## (Intercept)          hp 
    ## 30.09886054 -0.06822828

## Reading Data & Simple Statistics

``` r
str(tv_df) # Basic dataframe info  
```

    ## 'data.frame':    40 obs. of  6 variables:
    ##  $ Show    : chr  "Living with Ed" "Monarch Cove" "Top Chef" "Iron Chef America" ...
    ##  $ Network : chr  "HGTV" "LIFE" "BRAVO" "FOOD" ...
    ##  $ PE      : num  54 64.6 78.6 62.6 56 ...
    ##  $ GRP     : num  151 375.5 808.5 17.3 44.1 ...
    ##  $ Genre   : chr  "Reality" "Drama/Adventure" "Reality" "Reality" ...
    ##  $ Duration: int  30 60 60 30 60 60 60 30 30 30 ...

``` r
head(tv_df) # View the first 6 rows
```

    ##                                 Show Network      PE   GRP           Genre
    ## 1                     Living with Ed    HGTV 54.0000 151.0         Reality
    ## 2                       Monarch Cove    LIFE 64.6479 375.5 Drama/Adventure
    ## 3                           Top Chef   BRAVO 78.5980 808.5         Reality
    ## 4                  Iron Chef America    FOOD 62.5703  17.3         Reality
    ## 5          Trading Spaces: All Stars     TLC 56.0000  44.1         Reality
    ## 6 Lisa Williams: Life Among the Dead    LIFE 56.2056 382.6         Reality
    ##   Duration
    ## 1       30
    ## 2       60
    ## 3       60
    ## 4       30
    ## 5       60
    ## 6       60

### Simple Analysis

``` r
xtabs(~Genre + Duration, data=tv_df) # Cross tabulate the data
```

    ##                   Duration
    ## Genre              30 60
    ##   Drama/Adventure   0 19
    ##   Reality           9  8
    ##   Situation Comedy  4  0

``` r
# Get the Average audience size  by genre
tv_df %>% group_by(Genre) %>% summarise(mean_GRP = mean(GRP))
```

    ## # A tibble: 3 x 2
    ##   Genre            mean_GRP
    ##   <chr>               <dbl>
    ## 1 Drama/Adventure     1243.
    ## 2 Reality              401.
    ## 3 Situation Comedy     631.

``` r
# Plot engagement by genre
ggplot(tv_df) + geom_point(aes(x=GRP,y=PE,color=Genre))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-5-1.png)

### ACL dataset

``` r
acl_df = read.csv('data/aclfest.csv', header=TRUE)
str(acl_df)
```

    ## 'data.frame':    1238 obs. of  7 variables:
    ##  $ band        : chr  "ALO" "Battles" "Bon Iver" "Flogging Molly" ...
    ##  $ acl         : int  0 0 0 0 0 0 0 0 0 0 ...
    ##  $ bonnaroo    : int  0 1 0 0 0 0 0 1 1 0 ...
    ##  $ coachella   : int  0 1 0 1 0 0 1 0 0 0 ...
    ##  $ lollapalooza: int  0 1 0 1 0 1 0 0 0 0 ...
    ##  $ outsidelands: int  1 0 1 0 1 1 0 0 0 1 ...
    ##  $ year        : int  2008 2008 2008 2008 2008 2008 2008 2008 2008 2008 ...

``` r
head(acl_df)
```

    ##                          band acl bonnaroo coachella lollapalooza outsidelands
    ## 1                         ALO   0        0         0            0            1
    ## 2                     Battles   0        1         1            1            0
    ## 3                    Bon Iver   0        0         0            0            1
    ## 4              Flogging Molly   0        0         1            1            0
    ## 5 Ivan Neville's Dumpstaphunk   0        0         0            0            1
    ## 6                   Radiohead   0        0         0            1            1
    ##   year
    ## 1 2008
    ## 2 2008
    ## 3 2008
    ## 4 2008
    ## 5 2008
    ## 6 2008

``` r
# How many bands played at lallapalooza
palooza_counts = xtabs(~lollapalooza, data=acl_df)
print(palooza_counts)
```

    ## lollapalooza
    ##   0   1 
    ## 800 438

``` r
palooza_proportions = prop.table(palooza_counts)
palooza_proportions
```

    ## lollapalooza
    ##         0         1 
    ## 0.6462036 0.3537964

``` r
# Same as above but with piping
xtabs(~lollapalooza,data=acl_df) %>% prop.table %>% round(3)
```

    ## lollapalooza
    ##     0     1 
    ## 0.646 0.354

``` r
# Joint probs of acl and lolla
xtabs(~acl + lollapalooza, data=acl_df)
```

    ##    lollapalooza
    ## acl   0   1
    ##   0 719 361
    ##   1  81  77

``` r
xtabs(~acl + lollapalooza, data=acl_df) %>% prop.table %>%  round(3)
```

    ##    lollapalooza
    ## acl     0     1
    ##   0 0.581 0.292
    ##   1 0.065 0.062

``` r
# Or probability of playing at Bonnaroo or Coachella
 # Add margins, just adds the total rows
xtabs(~bonnaroo + coachella, data=acl_df) %>%
  prop.table %>%
  addmargins
```

    ##         coachella
    ## bonnaroo          0          1        Sum
    ##      0   0.33925687 0.40064620 0.73990307
    ##      1   0.21486268 0.04523425 0.26009693
    ##      Sum 0.55411955 0.44588045 1.00000000

## Plotting

Keep this in mind for plotting:

1.  Scatter plots, to show relationships among numerical variables.
2.  Line graphs, to show change over time.
3.  Histograms, to show data distributions.
4.  Boxplots, to show between-group and within-group variation.
5.  Bar plots, to show summary statistics (like counts, means, or
    proportions).

Use faceting and aesthetic variation (e.g. color) to encode multivariate
information.

For more in-depth guide, see:
<https://bookdown.org/jgscott/DSGI/plots.html>

``` r
tvshows = read.csv('data/tvshows.csv', header=TRUE)
# head(tvshows)
power_christmas2015 = read.csv('data/power_christmas2015.csv', header=TRUE)
# head(power_christmas2015)
rapidcity = read.csv('data/rapidcity.csv', header=TRUE)
# head(rapidcity)
kroger = read.csv('data/kroger.csv', header=TRUE)
# head(kroger)
car_class_summaries = read.csv('data/car_class_summaries.csv', header=TRUE)
# head(car_class_summaries)




# Scatter Plot with shape as a facet
ggplot(tvshows) + 
  geom_point(aes(x=GRP, y=PE, shape=Genre))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-1.png)

``` r
# Scatter Plot with size as a facet. 
# This makes more sense to do on a quantitative variable though.
ggplot(tvshows) + 
  geom_point(aes(x=GRP, y=PE, size=Genre))
```

    ## Warning: Using size for a discrete variable is not advised.

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-2.png)

``` r
# Facet plot by different genre
ggplot(tvshows) + 
  geom_point(aes(x=GRP, y=PE)) + 
  facet_wrap(~Genre)
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-3.png)

``` r
# Line plot
ggplot(power_christmas2015) + 
  geom_line(aes(x=hour, y=ERCOT))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-4.png)

``` r
# Historgram
ggplot(rapidcity) + 
  geom_histogram(aes(x=Temp),bins=30)
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-5.png)

``` r
# Histogram faceted by month
ggplot(rapidcity) + 
  geom_histogram(aes(x=Temp), binwidth=3) + 
  facet_wrap(~Month)
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-6.png)

``` r
# Histogram with probabilities
ggplot(rapidcity) + 
  geom_histogram(aes(x=Temp, y=..density..), binwidth=3)
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-7.png)

``` r
# Boxplots, grouped by city
ggplot(kroger) + 
  geom_boxplot(aes(x = city, y = vol))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-8.png)

``` r
# Demand graph
ggplot(kroger) + 
  geom_point(aes(x = vol, y = price))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-9.png)

``` r
# Bar plot of summary stats

# Use geom_col when the data is already summarized
ggplot(car_class_summaries) + 
  geom_col(aes(x=class, y=average_cty))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-10.png)

``` r
# Use geom_bar when you need R to do the counting of the raw data
data(mpg) # read in the dataset
ggplot(mpg) + 
  geom_bar(aes(x=class))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-11.png)

``` r
# Adding better labels to plot and adjusting the font size

ggplot(kroger) + 
  geom_boxplot(aes(x = city, y = vol)) + 
  labs(x="Location of Kroger store",
       y="Weekly sales volume (packages sold)",
       title="Weekly cheese sales at 11 U.S. Kroger stores") + 
  theme(axis.text = element_text(size = 8)) 
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-7-12.png)

## Summarizing Data

``` r
#Calculate summary stats
rapidcity %>%
  summarize(avg_temp = mean(Temp),
            median_temp = median(Temp),
            sd_temp = sd(Temp),
            iqr_temp = IQR(Temp),
            min_temp = min(Temp),
            max_temp = max(Temp),
            q05_temp = quantile(Temp, 0.05),
            q95_temp = quantile(Temp, 0.95)) %>%
  round(1)
```

    ##   avg_temp median_temp sd_temp iqr_temp min_temp max_temp q05_temp q95_temp
    ## 1     47.3        47.6    20.1     30.7      -19     91.9     12.9     77.2

``` r
# Add a column to rapidcity to calculate the z score
rapidcity = rapidcity %>%
  mutate(z = (Temp - mean(Temp))/sd(Temp))

head(rapidcity)
```

    ##   Year Month Day Temp         z
    ## 1 1995     1   1 12.6 -1.729407
    ## 2 1995     1   2 19.9 -1.365390
    ## 3 1995     1   3  9.2 -1.898949
    ## 4 1995     1   4  6.2 -2.048544
    ## 5 1995     1   5 16.0 -1.559865
    ## 6 1995     1   6 17.8 -1.470107

## Data Wrangling with tidyverse

``` r
# Calculate summary statistic by group
rapidcity %>%
  group_by(Month) %>%
  summarize(avg_temp = mean(Temp),
            sd_temp = sd(Temp),
            q05_temp = quantile(Temp, 0.05),
            q95_temp = quantile(Temp, 0.95)) %>%
  
  round(1)
```

    ## # A tibble: 12 x 5
    ##    Month avg_temp sd_temp q05_temp q95_temp
    ##    <dbl>    <dbl>   <dbl>    <dbl>    <dbl>
    ##  1     1     24.4    13.5     -1.1     42.4
    ##  2     2     27.4    13        2.2     45.4
    ##  3     3     34.2    12.7      9       52.9
    ##  4     4     44.5     9.7     27.2     60  
    ##  5     5     54.3     8.3     41.1     68.8
    ##  6     6     64.3     7.7     52       77.6
    ##  7     7     73.7     6.6     62.5     85.1
    ##  8     8     71.9     6.1     60.6     82  
    ##  9     9     61.4     9.1     47.2     77.1
    ## 10    10     47.9     9.7     32.4     64  
    ## 11    11     35.1    11.5     14.7     52.6
    ## 12    12     25.7    12.4      1.1     42.3

``` r
rapidcity_summary = rapidcity %>%
  group_by(Month) %>%
  summarize(avg_temp = mean(Temp),
            prop_freeze = sum(Temp <= 32)/n())

rapidcity_summary
```

    ## # A tibble: 12 x 3
    ##    Month avg_temp prop_freeze
    ##    <int>    <dbl>       <dbl>
    ##  1     1     24.4     0.673  
    ##  2     2     27.4     0.589  
    ##  3     3     34.2     0.392  
    ##  4     4     44.5     0.0806 
    ##  5     5     54.3     0.00190
    ##  6     6     64.3     0      
    ##  7     7     73.7     0      
    ##  8     8     71.9     0      
    ##  9     9     61.4     0      
    ## 10    10     47.9     0.0495 
    ## 11    11     35.1     0.367  
    ## 12    12     25.7     0.642

``` r
# We need to add 'facto'r here because the plot expects x to be categorical
ggplot(rapidcity_summary) + 
  geom_col(aes(x=factor(Month), y=avg_temp))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-9-1.png)

``` r
ggplot(rapidcity_summary) + 
  geom_col(aes(x=factor(Month), y=prop_freeze))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-9-2.png)

``` r
# Filter data by year before computing summary statistics 
rapidcity %>%
  filter(Year >= 2006 & Year <= 2009) %>%
  group_by(Month) %>%
  summarize(avg_temp = mean(Temp),
            sd_temp = sd(Temp)) %>%
  round(1)
```

    ## # A tibble: 12 x 3
    ##    Month avg_temp sd_temp
    ##    <dbl>    <dbl>   <dbl>
    ##  1     1     27.4    12.6
    ##  2     2     25.3    12.4
    ##  3     3     36.2    11.9
    ##  4     4     44.2    11  
    ##  5     5     56.1     8.7
    ##  6     6     65.5     8.2
    ##  7     7     75.1     7.4
    ##  8     8     71.3     6.5
    ##  9     9     60.7     8.2
    ## 10    10     45.3     9.8
    ## 11    11     37.6    10.2
    ## 12    12     22      11.9

``` r
# Using 'select' allows you to pick out certain columns

head(rapidcity %>%
  filter(Year == 2009) %>%
  select(Month, Day, Temp))
```

    ##   Month Day Temp
    ## 1     1   1 30.7
    ## 2     1   2 20.3
    ## 3     1   3 16.9
    ## 4     1   4  8.0
    ## 5     1   5 13.9
    ## 6     1   6 28.2

``` r
#Alternatively, using a  negative sign will remove certain columns.
# Below achieves same result as above
head(rapidcity %>%
  filter(Year == 2009) %>%
  select(-Year,-z))
```

    ##   Month Day Temp
    ## 1     1   1 30.7
    ## 2     1   2 20.3
    ## 3     1   3 16.9
    ## 4     1   4  8.0
    ## 5     1   5 13.9
    ## 6     1   6 28.2

``` r
# Mutate allows you to add new variables from old ones
rapidcity_augmented = rapidcity %>%
  mutate(Summer = ifelse(Month == 6 | Month == 7 | Month == 8,
                         yes="summer", no="not_summer"))

head(rapidcity_augmented)
```

    ##   Year Month Day Temp         z     Summer
    ## 1 1995     1   1 12.6 -1.729407 not_summer
    ## 2 1995     1   2 19.9 -1.365390 not_summer
    ## 3 1995     1   3  9.2 -1.898949 not_summer
    ## 4 1995     1   4  6.2 -2.048544 not_summer
    ## 5 1995     1   5 16.0 -1.559865 not_summer
    ## 6 1995     1   6 17.8 -1.470107 not_summer

``` r
# Use arrange for sorting
head(rapidcity %>%
  arrange(Temp))
```

    ##   Year Month Day  Temp         z
    ## 1 1996     2   2 -19.0 -3.305149
    ## 2 2008    12  15 -12.2 -2.966065
    ## 3 1996     2   3 -11.8 -2.946119
    ## 4 2006     2  18 -11.5 -2.931160
    ## 5 1996     1  30 -11.0 -2.906227
    ## 6 1996    12  26 -10.8 -2.896254

``` r
# The default is ascending. We can change that:
head(rapidcity %>%
  arrange(desc(Temp)))
```

    ##   Year Month Day Temp        z
    ## 1 2007     7   7 91.9 2.224909
    ## 2 2006     7  16 90.7 2.165071
    ## 3 2006     7  30 89.8 2.120192
    ## 4 2007     7  23 89.5 2.105232
    ## 5 2007     7  24 89.5 2.105232
    ## 6 2002     6  29 89.4 2.100246

``` r
# Find the 5 coldest months
rapidcity %>%
  group_by(Year, Month) %>%
  summarize(avg_temp = mean(Temp),
            coldest_day = min(Temp),
            warmest_day = max(Temp)) %>%
  arrange(avg_temp) %>%
  head(5) %>%
  round(1)
```

    ## `summarise()` has grouped output by 'Year'. You can override using the `.groups` argument.

    ## # A tibble: 5 x 5
    ## # Groups:   Year [4]
    ##    Year Month avg_temp coldest_day warmest_day
    ##   <dbl> <dbl>    <dbl>       <dbl>       <dbl>
    ## 1  1996     1     14.9       -11          46.1
    ## 2  2009    12     16.4        -2.6        35.6
    ## 3  2000    12     17.3        -9          38.8
    ## 4  1996    12     17.5       -10.8        40.4
    ## 5  2001     2     17.6        -3.9        40.8

``` r
titanic = read.csv("data/titanic.csv") # Load in the titanic data set
head(titanic)
```

    ##                              name survived    sex     age passengerClass
    ## 1   Allen, Miss. Elisabeth Walton      yes female 29.0000            1st
    ## 2  Allison, Master. Hudson Trevor      yes   male  0.9167            1st
    ## 3    Allison, Miss. Helen Loraine       no female  2.0000            1st
    ## 4 Allison, Mr. Hudson Joshua Crei       no   male 30.0000            1st
    ## 5 Allison, Mrs. Hudson J C (Bessi       no female 25.0000            1st
    ## 6             Anderson, Mr. Harry      yes   male 48.0000            1st

``` r
# A bit more complex wranlging
surv_adults = titanic %>%
  mutate(age_bracket = ifelse(age >= 18,
                              yes="adult", no="child")) %>%
  filter(age_bracket == "adult") %>%
  group_by(sex, passengerClass) %>%
  summarize(total_count = n(),
            surv_count = sum(survived == 'yes'),
            surv_pct = surv_count/total_count)
```

    ## `summarise()` has grouped output by 'sex'. You can override using the `.groups` argument.

``` r
surv_adults
```

    ## # A tibble: 6 x 5
    ## # Groups:   sex [2]
    ##   sex    passengerClass total_count surv_count surv_pct
    ##   <chr>  <chr>                <int>      <int>    <dbl>
    ## 1 female 1st                    125        121   0.968 
    ## 2 female 2nd                     85         74   0.871 
    ## 3 female 3rd                    106         47   0.443 
    ## 4 male   1st                    144         47   0.326 
    ## 5 male   2nd                    143         12   0.0839
    ## 6 male   3rd                    289         45   0.156

``` r
ggplot(surv_adults) + 
  geom_col(aes(x=sex, y=surv_pct,fill=sex)) + 
  facet_wrap(~passengerClass, nrow=1)
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-9-3.png)

``` r
toyimports  = read.csv("data/toyimports.csv") # Load in the titanic data set
head(toyimports )
```

    ##   partner year         partner_name product                        product_name
    ## 1     ARE 1998 United Arab Emirates  950341 Toys representing animals or non-hu
    ## 2     ARE 2000 United Arab Emirates  950349 Toys representing animals or non-hu
    ## 3     ARE 2003 United Arab Emirates  950349 Toys representing animals or non-hu
    ## 4     ARE 2005 United Arab Emirates  950320 Reduced-size ("scale") model assemb
    ## 5     ARG 1996            Argentina  950341 Toys representing animals or non-hu
    ## 6     ARG 1996            Argentina  950310  Electric trains, including tracks,
    ##   US_report_import  pop2000 region
    ## 1            1.060  3247000      7
    ## 2           12.012  3247000      7
    ## 3            4.650  3247000      7
    ## 4           49.236  3247000      7
    ## 5            0.000 36895710      2
    ## 6           10.850 36895710      2

``` r
country_totals = toyimports %>%
  group_by(partner_name) %>%
  summarize(total_dollar_value = sum(US_report_import)) %>%
  arrange(desc(total_dollar_value))

country_totals
```

    ## # A tibble: 129 x 2
    ##    partner_name     total_dollar_value
    ##    <chr>                         <dbl>
    ##  1 China                     26842305.
    ##  2 Denmark                    1034990.
    ##  3 Canada                      572309.
    ##  4 Hong Kong, China            545186.
    ##  5 Switzerland                 400969.
    ##  6 Korea, Rep.                 350612.
    ##  7 Germany                     312891.
    ##  8 Japan                       253160.
    ##  9 Thailand                    226155.
    ## 10 Indonesia                   213807.
    ## # ... with 119 more rows

``` r
top3_partner_names = c('China', 'Denmark', 'Canada')


top3_byyear = toyimports %>%
  filter(partner_name %in% top3_partner_names) %>%
  group_by(year, partner_name) %>%
  summarize(yearly_dollar_value = sum(US_report_import))
```

    ## `summarise()` has grouped output by 'year'. You can override using the `.groups` argument.

``` r
ggplot(top3_byyear) +  
  geom_line(aes(x=year, y=yearly_dollar_value, color=partner_name)) +
  scale_color_brewer(type='qual') + 
  scale_y_log10() + 
  scale_x_continuous(breaks = 1996:2005) + 
  labs(x="Year", y = "Dollar value of imports (log scale)",
       title="Toy imports from the U.S.'s top-3 partners, 1996-2005")
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-9-4.png)

### Data Wrangle shortcuts

``` r
mean(~age,data=titanic) # Calcualte the mean
```

    ## [1] 29.88113

``` r
mean(age ~ sex, data=titanic) # Calcualte the mean by category
```

    ##   female     male 
    ## 28.68707 30.58523

``` r
prop(~survived, data=titanic) # Proportion of titanic survivors
```

    ##   prop_no 
    ## 0.5917782

``` r
favstats(age ~ sex, data=titanic) # combo of all the good stuff
```

    ##      sex    min Q1 median Q3 max     mean       sd   n missing
    ## 1 female 0.1667 19     27 38  76 28.68707 14.57700 388       0
    ## 2   male 0.3333 21     28 39  80 30.58523 14.28057 658       0

## Regression

``` r
heartrate = read.csv('data/heartrate.csv')
head(heartrate)
```

    ##   age hrmax
    ## 1  25   190
    ## 2  43   176
    ## 3  19   203
    ## 4  31   177
    ## 5  23   183
    ## 6  27   201

``` r
ggplot(heartrate) + 
  geom_point(aes(x=age, y=hrmax)) + 
  geom_smooth(aes(x=age, y=hrmax), method='lm')
```

    ## `geom_smooth()` using formula 'y ~ x'

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-1.png)

``` r
model_hr = lm(hrmax ~ age, data=heartrate)
coef(model_hr)
```

    ## (Intercept)         age 
    ## 207.9306683  -0.6878927

``` r
y_hats = predict(model_hr)

plot(y_hats,heartrate$hrmax)
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-2.png)

``` r
plot(heartrate$age,model_hr$residuals)
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-3.png)

``` r
ebola = read.csv('data/ebola.csv')
head(ebola)
```

    ##         Date Day GuinSus GuinDeath GuinLab LibSus LibDeath LibLab NigSus
    ## 1 2014-03-25   0      86        59       0      0        0      0      0
    ## 2 2014-03-26   1      86        60       1      0        0      0      0
    ## 3 2014-03-27   2     103        66       4      0        0      0      0
    ## 4 2014-03-31   6     112        70      24      0        0      0      0
    ## 5 2014-04-01   7     122        80      24      0        0      0      0
    ## 6 2014-04-02   8     127        83      35      0        0      0      0
    ##   NigDeath NigLab SLSus SLDeath SLLab SenSus SenDeath SenLab totalSus
    ## 1        0      0     0       0     0      0        0      0       86
    ## 2        0      0     0       0     0      0        0      0       86
    ## 3        0      0     0       0     0      0        0      0      103
    ## 4        0      0     0       0     0      0        0      0      112
    ## 5        0      0     0       0     0      0        0      0      122
    ## 6        0      0     0       0     0      0        0      0      127
    ##   totalDeath totalLab
    ## 1         59        0
    ## 2         60        1
    ## 3         66        4
    ## 4         70       24
    ## 5         80       24
    ## 6         83       35

``` r
# Looks exponential so lienar regression seems suspect at first
ggplot(ebola) + 
  geom_line(aes(x=Day, y = totalSus))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-4.png)

``` r
# But we can change the y var
# total cases over time: logarithm scale for y variable
ggplot(ebola) + 
  geom_line(aes(x=Day, y = log(totalSus)))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-5.png)

``` r
# this looks like something that could be fit with linear regression

# linear model for log(cases) versus time
lm_ebola = lm(log(totalSus) ~ Day, data=ebola)
coef(lm_ebola)
```

    ## (Intercept)         Day 
    ##  4.53843517  0.02157854

``` r
# total cases over time with reference line
ggplot(ebola) + 
   geom_line(aes(x=Day, y = log(totalSus))) + 
   geom_abline(intercept = 4.54, slope = 0.0216, color='red')
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-6.png)

``` r
# Power Law

animals = read.csv('data/animals.csv')
head(animals)
```

    ##             animal     body  brain
    ## 1 African elephant 6654.000 5712.0
    ## 2   Asian elephant 2547.000 4603.0
    ## 3              Cat    3.300   25.6
    ## 4       Chimpanzee   52.160  440.0
    ## 5       Chinchilla    0.425    6.4
    ## 6              Cow  465.000  423.0

``` r
# Hard to see any relationship at first because of dramtic scale difference
ggplot(animals) + 
  geom_point(aes(x=body, y=brain))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-7.png)

``` r
# But, taking the log of both variables helps squish everything together!
ggplot(animals) + 
  geom_point(aes(x=log(body), y=log(brain)))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-8.png)

``` r
# Eestimating demand function!

milk = read.csv('data/milk.csv')
head(milk)
```

    ##   price sales
    ## 1  3.48    15
    ## 2  3.12    11
    ## 3  2.95    21
    ## 4  2.68    30
    ## 5  3.62    11
    ## 6  4.32    11

``` r
# Based on the below plot, we can see a lienar relaitonship doesn't exactly make sense.

ggplot(milk) + geom_point(aes(x=price,y=sales))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-9.png)

``` r
# Probably a power law?
ggplot(milk) +
   geom_point(aes(x=log(price), y=log(sales)))
```

![](R_Basics_files/figure-markdown_github/unnamed-chunk-11-10.png)

``` r
# Oh yea. Now we can estimate that function
lm_milk = lm(log(sales) ~ log(price), data=milk)
coef(lm_milk)
```

    ## (Intercept)  log(price) 
    ##    4.720604   -1.618578
