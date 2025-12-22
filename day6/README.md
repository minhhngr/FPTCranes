# Day 6

- left-skewed (negative) distribution
    - mean < median < mode
    - long tail on the left (Data Cluster on the Right)

- right-skewed (positive) distribution
    - mode < median < mean
    - long tail on the right (Data Cluster on the Left)

- normal distribution (Gaussian distribution) - Symmetry
    - mean = median = mode
    - bell-shaped curve: data clusters around the center, tapering off equally on both sides, forming a symmetrical shape.
    - standard deviation (σ) measures the spread of data points around the mean (μ). %68 of data falls within 1σ, %95 within 2σ, and %99.7 within 3σ.
    - normal distribution formula
        - f(x) = (1 / (σ * √(2π))) * e^(-0.5 * ((x - μ) / σ)^2)
        - where:
            - f(x) is the probability density function
            - e is Euler's number (approximately 2.71828)
            - π is Pi (approximately 3.14159)
            - μ is the mean of the distribution
            - σ is the standard deviation of the distribution
            - x is the variable for which we are calculating the probability density
- uniform distribution
    - formula
        - f(x) = 1 / (b - a) for a ≤ x ≤ b
        - f(x) = 0 otherwise
        - where:
            - f(x) is the probability density function
            - a is the minimum value of the distribution
            - b is the maximum value of the distribution
            - x is the variable for which we are calculating the probability density
    - discrete uniform distribution
        - all values within a finite set are equally likely
        - all outcomes are equally likely within a finite set of values
        - probability mass function (PMF) is constant across the set
        - mean = (a + b) / 2
        - variance = ((b - a + 1)² - 1) / 12
        - Applications: rolling a fair die, drawing a card from a well-shuffled deck
    - continuous uniform distribution
        - all outcomes are equally likely within a continuous range [a, b]
        - probability density function (PDF) is constant across the range
        - mean = (a + b) / 2
        - variance = ((b - a)²) / 12
        - Applications: random number generation within a specified range, modeling scenarios with equal likelihood across a continuum

- binomial distribution
    - formula
        - P(X = k) = (n choose k) * p^k * (1 - p)^(n - k)
        - where:
            - P(X = k) is the probability of getting exactly k successes in n trials
            - n is the total number of trials
            - k is the number of successful trials
            - p is the probability of success on an individual trial
            - (n choose k) is the binomial coefficient, calculated as n! / (k! * (n - k)!)
    - mean = n * p
    - variance = n * p * (1 - p)
    - Applications: quality control (defective vs. non-defective items), survey responses (yes/no answers), clinical trials (success/failure of a treatment)
    - Characteristics:
        - Fixed number of trials (n)
        - Each trial is independent
        - Two possible outcomes (success or failure)
        - Constant probability of success (p) across trials
        - Used to model the number of successes in a series of independent Bernoulli trials
        - Examples: flipping a coin multiple times, number of heads in a series of coin tosses

Real-World Decision Making:
- Finance: Modeling stock price movements, risk assessment, and portfolio optimization using normal and binomial distributions.
- Quality Control: Using binomial distribution to monitor defect rates in manufacturing processes.
- Environmental Science: Analyzing climate data and predicting weather patterns with normal distribution.
- Healthcare: Modeling patient outcomes and treatment effectiveness using various probability distributions.
- Marketing: Analyzing customer behavior and preferences using uniform and normal distributions.
- Operations Research: Optimizing supply chain and inventory management using probability distributions.
- Social Sciences: Studying survey data and population characteristics with normal and binomial distributions.
- Engineering: Reliability analysis and failure prediction using probability distributions.
- Machine Learning: Modeling uncertainties in predictions and data distributions using various probability distributions.
- Psychology: Analyzing cognitive test scores and behavioral data with normal distribution.
- Gaming: Designing fair games and understanding player behavior using uniform and binomial distributions.
- Sports Analytics: Evaluating player performance and game outcomes using probability distributions.
- Simulation: Running Monte Carlo simulations to model complex systems and processes using various probability distributions.
- Risk Management: Assessing and mitigating risks in various industries using probability distributions.
- Epidemiology: Modeling the spread of diseases and effectiveness of interventions using probability distributions.
- Supply Chain Management: Forecasting demand and optimizing inventory levels using probability distributions.
- Telecommunications: Modeling network traffic and optimizing resource allocation using probability distributions.
- Artificial Intelligence: Enhancing decision-making processes and uncertainty modeling using probability distributions.
- Gaming Industry: Designing loot drop systems and random events using uniform and binomial distributions.
- Education: Analyzing student performance data and test scores using normal distribution.
- Data Science: Analyzing large datasets and extracting insights using various probability distributions.
- Psychology: Understanding human behavior and cognitive processes using probability distributions.
- Marketing Analytics: Segmenting customers and predicting purchasing behavior using probability distributions.
- Sports Analytics: Evaluating player performance and game strategies using probability distributions.
- Environmental Modeling: Predicting natural phenomena and assessing environmental risks using probability distributions.
- Simulation and Modeling: Creating realistic simulations of complex systems using probability distributions.

