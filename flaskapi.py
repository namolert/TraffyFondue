from flask import Flask, request, jsonify
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, IndexToString
import pandas as pd
import train_random_forest

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "Hello Guys"


@app.route('/predict', methods=['POST'])
def predict_star():
    data = request.json
    df = pd.DataFrame(data, index=[0])
    spark_pred = SparkSession.builder.getOrCreate()
    spark_df = spark_pred.createDataFrame(df)

    label_indexer = StringIndexer(inputCol='star', outputCol='label')
    indexer_model = label_indexer.fit(df_select)
    indexer_model_trans = indexer_model.transform(spark_df)

    indexer = StringIndexer(inputCols=['type', 'time_diff', 'subdistrict', 'district'], outputCols=[
                            'type_indexed', 'time_diff_indexed', 'subdistrict_indexed', 'district_indexed'])
    indexed_df = indexer.fit(df_select).transform(indexer_model_trans)
    encoder = OneHotEncoder(inputCols=['type_indexed', 'time_diff_indexed', 'subdistrict_indexed', 'district_indexed'], outputCols=[
                            'type_encoded', 'time_diff_encoded', 'subdistrict_encoded', 'district_encoded'])
    encoded_df = encoder.fit(indexed_df).transform(indexed_df)
    assembler = VectorAssembler(inputCols=[
                                'type_encoded', 'time_diff_encoded', 'subdistrict_encoded', 'district_encoded'], outputCol='features')
    final_df = assembler.transform(encoded_df)

    predictions = training_model.transform(final_df)
    predict_label_reverse = IndexToString(
        inputCol="prediction", outputCol="predicted_result", labels=indexer_model.labels)
    predictions_res = predict_label_reverse.transform(predictions)

    predicted_star = predictions_res.select('predicted_result').first()[0]
    response = {'predicted_star': predicted_star}

    return jsonify(response)


if __name__ == '__main__':
    app.run()
