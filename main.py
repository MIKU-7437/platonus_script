from jinja2 import Template
import os

class Q:
    def __init__(self, question, answers, correct_answers, answers_i=""):
        # Initialize question text and image
        if isinstance(question, list):
            self.question_text = question[0]
            self.question_img = question[1] if len(question) > 1 else ""
        elif isinstance(question, str):
            self.question_text = question
            self.question_img = ""
        correct_answers_new = correct_answers
        if type(correct_answers)==list:
            pass
        else:
            correct_answers_new = [int(correct_answers)]
        if answers_i:
            answers_i = answers_i.split(',')
            answers_full = []
            for i in range(len(answers_i)):
                answers_full.append([answers[i], answers_i[i], 1 if i+1 in correct_answers_new else 0])  
            self.answers = answers_full
        else:
            answers_full = []
            for i in range(len(answers)):
                answers_full.append([answers[i], "", 1 if (i+1 in correct_answers_new) else 0])  
            self.answers = answers_full  # Handling empty image URLs

# Create Question objects

# Introduction and Descriptive Statistics for Exploring Data
q1_1_1_1 =  Q(
    "What is an appropriate way to visualize a list of the eye colors of 120 people? Select all that apply.",
    [
        "pie chart",
        "box plot",
        "dot plot"
    ],
    [1, 3]
)

q1_1_1_4 = Q(
    "You want to investigate whether households in California tend to have a higher income than households in Massachusetts. Which summary measure would you use to compare the two states?",
    [
        "3rd quartile of household income",
        "mean household income",
        "median household income"
    ],
    3
)

q1_1_1_5 =  Q(
    "Suppose all household incomes in California increase by 5%. How does that change the mean household income?",
    [
        "cannot be determined from the information given",
        "the mean household income doesn't change",
        "the mean household income goes up by 5%"
    ],
    3
)
q1_1_1_6 = Q(
    "Suppose all household incomes in California increase by 5%. How does that change the median household income?",
    [
        "median household income goes up by 5%",
        "the median household income doesn't change",
        "cannot be determined from the information given"
    ],
    1
)
q1_1_1_7 = Q(
    "Suppose all household incomes in California increase by 5%. How does that change the standard deviation of the household incomes?",
    [
        "the standard deviation of the household incomes goes up by 5%",
        "the standard deviation of the household incomes doesn't change",
        "cannot be determined from the information given"
    ],
    1
)
q1_1_1_8 = Q(
    "Suppose all household incomes in California increase by 5%. How does that change the interquartile range of the household incomes?",
    [
        "the interquartile range of the household incomes doesn't change",
        "cannot be determined from the information given",
        "the interquartile range of the household incomes goes up by 5%"
    ],
    3
)

q1_1_1_9 = Q(
    "Suppose all household incomes in California increase by $5,000. How does that change the mean household income?",
    [
        "the mean household income doesn't change",
        "the mean household income goes up by $5,000",
        "cannot be determined from the information given"
    ],
    2
)

q1_1_1_10 = Q(
    "Suppose all household incomes in California increase by $5,000. How does that change the median household income?",
    [
        "the median household income goes up by $5,000",
        "cannot be determined from the information given",
        "the median household income doesn't change"
    ],
    1
)

q1_1_1_11 = Q(
    "Suppose all household incomes in California increase by $5,000. How does that change the standard deviation of the household incomes?",
    [
        "the standard deviation of the household incomes doesn't change",
        "the standard deviation of the household incomes goes up by $5,000",
        "cannot be determined from the information given"
    ],
    1
)
q1_1_1_12 = Q(
    "Suppose all household incomes in California increase by $5,000. How does that change the interquartile range of the household incomes?",
    [
        "the interquartile range of the household incomes doesn't change",
        "cannot be determined from the information given",
        "the interquartile range of the household incomes goes up by $5,000"
    ],
    1
)
q1_1_1_13 = Q(
    "The median sales price for houses in a certain county during the last year was $342,000. What can we say about the percentage of sales represented by the houses that sold for more than $342,000?",
    [
        "the houses that sold for more than $342,000 represent more than 50% of all sales",
        "the houses that sold for more than $342,000 represent exactly 50% of all sales",
        "the houses that sold for more than $342,000 represent less than 50% of all sales"
    ],
    2
)

# Producing Data and Sampling
q1_2_1_1 = Q(
    "A news company located next to Times Square in New York wants to get a sense how people feel about a proposed law on immigration. A reporter steps out of the building and randomly selects 100 people walking there and asks them about the proposed law. What can we say about this sampling plan? Single correct answer.",
    [
        "it leads to voluntary response bias",
        "it leads to non-response bias",
        "it represents a simple random sampling",
        "it leads to selection bias"
    ],
    4
)

