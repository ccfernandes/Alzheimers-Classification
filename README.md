# Alzheimers-Classification

Repository for Santa Clara University Senior Design Project 2020-2021

Contributors: Chelsea Fernandes, Aiyushi Kumar, Shreya Venkatesh

## Data Preprocessing

Our data is being sourced from ADNI, from which we preprocess the raw data to feed into our model. 

The following preprocessing was completed:
* Averaging of cognitive test data (Convert_Ecog_Test_Values.ipynb)
* Merging of various csv files (adni_merge_data.ipynb)
* Normalization of merged data (normalize_data_3.ipynb)

## Data Analysis 

To determine which features to remove from our dataset, the following was completed:
* Plotted histograms (Histogram_plot_grp_1.ipynb)
* Plotted boxplots for each feature (boxplots.uptnb)
* k-fold cross validation (kfold_crossvalidation.ipynb)

![histo_git](https://user-images.githubusercontent.com/37026923/134597137-8f34dc5c-16d0-43cd-953e-572dca2e0e11.png)

In the histograms, overlapping peaks of the three classes indicate that the feature has no discriminatory values between the classes (NOT good for a classification problem). For example, the histogram on the left has minimally overlapping peaks and shows the RAVLT cognitive test can be used as a feature to separate the three classes. On the other hand, the histogram on the right completely overlaps the three classes showing that the Cerebrum values are not ideal for separating the classes.

![boxplot_git](https://user-images.githubusercontent.com/37026923/134597219-506148ec-4cf8-40c8-bb06-d048aa1828ba.png)

A similar thought-process was done when analyzing the boxplot corresponding to each feature. The features that display less overlap in data between the 3 classes tend to be more sensitive to distinguishing the classes apart from one another.

## Website and Results

For our final model, we decided to implement a random forest multiclass-classification model. The feature contribution is conveyed through the pie chart below. The features MMSE and FAQ_TOTAL contributed most to the overall classification, which aligns with the scientific data regarding commons methods of diagnosing Alzheimer's Disease patients. 
![feature_contrib](https://user-images.githubusercontent.com/37026923/134597477-70d17360-28c4-4bbf-ae51-9668a771819b.png)

Below is an example of the pie chart that is displayed to the user defining the predicted classification based on inputted data. 
![website_output](https://user-images.githubusercontent.com/37026923/134597375-4bfacd4c-a466-4ee4-bb23-e179fbcaf1dd.png)