Identifying Outliers and Risk:
- Outliers: Data points that deviate significantly from the overall pattern of the data. They can be identified using statistical methods such as Z-scores, IQR (Interquartile Range), or visualizations like box plots.
- Risk Assessment: Probability distributions help in quantifying and managing risks by modeling uncertainties in various scenarios
For example, in finance, normal distribution is used to model stock price movements and assess the risk of investment portfolios. In project management, probability distributions can be used to estimate the likelihood of project completion times and costs, helping to identify potential risks and plan accordingly.

In real-world datastes, values are rarely perfectly symmetrical. Understanding the skewness of data distributions is crucial for accurate data analysis and decision-making. Skewed distributions can impact statistical measures such as mean, median, and mode, leading to potential misinterpretations if not properly accounted for. For instance, in income data, a right-skewed distribution may indicate that a small number of individuals earn significantly more than the majority, affecting average income calculations. Recognizing and addressing skewness allows for more robust statistical analyses and better-informed decisions across various fields, including finance, healthcare, and social sciences.




## Kurtosis

- Kurtosis is a statistical measure that describes the shape of a distribution's tails in relation to its overall shape. It provides insights into the presence of outliers and the extremity of data points in a dataset.
- Excess Kurtosis:
    - Excess kurtosis is calculated by subtracting 3 from the kurtosis value obtained from the formula. This adjustment is made because a normal distribution has a kurtosis of 3, and excess kurtosis allows for easier interpretation.
    - Positive Excess Kurtosis (Leptokurtic):
        - A distribution with positive excess kurtosis has fatter tails and a sharper peak compared to a normal distribution.
        - This indicates a higher likelihood of extreme values or outliers in the dataset.
        - Example: Financial returns often exhibit leptokurtic behavior, indicating a higher risk of extreme market movements.
    - Negative Excess Kurtosis (Platykurtic):
        - A distribution with negative excess kurtosis has thinner tails and a flatter peak compared to a normal distribution.
        - This suggests fewer extreme values or outliers in the dataset.
        - Example: Uniform distributions are platykurtic, as they have equal probabilities across the range and lack extreme values.

Compare Kurtosis Values:
Type | Mesokurtic | Platykurtic | Leptokurtic
--- | --- | --- | ---
Kurtosis Value | (Modeerate) 3 | (Low) < 3 | (High) > 3
Excess Kurtosis | 0 | Negative | Positive
Tailedness | Normal tails | Thin tails | Fat tails
Outliers frequency | Moderate presence | Fewer outliers | More outliers
Example Distributions | Normal distribution | Uniform distribution | Cauchy distribution

formula
- Kurtosis (K) = (n * Σ(xi - x̄)^4) / ((n - 1) * (n - 2) * (n - 3) * s^4)
- Population Kurtosis (K) = (Σ(xi - x̄)^4) / (n * s^4)

- where:
    - n is the number of data points
    - xi represents each individual data point
    - x̄ is the mean of the data points
    - s is the standard deviation of the data points   

Leptokuric: High peak, fat tails (e.g., Cauchy distribution)
Mesokurtic: Moderate peak and tails (e.g., Normal distribution)
Platykurtic: Low peak, thin tails (e.g., Uniform distribution)

Why kurtosis matters:
- Risk Management: High kurtosis indicates a higher likelihood of extreme events, which is crucial for risk assessment in finance and insurance.
- Data Analysis: Understanding kurtosis helps in identifying the presence of outliers and the overall shape of the data distribution, aiding in better statistical modeling.
- Decision Making: Knowledge of kurtosis can inform decisions in various fields, such as quality control, where extreme values may indicate defects or anomalies.
- Not only about average outcomes, but also the likelihood of extreme events.
- highlights the probability of rare but impactful occurrences, serve outcomes
- Higher kurtosis indicates a higher likelihood of extreme events, which is crucial for risk assessment in finance and insurance.
- Common applications:
    - Finance: Modeling asset returns and assessing market risks.
    - Quality Control: Identifying defects in manufacturing processes.
    - Environmental Science: Analyzing extreme weather events.
    - Healthcare: Studying rare disease occurrences and treatment outcomes.


Leptokurtic distributions and risk:
- Leptokurtic distributions have fatter tails and a sharper peak compared to normal distributions
- This indicates a higher likelihood of extreme values or outliers in the dataset.
- In risk management, leptokurtic distributions suggest a greater potential for rare but impactful events
- Fat/heavy tails imply that extreme deviations from the mean are more probable than in normal distributions
- For example, financial returns often exhibit leptokurtic behavior, indicating a higher risk of extreme market movements.

Platykurtic distributions and risk:
- Platykurtic distributions have thinner tails and a flatter peak compared to normal distributions.
- This suggests fewer extreme values or outliers in the dataset.
- In risk management, platykurtic distributions imply a lower likelihood of rare but impactful events
- Thin tails indicate that extreme deviations from the mean are less probable than in normal distributions
- Extreme values are less likely to occur, reducing the risk associated with rare events
- For example, uniform distributions are platykurtic, as they have equal probabilities across the range and lack extreme values.

Real-World Decision Making:
- Finance: Understanding kurtosis helps in modeling asset returns and assessing market risks, enabling better investment decisions.
- Quality Control: Identifying defects in manufacturing processes through kurtosis analysis aids in maintaining product quality.
- Environmental Science: Analyzing extreme weather events using kurtosis informs disaster preparedness and mitigation strategies.
- Healthcare: Studying rare disease occurrences and treatment outcomes with kurtosis analysis supports effective healthcare planning and resource allocation.