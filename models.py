from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames

#function to get the llm model from watsonx and return the llm object
def get_llm():
    model_id= 'ibm/granite-3-2-8b-instruct'
    parameters= {
        'temperature': 0.5,
        'max_new_tokens':  256
    }
    project_id= 'skills_network'
    watsonx_llm= WatsonxLLM(
        model_id=model_id,
        url="https://us-south.ml.cloud.ibm.com",
        project_id=project_id,
        params=parameters
    )
    return watsonx_llm

def watsonx_embedding():
    embed_params= {
        EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
        EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True}
    }

    watsonx_embedding= WatsonxEmbeddings(
        model_id= "ibm/slate-125m-english-rtrvr",
        url="https://us-south.ml.cloud.ibm.com",
        project_id= "skills_network",
        params= embed_params
    )
    return watsonx_embedding