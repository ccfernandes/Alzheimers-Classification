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