q1_2_1_2 = Q(
    "A car company wants to get a sense how satisfied the owners of its new car model are with the quality of that car. It randomly selects 250 numbers from all the vehicle registration numbers that have been issued for this model and contacts the owners of that model. What can we say about this sampling plan?",
    [
        "it represents a simple random sampling",
        "it leads to selection bias",
        "it leads to non-response bias",
        "it leads to voluntary response bias"
    ],
    1
)
q1_2_1_3 = Q(
    "An airline wants to do a customer survey in order to improve its service. For one month, it sends an email to a random sample of customers which flew with the airline on the previous day (no customer will be contacted more than once). The email states that the airline would like the customer to fill out a 10-minute survey in order to help the airline improve its service. What can we say about this sampling plan? Single correct answer.",
    [
        "it represents a simple random sampling",
        "it leads to selection bias",
        "it leads to non-response bias",
        "it leads to voluntary response bias"
    ],
    3
)
q1_2_1_4 = Q(
    "As in the previous question, an airline wants to do a customer survey in order to improve its service. For one month, it sends an email to a random sample of customers which flew with the airline on the previous day (no customer will be contacted more than once). Again, the email states that the airline would like the customer to fill out a 10-minute survey in order to help the airline improve its service, but this time it states in addition that every respondent will receive a gift card worth $100. What can we say about this sampling plan?",
    [
        "it represents a simple random sampling",
        "it leads to selection bias",
        "it leads to non-response bias",
        "it leads to voluntary response bias"
    ],
    3
)
q1_2_1_5 = Q(
    "Some years ago, there were many news reports about the 'Paleo diet'. It was claimed that the Paleo Diet would result in weight loss as well as prevention and control of many 'diseases of civilization'. A news channel decides to check this out. It recruits people who have followed the diet for the past year and selects 100 at random. It also recruits people who have not followed the diet and selects 100 at random. It finds that there is more weight loss in the diet group, and that this result is 'statistically significant'. Which of the following statements are true?",
    [
        "This is a randomized controlled experiment.",
        "It is possible that the difference in weight loss is due to the placebo effect.",
        "If a future carefully run randomized controlled experiment reveals that the paleo diet does not result in weight loss, then we can conclude that the weight loss observed above must be due to the placebo effect."
    ],
    2
)
q1_2_1_6 = Q(
    "A number of competitive female cross country runners suffer from bone loss due to the low estrogen levels. Some medical experts conjecture that this can be prevented by taking oral contraceptives, as those contain estrogen. This conjecture is to be tested with an experiment. The goal of the experiment is to find out whether taking an oral contraceptive prevents bone loss in female cross country runners. Which of the following subjects should be recruited in order to do a good experiment? (Pick one of the three.)",
    [
        "A group of women who are competitive runners and another group of women who are not competitive athletes.",
        "A group of female runners who are taking oral contraceptives and another group of female runners who are not taking oral contraceptives.",
        "A group of female runners who are not taking oral contraceptives, but who are willing to take them if asked by the organizers of the experiment to do so."
    ],
    3
)
# Probability
q1_2_2_1 = Q(
    "A fair coin is tossed 5 times. What is the probability of getting at most 4 tails?",
    [
        "","","","",
    ],
    1,
    "1_2_2/1_2_2_1_1.png,1_2_2/1_2_2_1_2.png,1_2_2/1_2_2_1_3.png,1_2_2/1_2_2_1_4.png"
)
q1_2_2_2 = Q(
    "When you roll a pair of dice, a double is when both dice show the same number, e.g. both show '1' or both show '4'. What is the chance of a double when you roll a pair of dice?",
    [
        "6/15",
        "1/6",
        "1/12",
        "1/36"
    ],
    2
)
q1_2_2_3 = Q(
    "The game Monopoly is played by rolling a pair of dice. If you land in jail, then to get out, you must roll a double on any one of your next three turns, or else pay a fine. What are the chances that you get out of jail without paying a fine?",
    [
        ""
    ],
    1,
    "1_2_2/1_2_2_3.png"
)
q1_2_2_4 = Q(
    r"3% of all applicants to the Stanford Medical School are admitted. 70% of all applicants have a GPA of 3.6 or above. Of those who are admitted, 95% have a GPA of 3.6 or above.What are the chances of being admitted for an applicant whose GPA is 3.6 or above?",
    [
        ""
    ],
    1,
    "1_2_2/1_2_2_4.png"
)
q1_2_2_5 = Q(
    "A multiple choice exam has 10 questions. Each question has 3 possible answers, of which one is correct. A student knows the correct answers to 4 questions and guesses the answers to the other 6 questions.It turns out that the student answered the first question correctly. What are the chances that the student was merely guessing?",
    [
        ""
    ],
    1,
    "1_2_2/1_2_2_5.png"
)
q1_2_2_6 = Q(
    "There are three boxes on the table: The first box contains 2 quarters, the second box contains 2 nickels, and the last box contains 1 quarter and 1 nickel. You choose a box at random, then you pick a coin at random from the chosen box.If the coin you picked is a quarter, what's the chance that the other coin in the box is also a quarter?",
    [
        ""
    ],
    1,
    "1_2_2/1_2_2_6.png"
)
#The Normal Approximation for Data and the Binomial Distribution
q1_3_1_1 = Q(
    "Scores on a certain test follow the normal curve with an average of 1350 and a standard deviation of 120. What percentage of test takers score below 1230? (Use the empirical rule.)",
    [
        "18%",
        "68%",
        "34%",
        "16%"
    ],
    4
)
q1_3_1_2 = Q(
    "Scores on a certain test follow the normal curve with an average of 1350 and a standard deviation of 120. In order to qualify for a certain job, a candidate needs to score in the top 2.5%. What score does she need?",
    [
        "1710",
        "1470",
        "1590",
        "1650"
    ],
    3
)
q1_3_1_3 = Q(
    "Recall that the main object in a boxplot is a box that is bounded by the first and the third quartiles. So the length of the box is the difference between the third and the first quartile, which is called the interquartile range. This is a measure of spread of the data; it is sometimes used as an alternative to the standard deviation. If the data follow the normal curve, then the interquartile range equals how many standard deviations? (You may use the fact that the z-value of the third quartile is 0.7.)",
    [
        "0.7",
        "1",
        "1.4",
        "2"
    ],
    3
)
q1_3_1_4 = Q(
    "There are three boxes on the table: The first box contains 2 quarters, the second box contains 2 nickels, and the last box contains 1 quarter and 1 nickel. You choose a box at random, then you pick a coin at random from the chosen box.If the coin you picked is a quarter, what's the chance that the other coin in the box is also a quarter?",
    [
        ""
    ],
    1,
    "1_3_1/4.png"
)
q1_3_1_5 = Q(
    "A fair coin is tossed 6 times. What are the chances of getting 2 tails in each the first 3 and the last 3 tosses?",
    [
        ""
    ],
    1,
    "1_3_1/5.png"
)

