import pandas as pd
import streamlit as st
import pickle as pk


model = pk.load(open('gdc.pkl', 'rb'))


st.header('Accident Severity Predictor')


st.markdown(" Safety on the Road, Safe Way to Go!")

#mapping categorical values to human readable values
day_of_week_mapping = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
age_band_mapping = {'Under 18': 1, '18-30': 2, '31-50': 3, 'Over 51': 4, 'Unknown': 5}
sex_mapping = {'Male': 0, 'Female': 1, 'Unknown': 2}
educational_level_mapping = {'Illiterate': 1, 'Elementary school': 2, 'Junior high school': 3, 'High school': 4, 'Above high school': 5, 'Writing & reading': 6, 'Unknown': 7}
vehicle_driver_relation_mapping = {'Owner': 0, 'Employee': 1, 'Unknown': 2, 'Other': 3}
driving_experience_mapping = {'No Licence': 1, 'Below 1yr': 2, '1-2yr': 3, '2-5yr': 4, '5-10yr': 5, 'Above 10yr': 6, 'Unknown': 7}
type_of_vehicle_mapping = {'Automobile': 1, 'Public (> 45 seats)': 2, 'Lorry (41-100Q)': 3, 'Public (13-45 seats)': 4, 'Motorcycle': 5, 'Other': 6}
owner_of_vehicle_mapping = {'Owner': 0, 'Governmental': 1, 'Organization': 2, 'Other': 3, 'Unknown': 4}
service_year_mapping = {'Below 1yr': 1, '1-2yr': 2, '2-5yrs': 3, '5-10yrs': 4, 'Above 10yr': 5, 'Unknown': 6}
defect_of_vehicle_mapping = {'No defect': 0, 'Defect Present': 1}
area_accident_mapping = {'Residential areas': 1, 'Office areas': 2, 'Market areas': 3, 'Rural village areas': 4, 'Unknown': 5}
lanes_or_medians_mapping = {'Undivided Two way': 1, 'Double carriageway': 2, 'One way': 3, 'Unknown': 4}
road_alignment_mapping = {'Tangent road with flat terrain': 1, 'Escarpments': 2, 'Sharp reverse curve': 3, 'Unknown': 4}
types_of_junction_mapping = {'No junction': 1, 'T Shape': 2, 'Crossing': 3, 'Unknown': 4}
road_surface_type_mapping = {'Asphalt roads': 1, 'Gravel roads': 2, 'Other': 3, 'Unknown': 4}
road_surface_conditions_mapping = {'Dry': 1, 'Wet or damp': 2, 'Snow': 3, 'Flood over 3cm. deep': 4}
light_conditions_mapping = {'Daylight': 1, 'Darkness - lights lit': 2, 'Darkness - no lighting': 3, 'Unknown': 4}
weather_conditions_mapping = {'Normal': 1, 'Raining': 2, 'Snow': 3, 'Fog or mist': 4, 'Unknown': 5}
type_of_collision_mapping = {'Vehicle with vehicle collision': 1, 'Collision with pedestrians': 2, 'Rollover': 3, 'Unknown': 4}
cause_of_accident_mapping = {'Overspeed': 1, 'Overtaking': 2, 'Improper parking': 3, 'Drunk driving': 4, 'Unknown': 5}

severity_mapping = {0: 'Slight Injury', 1: 'Serious Injury', 2: 'Fatal Injury'}

#list the values as a drop down menu
Day_of_week = st.selectbox('Day of the Week', list(day_of_week_mapping.keys()))
Age_band_of_driver = st.selectbox('Age Band of Driver', list(age_band_mapping.keys()))
Sex_of_driver = st.selectbox('Sex of Driver', list(sex_mapping.keys()))
Educational_level = st.selectbox('Educational Level', list(educational_level_mapping.keys()))
Vehicle_driver_relation = st.selectbox('Vehicle Driver Relation', list(vehicle_driver_relation_mapping.keys()))
Driving_experience = st.selectbox('Driving Experience', list(driving_experience_mapping.keys()))
Type_of_vehicle = st.selectbox('Type of Vehicle', list(type_of_vehicle_mapping.keys()))
Owner_of_vehicle = st.selectbox('Owner of Vehicle', list(owner_of_vehicle_mapping.keys()))
Service_year_of_vehicle = st.selectbox('Service Year of Vehicle', list(service_year_mapping.keys()))
Defect_of_vehicle = st.selectbox('Defect of Vehicle', list(defect_of_vehicle_mapping.keys()))
Area_accident_occurred = st.selectbox('Area Accident Occurred', list(area_accident_mapping.keys()))
Lanes_or_Medians = st.selectbox('Lanes or Medians', list(lanes_or_medians_mapping.keys()))
Road_alignment = st.selectbox('Road Alignment', list(road_alignment_mapping.keys()))
Types_of_Junction = st.selectbox('Types of Junction', list(types_of_junction_mapping.keys()))
Road_surface_type = st.selectbox('Road Surface Type', list(road_surface_type_mapping.keys()))
Road_surface_conditions = st.selectbox('Road Surface Conditions', list(road_surface_conditions_mapping.keys()))
Light_conditions = st.selectbox('Light Conditions', list(light_conditions_mapping.keys()))
Weather_conditions = st.selectbox('Weather Conditions', list(weather_conditions_mapping.keys()))
Type_of_collision = st.selectbox('Type of Collision', list(type_of_collision_mapping.keys()))
Cause_of_accident = st.selectbox('Cause of Accident', list(cause_of_accident_mapping.keys()))

# user input data conversion
input_data = pd.DataFrame(
    [[day_of_week_mapping[Day_of_week], age_band_mapping[Age_band_of_driver], sex_mapping[Sex_of_driver], 
      educational_level_mapping[Educational_level], vehicle_driver_relation_mapping[Vehicle_driver_relation], 
      driving_experience_mapping[Driving_experience], type_of_vehicle_mapping[Type_of_vehicle], 
      owner_of_vehicle_mapping[Owner_of_vehicle], service_year_mapping[Service_year_of_vehicle], 
      defect_of_vehicle_mapping[Defect_of_vehicle], area_accident_mapping[Area_accident_occurred], 
      lanes_or_medians_mapping[Lanes_or_Medians], road_alignment_mapping[Road_alignment], 
      types_of_junction_mapping[Types_of_Junction], road_surface_type_mapping[Road_surface_type], 
      road_surface_conditions_mapping[Road_surface_conditions], light_conditions_mapping[Light_conditions], 
      weather_conditions_mapping[Weather_conditions], type_of_collision_mapping[Type_of_collision], 
      cause_of_accident_mapping[Cause_of_accident]]],
    columns=["Day_of_week", "Age_band_of_driver", "Sex_of_driver", "Educational_level", "Vehicle_driver_relation",
             "Driving_experience", "Type_of_vehicle", "Owner_of_vehicle", "Service_year_of_vehicle", 
             "Defect_of_vehicle", "Area_accident_occured", "Lanes_or_Medians", "Road_allignment", 
             "Types_of_Junction", "Road_surface_type", "Road_surface_conditions", "Light_conditions", 
             "Weather_conditions", "Type_of_collision", "Cause_of_accident"]
)

# Prediction button
if st.button('Predict'):
# Predict the accident severity
    prediction = model.predict(input_data)
    severity = severity_mapping.get(prediction[0], 'Unknown')

# Output prediction
    st.markdown(f'The predicted accident severity is: {severity}')
