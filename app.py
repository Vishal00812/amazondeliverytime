import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scr.pipeline.predict_pipeline import CustomData, PredictPipeline
import streamlit as st
import datetime

# Streamlit UI
def main():
    st.title('EXPECTED DELIVERY TIME INDICATOR')
    age_of_delivery_person = st.text_input("Age Of Delivery Person", "")
    rating_of_delivery_person = st.text_input("Rating Of Delivery Person", "")
    restaurant_latitude = st.text_input("Restaurant Latitude", "")
    restaurant_longitude = st.text_input("Restaurant Longitude", "")
    delivery_location_latitude = st.text_input("Delivery Location Latitude", "")
    delivery_location_longitude = st.text_input("Delivery Location Longitude", "")
    order_date = st.date_input("Order Date", 'today')
    date_str = order_date.strftime('%d-%m-%y')
    time_order_placed = st.time_input("Time When Order Placed", 'now')
    time_str1 = time_order_placed.strftime('%H:%M')
    time_order_picked = st.time_input("Time When Order Picked By Delivery Person", 'now')
    time_str2 = time_order_picked.strftime('%H:%M')
    weather_condition = st.selectbox("Weather Conditions", ["Fog", "Stormy", "Sandstorms", "Cloudy", "Windy", "Sunny"])
    road_traffic_density = st.selectbox("Road Traffic Density", ["Jam", "High", "Medium", "Low"])
    vehicle_condition = st.selectbox("Vehicle Condition", ["0", "1", "2", "3"])
    type_of_order = st.selectbox("Type Of Order", ["Snack", "Meal", "Drinks", "Buffet"])
    type_of_vehicle = st.selectbox("Type Of Vehicle Used By Delivery Person", ["motorcycle", "scooter", "electric_scooter", "bicycle"])
    multiple_deliveries = st.text_input("Multiple Deliveries", "")
    festival = st.selectbox("Festival", ["Yes", "No"])
    city = st.selectbox("City", ["Metropolitian", "Urban", "Semi-Urban"])

    # Form inputs
    
    # Predict button
    if st.button('Predict your delivery time!!!'):
        try:
            # Create CustomData object
            data = CustomData(
                Delivery_person_Age=age_of_delivery_person,
                Delivery_person_Ratings= rating_of_delivery_person,
                Restaurant_latitude=restaurant_latitude,
                Restaurant_longitude=restaurant_longitude,
                Delivery_location_latitude=delivery_location_latitude,
                Delivery_location_longitude=delivery_location_longitude,
                Order_Date= date_str,
                Time_Orderd=time_str1,
                Time_Order_picked=time_str2,
                Weather_condition=weather_condition,
                Road_traffic_density=road_traffic_density,
                Vehicle_condition=vehicle_condition,
                Type_of_order=type_of_order,
                Type_of_vehicle=type_of_vehicle,
                multiple_deliveries=multiple_deliveries,
                Festival=festival,
                City=city
            )

            # Get data as DataFrame
            pred_df = data.get_data_as_data_frame()
            st.write(pred_df)

            # Perform prediction
            predict_pipeline = PredictPipeline()
            delivery_prediction = predict_pipeline.predict(pred_df)

            # Display the prediction result
            st.success(f'The predicted delivery time is {delivery_prediction[0]}')

        except Exception as e:
            st.error(f'Error occurred: {str(e)}')

if __name__ == '__main__':
    main()