q1_3_1_6 = Q(
    "A fair coin is tossed 400 times. Approximately what are the chances to get more than 210 tails? (Use the empirical rule and the normal approximation to the binomial distribution.)",
    [
        "5%",
        "16%",
        "32%"
    ],
    2
)



#Sampling Distributions and the Central Limit Theorem
q1_3_2_1 = Q(
    "A town has 10,000 registered voters, of whom 6,000 are voting for the Democratic party. A survey organization is taking a sample of 100 registered voters (assume sampling with replacement). The percentage of Democratic voters in the sample will be around _____, give or take ____. (You may use the fact that the standard deviation of 6,000 1s and 4,000 0s is about 0.5)",
    [
        "60%, give or take 5%",
        "40%, give or take 5%",
        "60%, give or take 0.5%",
        "40%, give or take 0.5%"
    ],
    1
)
q1_3_2_2 = Q(
    "You solicit 100 pledges for a charitable organization. Each pledge is equally likely to be $10, $50, or $100. You may use the fact that the standard deviation of the three amounts $10, $50, and $100 is $37. What is the expected value of the sum of the 100 pledges?",
    [
        "$5333",
        "$533",
        "$3700",
        "$370"
    ],
    1
)
q1_3_2_3 = Q(
    "You solicit 100 pledges for a charitable organization. Each pledge is equally likely to be $10, $50, or $100. You may use the fact that the standard deviation of the three amounts $10, $50, and $100 is $37. What are the chances that the 100 pledges total more than $5,700?",
    [
        "16%",
        "32%",
        "5%"
    ],
    1
)
q1_3_2_4 = Q(
    "There are two candidates running for governor in CA and they are said to have roughly equal support from the voters. To get a better idea who is ahead, a company polls 400 of the 20 million registered voters in California. Likewise, there are two candidates running for mayor in Palo Alto who are said to have roughly equal support, and the company polls 400 out of the 20,000 registered voters in Palo Alto. Will the first poll be more accurate, equally accurate, or less accurate than the second poll?",
    [
        "more accurate",
        "equally accurate",
        "less accurate"
    ],
    2
)
q1_3_2_5 = Q(
    "The average taxable income reported on tax returns for the year 2016 is $45,000, and the standard deviation of the taxable incomes is $23,000. Which of the following two statements are true? Both?",
    [
        "The chances that the sum of 100 randomly selected taxable incomes exceeds $4 million can be computed from the above information using normal approximation.",
        "The percentage of taxable incomes that fall below $30,000 can be computed from the above information using normal approximation."
    ],
    1
)
#6-9 нет
#Regression
q1_4_1_1 = Q(
    "Some people believe that musical activity (e.g. playing an instrument) enhances mathematical ability. 100 high school students were selected at random. For each student, musical activity was recorded in hours per week and mathematical ability was assessed by a test. The correlation coefficient was found to be 0.85. Does the large correlation coefficient prove that musical activity enhances mathematical ability?",
    [
        "yes",
        "no"
    ],
    2
)
q1_4_1_2 = Q(
    "What would your answer to the previous question be if you learned that all students in the study came from the same grade?",
    [
        "yes",
        "no"
    ],
    2
)
q1_4_1_3 = Q(
    "For a group of commuters commuting to work on a given day, the correlation coefficient between a) time spent waiting at traffic signals, and b) total commuting time, was found to be 0.4. Which of the following statements about the correlation coefficient are true?",
    [
        "The average commuter spent 40% of the commuting time waiting at traffic signals.",
        "The more time a commuter spends commuting to work, the more time he spends waiting at traffic signals, on average.",
        "The more time a commuter spends waiting at traffic signals, the longer the total commuting time, on average.",
        "If a commuter's total commuting time increases by 10 minutes, then he will spend an additional 4 minutes waiting at traffic signals, on average."
    ],
    [2, 3]
)
q1_4_1_4 = Q(
    "A study followed 1,000 children over time. The scatter plot of heights at age 1 vs. heights at age 2 looks football-shaped with a correlation coefficient r=0.8. Alice's height at age 1 is at the 80th percentile. Would you predict her height at age 2 to be below, at, or above the 80th percentile?",
    [
        "below",
        "at",
        "above"
    ],
    1
)
q1_4_1_5 = Q(
    "In the previous question we learned that in a study of children's height, the correlation coefficient between height at age 1 vs. height at age 2 is r=0.8. Predict the z-score of Alice's height at age 2. (You may use the fact that the z-score of the 80th percentile is z=0.85.)",
    [
        "(0.8)(0.85) = 0.68",
        "0.85/0.8 = 1.0625",
        "not enough information"
    ],
    1
)
q1_4_1_6 = Q(
    "In a biology class, both the midterm scores and the final exam scores have an average of 50 and a standard deviation of 10. The scatterplot looks football-shaped and the correlation coefficient is 0.6. Claudia would like to know what score her friend Emily got on the final. Question (a): If you have no information on how Emily did on the midterm, what is your prediction for her score on the final?",
    [
        "40",
        "44",
        "50",
        "56"
    ],
    3
)
#7-9 no
q1_4_1_10 = Q(
    "A tutoring center advertises its services by stating that students who sign up improve their GPA on tests by 0.5 points on average. Is this indeed evidence that the tutoring helps or could this be due to the regression effect?",
    [
        "The improvement proves that the tutoring helps.",
        "The improvement could be due to the regression effect."
    ],
    2
)
q1_4_1_11 = Q(
    "True or false: If an observation with large leverage has a small residual, then it is not influential.",
    [
        "True",
        "False"
    ],
    2
)

