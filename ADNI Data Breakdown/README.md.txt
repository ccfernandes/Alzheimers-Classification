Data Testing README


mergedData_MAIN.csv was achived using jupyter notebook scripts 
 - merged datasets 
 - no normalization via script (only manually for imaging data)


Preprocessing from merged Data to get mergedData_MAIN:
 - Deleted SMC
 - created ICV ratios for Cerebrum, total_hippo, total_csf, ventricles, entorhinal using ICV
 - Removed ICV ratio that was infinite #DIV/0! (note: 0 values are still there)
 - ABETA >1700 and <200 values were changed to 1700 and 200 respectively 
 - Changed LMCI and EMCI to MCI (aka. merged LMCI and EMCI into one class)
 - Removed ICV column from data (once ratio calculation was complete)

Notes: 
- we will need to conduct a test to see which features make a significant impact on accuracy -> subtraction method
	- iteratively remove one feature at a time 
	- run set through model and note change in accuracy
- MCI negatively impacts accuracy results (78% with vs 98% without)

(Remember to take in ICV in front end model to do the ratio calculation)
