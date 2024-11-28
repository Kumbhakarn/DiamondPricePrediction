from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline  # Assuming this is your pipeline for prediction

application = Flask(__name__)
app = application

# Home page route
@app.route('/')
def home_page():
    return render_template('index.html')

# Prediction form route
@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('form.html')  # Shows the form to input data
    else:
        # Extract form data and predict the price
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        final_new_data = data.get_data_as_dataframe()  # Convert form data to dataframe
        predict_pipeline = PredictPipeline()
        prediction = predict_pipeline.predict(final_new_data)  # Get the prediction

        # Round off the predicted price
        results = round(prediction[0], 2)

        # Return the result back to form page with the prediction
        return render_template('form.html', final_result=results)

if __name__ == "__main__":
    app.run(debug=True)