#Confidence Intervals
q1_5_1_1 = Q(
    "A random sample of 500 sales prices of recently purchased homes in a county is taken. From that sample a 90% confidence interval for the average sales price of all homes in the county is computed to be $215,000 +/- $35,000. Is the following statement true or false? 'About 90% of all home sales in the county have a sales price in the range $215,000 +/- $35,000.'",
    [
        "true",
        "false"
    ],
    2
)
q1_5_1_2 = Q(
    "A random sample of 500 sales prices of recently purchased homes in a county is taken. From that sample a 90% confidence interval for the average sales price of all homes in the county is computed to be $215,000 +/- $35,000. Is the following statement: true or false? 'There is a 90% chance that the average sales price of all homes in the county is in the range $215,000 +/- $35,000.'",
    [
        "true",
        "false"
    ],
    2
)
q1_5_1_3 = Q(
    "A poll of 400 eligible voters in a city finds that 313 plan to vote in the next election. Find a 95% confidence interval for the percentage of all eligible voters in the city who plan to vote.",
    [
        ""
    ],
    1,
    "1_5_1/3.png"
)
q1_5_1_4 = Q(
    "Based on a sample of 500 salaries in a large city we want to find a confidence interval for the average salary in that city. Is it possible to do this using the formula 'average +/- z SE'? (Keep in mind that the histogram of salaries is not normal but quite skewed.)",
    [
        "yes",
        "no"
    ],
    1
)
q1_5_1_5 = Q(
    "The margin of error for the confidence interval from Question (a), which was based on 500 salaries, turns out to be $5,400. How many salaries do we need to sample in order to shrink the margin of error to about $2,000?",
    [
        ""
    ],
    1,
    "1_5_1/5.png"
)
q1_5_1_6 = Q(
    "You are interested what the current starting salary for jobs in data science is. You solicit feedback on an online forum about data science and you get 230 replies with salary numbers. Can you use the formula 'average +/- z SE' to find a confidence interval for the average starting salary?",
    [
        "yes",
        "no"
    ],
    2
)
#Resampling

q1_6_1_1 = Q(
    "We want to use the Monte Carlo method to estimate the probability of getting exactly one ace (one spot) in three rolls of die. Which of the following is a correct description for doing this?",
    [
        "To simulate the roll of a die, we draw a number at random (with replacement) from 1,2,3,4,5,6. To simulate the probability in question with B=1000 Monte Carlo simulations, we simulate the roll of a die 3B=3000 times and count the number of times an ace comes up. Then we divide this number by 3B. The resulting proportion is our Monte Carlo estimate.",
        "To simulate three rolls of a die, we draw three times a number at random (with replacement) from 1,2,3,4,5,6. If we get the number '1' exactly once, then we label this trial to be a success. We repeat this B=1000 times. The proportion of successes in these 1000 trials is our Monte Carlo estimate of the probability in question.",
        "To simulate three rolls of a die, we draw three times a number at random (with replacement) from 1,2,3,4,5,6. We repeat this simulation many times until we get the number '1' exactly once, then we stop. The desired Monte Carlo estimate is 1/(number of repetitions)."
    ],
    2
)
q1_6_1_2 = Q(
    "We want to use the Monte Carlo Method to approximate the standard error of our estimate from Question 1. Which of the following is a correct description for doing this?",
    [
        "We compute the standard deviation of the all the numbers we simulated in Question 1.",
        "In each of the B=1000 trials we simulated in Question 1, if the trial results in a success (i.e. '1' shows exactly once), then we give that trial the label 1, otherwise the label 0. We compute the standard deviation of these 1000 labels.",
        "We repeat the whole Monte Carlo simulation done in Question 1 many times (e.g. 2000 times). Each time we get an estimate of the probability in question. We compute the standard deviation of these 2000 estimates."
    ],
    3
)
q1_6_1_3 = Q(
    "We want to use the bootstrap to estimate the bias",
    [
        "Draw a bootstrap sample and compute ",
        "The bootstrap plug-in principle suggests to estimate the bias"
    ],
    2
)
q1_6_1_4 = Q(
    "We want to compute a 90% bootstrap percentile interval for the correlation coefficient based on 32 pairs. Which of the following is a correct description for doing this?",
    [
        ""
    ],
    1,
    "1_6_1/4.png"
)
#Analysis of Categorical Data
q1_6_2_1 = Q(
    "Some people suspect that child births may not be equally distributed over the seven days of the week because hospital staff (who can influence the time of delivery in some cases) may prefer to work on certain days of the week. Which of the following is the null hypothesis?",
    [
        "child births occur equally likely on the seven days of the week",
        "child births are more likely on certain days of the week"
    ],
    1
)
q1_6_2_2 = Q(
    "To investigate, you note the day of the week of 300 births that were randomly selected from all births that occurred in New York City last year. What test should you use to test the null hypothesis?",
    [
        "z-test",
        "chi-square test for goodness-of-fit",
        "chi-square test of independence",
        "chi-square test of homogeneity"
    ],
    2
)

