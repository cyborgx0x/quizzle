import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
data = {
    'question_id': [1, 2, 3, 4, 5],
    'question_text': [
        'What is the capital of France?',
        'Solve the equation: 2x + 3 = 7',
        'What is the largest planet in our solar system?',
        'Who wrote the play "Romeo and Juliet"?',
        'What is the chemical symbol for water?'
    ],
    'subject': ['geography', 'math', 'science', 'literature', 'science']
}

questions = pd.DataFrame(data)

tfidf = TfidfVectorizer(stop_words='english')
questions['question_text'] = questions['question_text'].fillna('')
tfidf_matrix = tfidf.fit_transform(questions['question_text'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(question_id, cosine_sim=cosine_sim):
    idx = question_id - 1
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    question_indices = [i[0] for i in sim_scores]
    return questions['question_text'].iloc[question_indices]

recommended_questions = get_recommendations(1)
print(recommended_questions)
