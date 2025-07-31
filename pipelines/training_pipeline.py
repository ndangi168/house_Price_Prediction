from zenml import Model, pipeline, step
from steps.data_ingestion_steps import data_ingestion_step
from steps.handle_missing_values_steps import handle_missing_values_step

@pipeline(
    model = Model(
        name="prices_predictor"
    ),
)

def ml_pipeline():
    raw_data = data_ingestion_step("/Users/nikhildangi/Documents/COde/housePricePrediction/data/archive.zip")
    cleaned_df = handle_missing_values_step(raw_data)
    model = cleaned_df
    return model

if __name__ == "__main__":
    run = ml_pipeline()