q1_6_2_3 = Q(
    "What is the degrees of freedom for the test from Question (b)?",
    [
        "3"
    ],
    1
)

q1_6_2_4 = Q(
    "What would be the answer to Question (b) if you wanted to investigate a simpler question, namely whether the percentage of births on weekends is lower than expected?",
    [
        "z-test",
        "chi-square test for goodness-of-fit",
        "chi-square test of independence",
        "chi-square test of homogeneity"
    ],
    1
)
q1_6_2_5 = Q(
    "This question and the next one are related to the following context: A food delivery start-up decides to advertise its service by placing ads on web pages. They wonder whether the percentage of viewers who click on the ad changes depending on how often the viewers were shown the ad. They randomly select 100 viewers from among those who were shown the add once, 135 from among those who were shown the add twice, and 150 from among those who were shown the ad three times. Which is the null hypothesis?",
    [
        "the chances that the user clicks on the ad is the same for all three groups",
        "the chances that the user clicks on the ad increases with the number of ads shown"
    ],
    1
)
q1_6_2_6 = Q(
    "In the previous question, which test is appropriate to test the null hypothesis?",
    [
        "z-test",
        "chi-square test for goodness-of-fit",
        "chi-square test of independence",
        "chi-square test of homogeneity"
    ],
    4
)
q1_6_2_7 = Q(
    "A county wants to check whether the racial composition of the teachers in the county corresponds to that of the population in the county. It samples 500 teachers at random and wants to compare that sample with the census numbers about the racial groups in that county. Which test would be appropriate?",
    [
        "z-test",
        "chi-square test for goodness-of-fit",
        "chi-square test of independence",
        "chi-square test of homogeneity",
        "none of these"
    ],
    2
)
q1_6_2_8 = Q(
    "An airline wants to find out whether there is a connection between the customer's status in its frequent flyer program and the class of ticket that the customer buys. It samples 1,000 ticket records at random and for each ticket notes the status level ('none', 'silver', 'gold') and the ticket class ('economy', 'business','first'). Which test would be appropriate?",
    [
        "z-test",
        "chi-square test for goodness-of-fit",
        "chi-square test of independence",
        "chi-square test of homogeneity",
        "none of these"
    ],
    3
)
q1_6_2_9 = Q(
    "The airline wants to find out whether there is a connection between the customer's status in its frequent flyer program and the amount that the customer spends on tickets in the following year. It samples 1,000 ticket records at random and for each ticket notes the status level ('none', 'silver', 'gold') and the amount spent on tickets in the following year. Which test would be appropriate?",
    [
        "z-test",
        "chi-square test for goodness-of-fit",
        "chi-square test of independence",
        "chi-square test of homogeneity",
        "none of these"
    ],
    5
)
#One-Way Analysis of Variance
q1_7_1_1 = Q(
    "An online retailer strongly suspects that customers purchase more in the following month if they are shown a company ad more often. To confirm that hunch they randomly select 50 customers who are then sent one ad, 45 customers who are sent two ads, and 52 customers who are sent three ads. Which is the null hypothesis?",
    [
        "the spending means for the three groups are the same.",
        "the spending means increase with the number of ads"
    ],
    1
)
q1_7_1_2 = Q(
    "Based on the description of the experiment in the previous question and the boxplots below, do you think that the assumptions of ANOVA are met?",
    [
        "yes",
        "no"
    ],
    1
)
q1_7_1_3 = Q(
    "Based on the ANOVA table below and the boxplots, what is the conclusion of the analysis?",
    [
        "There is no statistically significant effect.",
        "There is sufficient evidence to conclude that the spending means increase with the number of ads.",
        "There is sufficient evidence to conclude that the spending means are not equal, but based on this analysis alone we cannot conclude that the spending means increase with the number of ads."
    ],
    3
)
q1_7_1_4 = Q(
    "Does the p-value of 0.5% mean that there is strong evidence that eye color has an effect on the type of vision correction that patients choose?",
    [
        "yes",
        "no"
    ],
    2
)
q1_7_1_5 = Q(
    "Which of the following options describes a valid conclusion?",
    [
        "There is not enough evidence to conclude that the twelve treatment means are different.",
        "We can conclude that there are differences between the two pairs of treatments that were found to be significant by the two-sample t-tests."
    ],
    1
)
q1_8_1_1 = Q(
    "What is the false discovery proportion (FDP) of the procedure that yielded the following results:",
    [
        "36/(9+36)",
        "16/(9+16)",
        "9/(9+36)",
        "9/(9+16)"
    ],
    3
)
q1_8_1_2 = Q(
    "Which of the following three statements is an appropriate summary of these findings? Select all that apply.",
    [
        "The correlation between these two lifestyle choices is highly significant and should be reported as such.",
        "The seemingly significant correlation was found as a consequence of data snooping and therefore the p-value is not valid. The researchers shouldn't report anything.",
        "The seemingly significant correlation was found as a consequence of data snooping and therefore the p-value is not valid. However, this could potentially be a significant new finding. The researchers can report it as such, pointing out that they cannot attach a valid p-value to this finding. It can serve as a hypothesis for a future study with new data, which would then allow for statistically valid conclusions."
    ],
    [2, 3]
)
q1_8_1_3 = Q(
    "Which of the following three statements is an appropriate conclusion?",
    [
        "This is sufficient evidence to reject all of these 31 null hypotheses, because there is only a 5% chance that any of these 31 p-values would be this small if the null hypotheses were true.",
        "There is a 95% probability that all of these 31 null hypotheses are false.",
        "If we reject these 31 null hypotheses then we can expect that about 5% of them are rejected in error."
    ],
    1
)
q1_8_1_4 = Q(
    "Which of the following three statements is an appropriate conclusion?",
    [
        "There is a 95% probability that all of these 31 null hypotheses are false.",
        "This is sufficient evidence to reject all of these 31 null hypotheses, because there is only a 5% chance that any of these 31 p-values would be this small if the null hypothesis were true.",
        "If we reject these 31 null hypotheses then we can expect that about 5% of them are rejected in error."
    ],
    3
)

