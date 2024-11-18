#Authors: Justin Natividad, Alexander Cornwell

import heapq
from datetime import datetime

#Example data
posts = {
    1: {"views": 100, "comments": 50, "likes": 20, "timestamp": "2024-11-10T12:00:00"},
    2: {"views": 300, "comments": 10, "likes": 50, "timestamp": "2024-11-12T15:00:00"},
    3: {"views": 150, "comments": 20, "likes": 25, "timestamp": "2024-11-11T10:00:00"},
}

#Task 4: Trending Post Report

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

#Calculate trending scores and push to heap
trending_posts = []
for post_id, post in posts.items():
    score = calculate_trending_score(post)
    heapq.heappush(trending_posts, (-score, post_id))

#Get top k trending posts
top_k = 2
top_posts = heapq.nsmallest(top_k, trending_posts)

#Display results
print("Trending Posts:")
for score, post_id in top_posts:
    post = posts[post_id]
    print(f"Post ID: {post_id}, Score: {(-score):.2f}, Views: {post['views']}, Comments: {post['comments']}, Likes: {post['likes']}")
