# MLOPS_Assignment
Name : Anindita Das
GitHub_Link : https://https://github.com/Anindita2019/MLOPS_Assignment/
Date: 19/04/2023

# Project Name : MLOPS_Assignment
> Problem statement: 1. Go to the Assignment/03_inference_pipeline/scripts folder.  

2. First we will break down all the model inference tasks into functions in the utils.py file you have been provided with functions level breakdown of all the tasks. We will basically need 2 
Functions for inference. The first function will encode the features and the second function will generate models prediction on the data and write it to the db. On top of this we will also do some sanity checks.


You can copy the encode_data function that you used in the training pipeline but there will be some modification. Recall that in the encode_data function that you used, you had to save the output columns as a list. In case of training this includes “app_complete_flag” which is available to us during training  but  will not have that inference so you modify the encode_data function accordingly.
    

3. Once you have written the code into the respective functions. You will modify the function to read their input data and write their output to the database present in file 'lead_scoring_data_cleaning.db'. The function will be executed in the following order so make sure to read the input for the functions appropriately

encode_data -> input_features_check -> load_model -> prediction_col_check
Ensure that you are reading and writing from the appropriate tables in the db.

 

NOTE: We need to clean our inference data before we can use it to get models inference. Thus we will run the data pipeline on the raw inference data and use the cleaned data for inference. Thus our encode_feature will read the input from data pipeline’s output which is present in the ‘lead_scoring_data_cleaning.db’ file.  Also note that since we are not creating any db here we do not require build_db function

4. Once you have coded the functions, create a notebook and import utils file in it and run all the functions in the proper order. This will help you debug your code.

NOTE : Before you run the get_model_prediction function ensure that you have run mlflow server command from the terminal at the appropriate path. Also ensure that you have promoted the registered model to promotion before running get_models_prediction function as this function loads model which is in production stage(“Lead_scoring_mlflow_production”)
NOTE : In order to promote a registered model to production go to "Models" tab . Click on the registered model and go to "Stage" drop down menu and select "Production". This way you can promote a registered model to production stage in MLflow.

5. Once you have ensured that the functions in utils.py file are working as intended, store all the constant values in constants.py and repeat step 3 to ensure that the code is working properly
6. Now create a pipeline using airflow in the 'lead_scoring_inference_pipeline.py'. Follow the instructions present in the file for creating the dag for airflow.
7. Now go to the '~/airflow/dags/' folder and create a folder named 'Lead_scoring_inference_pipeline' in it and copy paste the following files in it.The following file should be present in Lead_scoring_inference_pipeline folder

├── lead_scoring_inference_pipeline.py
├── constants.py
└── utils.py
8. After copying all the necessary files and folder from 'scripts' folder to 'Lead_scoring_inference_pipeline' and modify your constants, utils and lead_scoring_inference_pipeline.py as the paths have been changed when you have changed the directory. Make changes in the file path names in constants.py file.
9. With this you should be able to run the inference pipeline. Follow the instructions mentioned in the Airflow module to run the inference pipeline and take the screenshot of Airflow UI for submission.
10. Manually trigger the inference pipeline and see if we are getting the expected results.
11. Now copy the “leadscoring_inference.csv” file present in “Assignment/03_inference_pipeline/Data” to the “airflow/dags/Lead_scoring_data_pipeline/data” folder and modify the constants.py in the Lead_scoring_data_pipeline such that the data pipeline read “leadscoring_inference.csv” instead of “leadscoring.csv”. 

NOTE: “leadscoring_inference.csv” is our inference dataset and it does not contain “app_complete_flag”.  
NOTE: We need to clean our inference data before we can use it to get models inference. Thus we will run the data pipeline on the raw inference data and use the cleaned data for inference.

12. Once this is done first trigger the Data pipeline manually and then trigger the inference pipeline once the data pipeline’s run is complete. Revise till you get the expected output. Follow the instructions mentioned in the Airflow module to run the Inference pipeline and take the screenshot of Airflow UI for submission. Trigger the training pipeline manually.
13. Please find the grading rubrics and deliverables in these link. Please make sure you follow all the steps mentioned above.
14. Pat yourself on the back as you have completed the assignment.