q2_3_1 = Q(["For the below normal distribution, which of the following option holds true? σ1, σ2 and σ3 represent the standard deviations for curves 1, 2 and 3 respectively.", "q2_3_1.png"], ["σ1> σ2> σ3", "σ1< σ2< σ3", "σ1= σ2= σ3", "None"], 2)
q2_3_2 = Q("A test is administered annually. The test has a mean score of 150 and a standard deviation of 20. If Chioma's z-score is 1.50, what was her score on the test?", ["150", "130", "180", "30"], 3)
q2_3_3 = Q("If a negatively skewed distribution (i.e. skewed to the left) has a median of 50, which of the following statements are true? (Select all that apply)", ["Mode is greater than 50", "Mean is greater than 50", "Mean is less than 50", "None of the above"], [1, 3])
q2_3_4 = Q("What is the probability of getting two heads when two coins are flipped?", ["1/4", "1/2", "1/8", "1"], 1)
q2_3_5 = Q("The probability of getting a double by rolling TWO six-sided dice (with sides labeled as 1, 2, 3, 4, 5, 6) is:", ["2/36", "1", "1/6", "1/36"], 3)
q2_3_6 = Q("What is the area under a conditional Cumulative Density Function?", ["0", "1", "2", "0.5"], 2)
q2_3_7 = Q("Which of the following is a possible alternative hypothesis H1 for a two-tailed test.", ["µ is equal to 85", "µ is not equal to 85", "µ is less than 85", "µ is greater than 85"], 2)
q2_3_8 = Q("Green sea turtles have normally distributed weights, measured in kilograms, with a mean of 134.5 and a variance of 49.0. A particular green sea turtle’s weight has a z-score of -2.4. What is the weight of this green sea turtle? Round to the nearest whole number.", ["252kg", "118kg", "17kg", "151kg"], 2)
q2_3_9 = Q("A normal distribution can best be described as which of the following? (Select all that apply)", ["Symmetric", "Uniform", "Bell-shaped", "Skewed"], [1, 3])
q2_3_10 = Q("In its standardized form, the normal distribution", ["has a mean of 1 and a variance of 0.", "has a mean of 0 and a standard deviation of 1.", "has an area equal to 0.5.", "cannot be used to approximate discrete probability distributions"], 2)


q2_4_1 = Q("Using the teacher's rating data, is there an association between native (native English speakers) and the number of credits taught? What test will you use?", ["T-test", "Z-test", "Chi-Square Test for Association", "ANOVA"], 3)
q2_4_2 = Q("If I wanted to test for association using chi-square test, whether there is an association between gender (Male or Female) and tenure-ship (tenured or not tenured), what will be my degree of freedom?", ["1"], 1)
#q2_4_3 = Q("Consider a normally distributed data set with mean μ = 63.18 inches and standard deviation σ= 13.27 inches. What is the z-score when x = 91.54 inches? (To 3 decimal places)", ["2.137"])
q2_4_4 = Q(["Battery life of smartphones is of great concern to customers. A consumer group tested four brands of smartphones to determine the battery life. Samples of phones of each brand were fully charged and left to run until the battery died. What test will be be using to test the difference in means?", "q2_4_4.png"], ["Chi-square Test", "T-test", "ANOVA", "Pearson Correlation Test"], 3)
q2_4_5 = Q("A room  in a laboratory is only considered safe if the mean radiation level is 400 or less. When a sample of 10 radiation measurements were taken, the mean value of the radiation was 414 with a standard deviation of 17. What will be the appropriate test?", ["z-test", "t-test", "ANOVA", "Chi-square"], 1)
q2_4_6 = Q("The mineral content of a particular brand of  supplement pills is normally distributed with mean 490 mg and variance of 400. What is the probability that a randomly selected pill contains at least 500 mg of minerals?", ["0.3085", "0.2023", "0.0525", "0.7967"], 1)
q2_4_7 = Q("The P-value for a normally distributed right-tailed test is P=0.042. Which of the following is INCORRECT?", ["We will reject H0 at α=0.05, but not at α=0.01", "The z-score test statistic is approximately z=1.73", "The P-value for a two-tailed test based on the same sample would be P=0.084", "The P-value for a left-tailed test based on the same sample would be P= -0.042"], 4)
q2_4_8 = Q("The time X taken by a cashier in a grocery store express lane to complete a transaction follows a normal distribution with mean 90 seconds and standard deviation 20 seconds.What is the first quartile of the distribution of X (in seconds)?", ["81.2", "73.8", "76.6", "88.0"], 3)
q2_4_9 = Q("A man accused of committing a crime is taking a polygraph (lie detector) test. The polygraph is essentially testing the hypotheses H0: The man is telling the truth  vs. Ha: The man is not telling the truth. Suppose we use a 5% level of significance. Based on the man’s responses to the questions asked, the polygraph determines a P-value of 0.08. We conclude that:", ["The probability that the man is not telling the truth is 0.08.", "We fail to reject the null hypothesis as there is insufficient evidence that the man is not telling the truth.", "We reject the null hypothesis as there is sufficient evidence that the man is telling the truth.", "The probability that the man is telling the truth is 0.08."], 2)
q2_4_10 = Q("The average hourly wage at a fast-food restaurant is $5.85 with a standard deviation of $0.35. Assume that the wages are normally distributed. The probability that a selected worker earns more than $6.90 is", ["0", "0.0013", "0.9987", "0.4987"], 2)

