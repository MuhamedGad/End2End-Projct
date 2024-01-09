import mlflow
import mlflow.sklearn
import os
import pickle
import yaml
import pandas as pd
import numpy as np

def model (sample_skills, target_class)  :
    
    DF = r'..\data\processed\clusters_skills_df.pkl'
    CLUSTERS_SKILLS = r'..\data\processed\clusters_skills.yaml'
    MLFLOW_TRACKING_URI = '..\models/mlruns'
    MLFLOW_EXPERIMENT_NAME = "rf_job_predict"
    EXPERIMENT_ID = 'c410d8ab2d42489ba0b8738b000d13e5'
    ARTIFACT_PATH = '..\models/MODELS'
    

    
    df = pd.read_pickle(DF)
    x = df.droplevel(0, axis=1)
    x =x.iloc[:,25:]
    
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    
    target_path = ARTIFACT_PATH + '/' + EXPERIMENT_ID + '/artifacts'
    
    # Get a list of folders in the specified path
    folders = [entry.name for entry in os.scandir(target_path) if entry.is_dir()]
    
    # Print the list of folders
    
    
    target_path += '/' + folders[0]+ '/model.pkl'
    
    
    with open(target_path, 'rb') as file:
        loaded_model = pickle.load(file)
    
    
    
    with open(CLUSTERS_SKILLS, 'r') as file :
        clusters_skills = yaml.load(file, Loader=yaml.FullLoader)
        
    del clusters_skills['skills_group_8']
    
    

    target_score = 0
    
    test = pd.DataFrame(columns=list(clusters_skills.keys()) + x.columns.to_list())
    test.loc[0] = 0
    
    
    for cluster, skills in clusters_skills.items() :
        for skill in skills :
            if skill in sample_skills:
                test[cluster] +=1
    
    
    for skill in sample_skills :
        if skill in test.columns.tolist() :
            test[skill] += 1
    
    

    
    class_names = loaded_model.classes_

    
    predictions = loaded_model.predict_proba(test)
    
    for class_name, probability in zip(class_names, predictions[0]):  # Assuming predictions has shape (1, n_classes)
        
        if class_name == target_class :
            target_score = probability
            
    sorted_classes = sorted(zip(class_names, predictions[0]), key=lambda x: x[1], reverse=True)


    
    idx = np.argmax(predictions)
    class_names[idx]
    
    
    
    d = {}
    
    others = []
    for skill in x.columns.tolist() :
        if skill not in sample_skills:
            others.append(skill)
    
    
    
    
    for skill in others :
        new = test.copy()
        for cluster, skills in clusters_skills.items() :
            if skill in skills:
                new[cluster] +=1
        predictions = loaded_model.predict_proba(new)
        target_class_index = list(class_names).index(target_class)
        target_class_score = predictions[0][target_class_index]
        target_class_score = (target_class_score - target_score) / (target_score+0.0001)
        d[skill] = target_class_score
        
    
    
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    
    
    
    
    threshold = 1
    suggestions =  [key for key, value in sorted_items[:5] if value>threshold]

#    for key, value in sorted_items:
 #       if value > threshold:
  #          suggestions.append(key)
        
        
    return suggestions, sorted_classes 
    
    
    

    
    
if __name__ == '__main__':
    sample = ['Python', 'PostgreSQL',  'Flask', 'Keras']
    role = 'Data or business analyst'
    x, y = model (sample, role)
    print (x)
    
    
    
    
    
    
    
