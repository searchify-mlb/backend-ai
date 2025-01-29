from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_community.vectorstores import BigQueryVectorSearch
from langchain_google_vertexai import VertexAIEmbeddings
from config import PROJECT_ID, REGION, DEST_DATASET, DEST_TABLE, EMBEDDING_MODEL

def init_vector_store():
    """Initialize the vector store with embeddings"""
    embedding = VertexAIEmbeddings(
        model_name=EMBEDDING_MODEL,
        project=PROJECT_ID
    )
    
    return BigQueryVectorSearch(
        project_id=PROJECT_ID,
        dataset_name=DEST_DATASET,
        table_name=DEST_TABLE,
        location=REGION,
        embedding=embedding,
        distance_strategy=DistanceStrategy.EUCLIDEAN_DISTANCE
    )

def search_videos(query: str, vector_store):
    """Search for videos based on text query"""
    docs = vector_store.similarity_search(query)
    
    results = []
    for doc in docs:
        result = {
            "metadata": {
                "video": doc.metadata["video"],
                "id": doc.metadata["__id"],
                "job_id": doc.metadata["__job_id"]
            },
            "content": doc.page_content
        }
        results.append(result)
    
    return {
        "results": results,
        "total_count": len(results)
    }