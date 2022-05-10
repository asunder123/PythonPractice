###### Import package ######
import aporia
            
            ###### Initiate Aporia ######
aporia.init(token="a28ba2244c2c7a76e5bb38900c57836af0a35f50fd910c2f709111f57f420927", 
                                environment="local-dev",verbose=True)
###### Report Version Schema ######
apr_model_version = "sandbox-version"
apr_model_type = "binary"
apr_features_schema = {
            "amount": "numeric",
                "owner": "string",
                    "is_new": "boolean",
                        "created_at": "datetime",
                        }

apr_predictions_schema = {
            "approved": "boolean",
                "confidence": "numeric",
                }
apr_model = aporia.create_model_version(
model_id="model-alerts",
model_version=apr_model_version,
model_type=apr_model_type,
features=apr_features_schema,
predictions=apr_predictions_schema
###### Report Inference ######
apr_prediction_id = "pred_1337"

apr_features_dict = {
 "amount": 3918,"
  owner": "John Doe","
  is_new": "true","
  created_at": "2021-01-17",
        }

apr_prediction_dict = {
            "approved": "true",
            "confidence": 0.81,
                        }

apr_model.log_prediction(
 id=apr_prediction_id,
 features=apr_features_dict,
 predictions=apr_prediction_dict,
                )

apr_model.flush()
                            )