q2_5_1 = Q("Does the decision to accept or reject the null hypothesis remain the same when evaluating differences in group means using both ANOVA and regression tests?", ["True", "False"], 1)
q2_5_2 = Q(["Give the results of the regression analysis below, what is the correlation coefficient?", "q2_5_2.png"], ["0.19", "0.036", "17.08", "0.034"], 1)
q2_5_3 = Q(["Given the results for tenure-ship vs teaching evaluation, if our null hypothesis is that there is no difference in mean evaluation scores for professors who are tenured vs professors who are not tenured. What will be the conclusion of the t-test statistics?", "q2_5_3.png"], ["P-value is less than 0.05, that means that there is a difference in mean values for professors who are tenures versus professors who are not tenured.", "P-value is less than 0.05, we will fail to reject the null hypothesis.", "There is no conclusive evidence in the results above."], 1)
q2_5_4 = Q(["We run a regression analysis in place of a t-test to test if there is a difference in number of students enrolled in classes with professors who are visible minority(vismin = 1) vs professors who are not (vismin = 0). The table is shown below. What does the coefficient for vismin mean?", "q2_5_4.png"], ["Professors who are visible minority get about 58 students less on average that professors who aren't visible minority.", "We can't conclude because the error is too large and if factored could change the conclusion of the tests.", "Professors who are visible minority get about 21 students less on average that professors who aren't visible minority.", "Professors who are visible minority get about 21 students more on average that professors who aren't visible minority."], 3)
q2_5_5 = Q("Which of these are correct about correlation coefficient? (Select all that apply)", ["A correlation coefficient of -0.9 indicates a weak linear relationship?", "A correlation coefficient of -0.9 indicates a strong linear relationship?", "The correlation coefficient (r) ranges from -1 to 1", "The correlation coefficient (r) ranges from 0 to 1"], [2,3])
q2_5_6 = Q("Which of these options is most likely to be the null hypothesis for testing correlation between two variables?", ["There is a partial association  between an instructor’s looks and teaching  evaluation  score.", "There is no association  between an instructor’s looks and teaching  evaluation  score.", "There is an association  between an instructor’s looks and teaching  evaluation  score."], 2)
q2_5_7 = Q("If we ran a regression analysis between two continuous variables amount of time spent running on a treadmill vs the amount of calories burnt. If I get a coefficient of 0.33 for the amount of time running on the treadmill and  an R-square value of 0.81. What is the correlation coefficient?", ["0.77", "0.66", "0.81", "0.9"], 4)
q2_5_8 = Q("Which of the following best explains a scatter plot?", ["A one-dimensional graph of randomly scattered data.", "A two-dimensional graph of a curved line.", "A two-dimensional graph of a straight line.", "A two-dimensional graph of data values."], 4)

q2_6_1 = Q("Which of the following is the best example of categorical data?", ["Cost of houses in a state", "Weights of children at a school", "Average temperature of a lake on each day of a year", "Number of cars owned by a household"], 4)
#q2_6_2 = Q("What is the mode of the following data set?  1, 1, 2, 5, 6", ["2", "1", "5", "3"], 1)
q2_6_3 = Q("Which of the following would be the most appropriate way to display a data set that shows change over time?", ["A pie chart", "A line graph", "A bar chart", "A scatter plot"], 2)
q2_6_4 = Q("Which of the following data sets would be most appropriate for a bar chart?", ["Average temperature of a lake on each day of a year", "Price distribution of hotel rooms", "Elementary school children’s favorite colors", "Percent of a population by race"], 3)
q2_6_5 = Q("True or false? The statement, “Speeding is not correlated with life-expectancy” is an example of a null hypothesis.", ["True", "False"], 1)
#q2_6_6 = Q("In a two-tailed hypothesis test, let the null hypothesis µ be less than or equal to 100, alpha = 0.1, and the p-value = 0.04. Which of the following statements is true?", ["Reject the null hypothesis because the p-value is less than half of alpha.", "Fail to reject the null hypothesis because the p-value is less than alpha.", "Fail to reject the null hypothesis because the p-value is less than half of alpha.", "Reject the null hypothesis because the p-value is less than alpha."], 4)
q2_6_7 = Q("Which of the following statements is true about z-tests and t-tests?", ["When comparing the means of two independent samples with equal variances, a t-test should be used.", "When comparing the means of two independent samples with unequal means, a z-test should be used.", "When comparing the means of two independent samples with equal means, a z-test should be used.", "When comparing the means of two independent samples with unequal variances, a z-test should be used."], 1)
q2_6_8 = Q("If an alternative hypothesis claims that at least one of three population means is greater than 100, which type of distribution should be used?", ["T", "Normal", "F", "Z"], 3)
q2_6_9 = Q("Which of the following tests is most appropriate to find the correlation between bone density given a person’s daily calcium intake?", ["Regression", "T-test", "ANOVA", "Chi-Squared"], 1)
q2_6_10 = Q("The total profit for a product based on the amount of money spent on advertising can be represented with the regression equation y = 375 + 87x + 52 where epsilon is 52. What does the number 375 represent?", ["The number 375 is the amount of money spent on advertising that does not explain the amount of profit.", "The number 375 is the amount of money that must be spent on advertising to make any profit.", "The number 375 is the increase in profit per item sold.", "The number 375 is the number of items that must be sold to make a profit"], 2)









