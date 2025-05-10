from sentence_transformers import SenteceTransformer, util 

model = SentenceTransformer("all-MiniLM-L6-v2")

def is_simmilar_topic(new_topic, existing_topics, threshold=0.85):
    new_vec = model.encode(new_topic, convert_to_tensors=True)
    existing_vec = model.encode(existing_topics, convert_to_tensors=True)

    similarities = util.cos_sim(new_vec, existing_vec)
    max_score, idx = similaries.max().item(), similarities.argmax().item()

    if max_score >= threshold:
        return  existing_topics[idx]
    else:
        return None
