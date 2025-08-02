from zenml import Model, pipeline, step
from steps.data_ingestion_steps import data_ingestion_step
from steps.handle_missing_values_steps import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
from steps.data_splitter_step import data_splitter_step
from steps.model_builder_step import model_building_step
from steps.model_evaluator_step import model_evaluator_step

@pipeline(
    model = Model(
        name="prices_predictor"
    ),
)

def ml_pipeline():
    raw_data = data_ingestion_step("/Users/nikhildangi/Documents/COde/housePricePrediction/data/archive.zip")
    
    clean_data = handle_missing_values_step(raw_data)

    engineered_data = feature_engineering_step(clean_data, strategy="log", features=["Gr Liv Area", "SalePrice"])

    clean_data = outlier_detection_step(engineered_data, column_name="SalePrice")

    x_train, x_test, y_train, y_test = data_splitter_step(clean_data, target_column="SalePrice")

    model = model_building_step(x_train, y_train)

    evaluation_metrics, mse = model_evaluator_step(
        trained_model=model,
        X_test=x_test, 
        y_test=y_test
    )

    return model

if __name__ == "__main__":
    run = ml_pipeline()