import heapq
from datetime import datetime

# Example data
posts = {
    1: {"views": 100, "comments": 50, "likes": 20, "timestamp": "2024-11-10T12:00:00", "content": "This is about cats", "user": {"age": 25, "gender": "female"}},
    2: {"views": 300, "comments": 10, "likes": 50, "timestamp": "2024-11-12T15:00:00", "content": "Dogs are the best!", "user": {"age": 30, "gender": "male"}},
    3: {"views": 150, "comments": 20, "likes": 25, "timestamp": "2024-11-11T10:00:00", "content": "Cats and dogs together", "user": {"age": 22, "gender": "female"}},
}

#Function to calculate trending score
def calculate_trending_score(post):
    
    #Weights of the interactions
    w_views, w_comments, w_likes, w_decay = 1, 2, 1, 0.5
    
    #Calculate time difference
    time_diff = (datetime.now() - datetime.fromisoformat(post["timestamp"])).total_seconds() / 3600
    
    #Trending score calculation
    decay = w_decay * time_diff
    trending_score = w_views * post["views"] + w_comments * post["comments"] + w_likes * post["likes"] - decay
    
    return trending_score

#Function to filter posts
def filter_posts(posts, keyword=None, min_age=None, max_age=None, gender=None):
    filtered_posts = {}
    for post_id, post in posts.items():
        user = post["user"]
        if keyword and keyword.lower() not in post["content"].lower():
            continue  # Skip posts that don't contain the keyword
        if min_age and user["age"] < min_age:
            continue  # Skip users minimum age
        if max_age and user["age"] > max_age:
            continue  # Skip users above maximum age
        if gender and user["gender"].lower() != gender.lower():
            continue  # Skip users with a different gender, can be changed how the filter works based on gender
        filtered_posts[post_id] = post
    return filtered_posts

#Example Filter: Filter for posts that mention "cats" and are from users aged 20-30 who are female
filtered_posts = filter_posts(posts, keyword="cats", min_age=20, max_age=30, gender="female")

#Calculate trending scores and push to heap
trending_posts = []
for post_id, post in filtered_posts.items():
    score = calculate_trending_score(post)
    heapq.heappush(trending_posts, (-score, post_id))

#Get top k trending posts
top_k = 2
top_posts = heapq.nsmallest(top_k, trending_posts)

# Display Results
print("Trending Posts:")
for score, post_id in top_posts:
    post = filtered_posts[post_id]
    print(f"Post ID: {post_id}, Score: {(-score):.1f}, Views: {post['views']}, Comments: {post['comments']}, Likes: {post['likes']}, Content: \"{post['content']}\"")
