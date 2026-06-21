prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt B

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): Prompt B clearly defines the AI's role, task, audience, and constraints,
# making the instructions more specific.
# Your answer (Reason 2): Prompt B breaks the work into numbered steps, making it easier for the AI
# to follow and produce a well-organized response.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: Prompt A provides rich background context, helping the AI better
# understand the business situation and purpose of the analysis.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
# Your answer:

improved_prompt = """
Role: You are a data analyst helping a retail marketing team.

I am a marketing manager at a retail company and we have just finished
a three-month campaign. My team has collected customer feedback through
an online survey and we now have about 500 responses stored in a
spreadsheet.

Task:
Analyse the survey data.

Data:
500 responses containing age group, product purchased,
satisfaction rating (1-5), and written comments.

Steps:
1. Identify the age groups and products with the lowest satisfaction scores.
2. Extract the most common complaint themes from the written comments.
3. Write a short executive summary.

Audience:
CEO presentation on Friday.

Constraints:
Keep the summary concise and free of technical jargon.
"""

 Explanation:
# I rewrote Prompt A by borrowing the Role, Steps, Audience, and Constraints
# structure from Prompt B. These additions make the prompt clearer, more
# organized, and more likely to produce an accurate and well-structured response.