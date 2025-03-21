import pandas as pd
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer



data = [
    {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
    {"id": "vec2", "text": "The tech company Apple is known for its innovative products like the iPhone."},
    {"id": "vec3", "text": "Many people enjoy eating apples as a healthy snack."},
    {"id": "vec4", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
    {"id": "vec5", "text": "An apple a day keeps the doctor away, as the saying goes."},
    {"id": "vec6", "text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership."}
]

df = pd.DataFrame(data)

pc = Pinecone(api_key="pcsk_gbdCE_SEAVggt7GWdDgEfzWGQat9jzxpmqKyL3pd2xSh64Ysjt1PAoV3ecGcM8yWUPFNm")
index_name= "quickstart"

model = SentenceTransformer('all-MiniLM-L6-v2')

#embed text to model
embeddings = model.encode(df['text'].tolist())

#insert Id's to dataframe
ids = df['id'].tolist()
print(embeddings)




    
# Wait for the index to be ready
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)

index = pc.Index(index_name)


chunk_size = 100
for i in range(0, len(embeddings), chunk_size):
    batch_ids = ids[i:i+chunk_size]
    batch_embeddings = embeddings[i:i+chunk_size]
    index.upsert(vectors=zip(batch_ids, batch_embeddings), namespace="ns1")
    
    
    
print(index.describe_index_stats())

#This is supposed to work but I can't create indexes on Pinecone right now. Model is set for size 384 not 1024!.