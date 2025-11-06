# $\fbox{TEMPERAMENTS}$



## 1. Involved Biochemicals


- **<u>Cortisol (C)</u>:** Directs energy from non-essential functions to **alertness** during stress.
- **<u>Dopamine (D)</u>** Motivates a person to **anticipate** for reward.
- **<u>Estrogen (E)</u>:** Drives a female towards **primally healthy** tendencies.
- **<u>Oxytocin (O)</u>:** Fuels emotions that rise through any form of **connection** with others.
- **<u>Serotonin (S)</u>:** **Regulates** moods, emotions, and reaction speeds.
- **<u>Testosterone (T)</u>:** Drives a male towards **primally healthy** tendencies.

>**<u>NOTE</u>:**
> - Androgenecity (A) is testosterone (T) in males, and estrogen (E) in females.



## 2. Metric System


### 2.1 <u>Score Representation</u>:

- $1$: Extreme deficiency
- $2$: Mild deficiency
- $3$: Balanced
- $4$: Slight excessiveness
- $5$: High excessiveness


### 2.2 <u>Scoring Method</u>:

- All the dominant temperament types are scored with a default expectation.
- Blends are just average of the two involved temperaments.
- Fractional values are resolved by rounding-off the value towards the primary temperament.



## 3. Temperamental Scores


|Temperament|Cortisol (C)|Dopamine (D)|Oxytocin (O)|Serotonin (S)|Androgenicity (A)|
|:-|:-:|:-:|:-:|:-:|:-:|
|**Choleric**|3|5|1|2|5|
|**Melancholic**|5|1|3|4|1|
|**Phlegmatic**|1|2|5|5|1|
|**Sanguine**|1|5|3|3|3|



## 4. Procedure (v3.0.0)


1. Read the primary work of each basic biochemical from **section 1**.

2. As per the visible intensity of behavior expected from each of the 5 biochemicals, rate their presence on scale of $[1,5]$.

3. Write down the differences between biochemical points separated by commas, for each temperament on different line.

4. Now apply ***variance*** formulae on difference points with each temperament using:
$$ Var(X)=\frac{1}{N}\sum^{N}_{i=1}(x_{i}-\bar{x})^{2} $$

- $N=5 \text{ (each chemical)}$
- $x = \text{A particular chemical's score for a given temperament}$
- $\bar{x} = \text{Mean of all } x \text{ scores}$

5. Now for each variance point, choose the lowest one as primary temperament type.

6. If the second lowest variance type has a difference $< 0.5$ ($1.0$ being unit to move through types), then its a blend with secondary temperament. Else just dominant primary.

7. If at any point the variance are same, the preference for Jungian introverts (***I***) is in order (opposite for extroverts):

$$ \text{Melancholic > Phlegmatic > Choleric > Sanguine} $$



## 5. Application Example

Let's say we have a test subject with following score on biochemicals:

$$ \text{Cortisol} (C) = 3 $$
$$ \text{Dopamine} (D) = 2 $$
$$ \text{Oxytocin} (O) = 2 $$
$$ \text{Serotonin} (S) = 2 $$
$$ \text{Testosterone} (T) = 2 $$

We will take the same $CDOST$ order of chemicals for differences:

$$ \text{Choleric} (Chol) = [0,-3,1,0,-3] $$
$$ \text{Melancholic} (Mel) = [-2,1,-1,-2,1] $$
$$ \text{Phlegmatic} (Phleg) = [2,0,-3,-3,1] $$
$$ \text{Sanguine} (Sang) = [2,-3,-1,-1,-1] $$

After applying variance $Var(X)$ on these, where $X$ is the temperament:

$$ Var(Chol) = 2.8 $$
$$ Var(Mel) = 1.84 $$
$$ Var(Phleg) = 4.24 $$
$$ Var(Sang) = 2.56 $$

Type with least variance is $Mel$ (**melancholic**) with second lowest as $Sang$ (**sanguine**). But the difference between both is $\ge 0.5$, so its a **melancholic \[dominant\]** type.

>**<u>NOTE</u>:**
> - We use population variance (divide by $N=5$).
> - If you prefer sample variance, document it explicitly.



## 6. Recent Improvements


- Separation of estrogen & testosterone as **androgenicity (A)**.
- Introducing more reliable scores for blends.
- Fixing equal deviations with a preference order & not subjective bias.
- Using standard statistical formulae with proof of work.

---