q1 = Q("Which of the following is an example of time series data?", ["Annual average housing price in New York", "Batting average of a baseball player", "Number of trees in Jardin du Luxemburg in Paris", "Number of dolphins in the Pacific Ocean"], 1)
q2 = Q("What is the 25th percentile of the following data set; 1, 3, 3, 4, 5, 6, 6, 7, 8, 8", ["1", "3", "3.5", "5.5"], 2)
q3 = Q("Which of the following is a measure of variability?", ["Variance", "Mode", "Median", "Mean"], 1)
q4 = Q("Which of the following measures of central tendency will always change if a single value in the data changes?", ["All of the above", "Mean", "Median", "Mode"], 2)
q5 = Q("Which of the following data sets has a mean of 10 and standard deviation of 0?", ["10, 10, 10", "15, 15, 15", "0, 0, 0", "0, 10, 20"], 1)
q6 = Q("What is meta data?", ["The metabolism data in a clinical trial", "It’s the data about data", "Data about metal fatigue", "The data about metamorphism"], 2)
q7 = Q("Which of the following is an example of categorical data?", ["Length of the river Nile", "Mode of travel to work", "Number of fire hydrants in a city", "Number of children at a kindergarten"], 2)
q8 = Q("Median represents a value in the data set where:", ["Most observations are negative", "Half of the observations are known and the other half not known", "Most observations are positive", "Half of the observations are above the median and the other half below it"], 4)
q9 = Q("If the variance of a dataset is correctly computed with the formula using (n – 1) in the denominator, which of the following option is true?", ["Data is a sample", "Data contains other variables with categorical data", "Data is from an unknown source", "Data is a population"], 1)
q10 = Q("Which of the following is NOT a descriptive statistic?", ["t-test", "Mean", "Median", "Standard Deviation"], 1)



questions = [
q1_1_1_1,
q1_1_1_4,
q1_1_1_5,
q1_1_1_6,
q1_1_1_7,
q1_1_1_8,
q1_1_1_9,
q1_1_1_10,
q1_1_1_11,
q1_1_1_12,
q1_1_1_13,

q1_2_1_1,
q1_2_1_2,
q1_2_1_3,
q1_2_1_4,
q1_2_1_5,
q1_2_1_6,

q1_2_2_1,
q1_2_2_2,
q1_2_2_3,
q1_2_2_4,
q1_2_2_5,
q1_2_2_6,

q1_3_1_1,
q1_3_1_2,
q1_3_1_3,
q1_3_1_4,
q1_3_1_5,
q1_3_1_6,

q1_3_2_1,
q1_3_2_2,
q1_3_2_3,
q1_3_2_4,
q1_3_2_5,

q1_4_1_1,
q1_4_1_2,
q1_4_1_3,
q1_4_1_4,
q1_4_1_5,
q1_4_1_6,
q1_4_1_10,
q1_4_1_11,

q1_5_1_1,
q1_5_1_2,
q1_5_1_3,
q1_5_1_4,
q1_5_1_5,
q1_5_1_6,

q1_6_1_1,
q1_6_1_2,
q1_6_1_3,
q1_6_1_4,

q1_6_2_1,
q1_6_2_2,
q1_6_2_3,
q1_6_2_4,
q1_6_2_5,
q1_6_2_6,
q1_6_2_7,
q1_6_2_8,
q1_6_2_9,

q1_7_1_1,
q1_7_1_2,
q1_7_1_3,
q1_7_1_4,
q1_7_1_5,

q1_8_1_1,
q1_7_1_2,
q1_7_1_3,
q1_7_1_4,
q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
q2_6_1, q2_6_3, q2_6_4, q2_6_5, q2_6_7, q2_6_8, q2_6_9, q2_6_10,
q2_5_1, q2_5_2, q2_5_3, q2_5_4, q2_5_5, q2_5_6, q2_5_7, q2_5_8,

q2_4_1, q2_4_2, q2_4_4, q2_4_5, q2_4_6, q2_4_7, q2_4_8, q2_4_9, q2_4_10,

q2_3_1, q2_3_2, q2_3_3, q2_3_4, q2_3_5, q2_3_6, q2_3_7, q2_3_8, q2_3_9, q2_3_10,


]








# Load HTML template
current_dir = os.path.dirname(__file__) if "__file__" in locals() else ""
template_file = os.path.join(current_dir, "index.html")
with open(template_file, "r") as f:
    html_template = f.read()

# Create Jinja template
template = Template(html_template)

# Render HTML codey
html_output = template.render(questions=questions)

# Define the path to the output HTML file
output_file = os.path.join(current_dir, "index_new.html")

# Save HTML code to a file
with open(output_file, "w") as f:
    f.write(html_output)

print("HTML файл успешно сохранен как index_new.html")