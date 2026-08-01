import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

 
# Page Configuration
 
st.set_page_config(
    page_title="DriveIntel",
    page_icon="🚗",
    layout="wide"
)

 
# Title
 
st.title("🚗 DriveIntel")
st.subheader("Driving Maneuver Classification using Machine Learning")

st.markdown("""
Upload a **CSV file containing the engineered sensor features**.

The trained Random Forest model analyzes the uploaded driving session and predicts the driving maneuver for each sensor window.

### Driving Maneuver Classes

- 🚀 **Class 1** → Sudden Acceleration
- ↪️ **Class 2** → Sudden Right Turn
- ↩️ **Class 3** → Sudden Left Turn
- 🛑 **Class 4** → Sudden Brake
""")

 
# Load Model
 
try:
    model = joblib.load("models/random_forest.pkl")
except FileNotFoundError:
    st.error("❌ Model file not found! Please ensure models/random_forest.pkl exists.")
    st.stop()

 
# Behavior Mapping
 
behavior_map = {
    1: "🚀 Sudden Acceleration",
    2: "↪️ Sudden Right Turn",
    3: "↩️ Sudden Left Turn",
    4: "🛑 Sudden Brake"
}

 
# Upload CSV
 
uploaded_file = st.file_uploader(
    "Upload Engineered Features CSV",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        data = pd.read_csv(uploaded_file)

        st.success("✅ File uploaded successfully!")

        st.subheader("Uploaded Dataset")

        st.dataframe(data.head())

         
        # Validate Columns
         
        expected_columns = list(model.feature_names_in_)

        missing_columns = [
            col for col in expected_columns
            if col not in data.columns
        ]

        if missing_columns:

            st.error("❌ The uploaded file is missing required columns.")

            st.write("### Missing Columns")

            st.write(missing_columns)

        else:

            # Keep columns in correct order
            data = data[expected_columns]

             
            # Prediction
             
            predictions = model.predict(data)

            probabilities = model.predict_proba(data)

            confidence = probabilities.max(axis=1)

             
            # Create Result DataFrame
             
            result = pd.DataFrame()

            result["Predicted_Class"] = predictions

            result["Predicted_Behavior"] = [
                behavior_map[p]
                for p in predictions
            ]

            result["Confidence"] = (
                confidence * 100
            ).round(2)

             
            # Summary Graph
             
            st.subheader("📊 Driving Behavior Summary")

            summary = result["Predicted_Behavior"].value_counts()

            fig, ax = plt.subplots(figsize=(9, 5))

            bars = ax.bar(
                summary.index,
                summary.values
            )

            ax.set_title("Detected Driving Maneuvers")
            ax.set_xlabel("Driving Maneuver")
            ax.set_ylabel("Number of Predictions")

            # Keep labels horizontal
            plt.xticks(rotation=0)

            # Add values on top of bars
            for bar in bars:
                height = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width()/2,
                    height + 2,
                    f"{int(height)}",
                    ha="center",
                    va="bottom",
                    fontsize=10
                )

            plt.tight_layout()

            st.pyplot(fig)

             
            # Metrics
             
            total_predictions = len(result)

            most_common = summary.idxmax()

            most_common_count = summary.max()

            percentage = (
                most_common_count /
                total_predictions
            ) * 100

            average_confidence = result["Confidence"].mean()

            st.subheader("📈 Overall Analysis")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Sensor Windows",
                    total_predictions
                )

            with col2:
                st.metric(
                    "Dominant Maneuver",
                    most_common
                )

            with col3:
                st.metric(
                    "Average Confidence",
                    f"{average_confidence:.2f}%"
                )

             
            # Final Conclusion
             
            st.subheader("📝 Final Conclusion")

            if percentage >= 60:

                st.success(
                    f"""
### Session Summary

The uploaded driving session is **predominantly characterized by {most_common}**, accounting for **{percentage:.1f}%** of all predicted driving maneuvers.

This indicates that the analyzed driving session was mainly associated with this maneuver.
"""
                )

            elif percentage >= 40:

                st.info(
                    f"""
### Session Summary

The uploaded driving session contains a mixture of driving maneuvers, with **{most_common}** being the most frequently detected maneuver (**{percentage:.1f}%**).

No single maneuver overwhelmingly dominates the session, suggesting varied driving patterns throughout the recording.
"""
                )

            else:

                st.info(
                    """
### Session Summary

The uploaded driving session contains a balanced distribution of different driving maneuvers.

No single maneuver dominates the analyzed session, indicating diverse driving events throughout the uploaded data.
"""
                )

            st.markdown("---")

            st.caption(
                """
**Note**

DriveIntel predicts **driving maneuvers** (Sudden Acceleration, Sudden Right Turn, Sudden Left Turn, and Sudden Brake) using engineered vehicle motion sensor features.

The predictions describe the detected maneuver within each sensor window and **should not be interpreted as an overall driver safety or risk score**.
"""
            )

    except Exception as e:

        st.error(f"❌ An error occurred: {e}")