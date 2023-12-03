import praw

reddit = praw.Reddit(
    client_id='YourClientID',
    client_secret='YourClientSecret',
    user_agent='MyRedditScraper',
    username='YourUsername',
    password='YourPassword'
)

# Define the subreddit and search keywords
subreddit = reddit.subreddit('oculus')
keywords = ['too heavy', 'weight too much', 'uncomfortable']

# Search for both submissions and comments containing the specified keywords
weight_complaints_submissions = []

for keyword in keywords:
    weight_complaints_submissions.extend(list(subreddit.search(keyword, time_filter='all', sort='relevance')))

weight_complaints_comments = []

# Collect comments containing the keywords
for submission in weight_complaints_submissions:
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if hasattr(comment, 'body') and isinstance(comment.body, str):
            for keyword in keywords:
                if keyword in comment.body.lower():
                    weight_complaints_comments.append(comment)
                    break

# Count the number of submissions and comments related to weight complaints
num_weight_complaints_submissions = len(weight_complaints_submissions)
num_weight_complaints_comments = len(weight_complaints_comments)

# Display the counts
print(f"Number of submissions related to weight complaints in 'oculus' subreddit: {num_weight_complaints_submissions}")
print(f"Number of comments related to weight complaints in 'oculus' subreddit: {num_weight_complaints_comments}")
