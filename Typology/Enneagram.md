# $\fbox{ENNEAGRAM}$



## 1. Type Definitions


### 1.1 <u>Trait Tables</u>:

| Type |     Core Trait     |     Core Motivation     |          Core Fear          |
| :--: | :----------------: | :---------------------: | :-------------------------: |
|  1   |  Moral absolution  |       Being moral       |        Being corrupt        |
|  2   |    Warm/caring     |      Getting love       |       Devoid of love        |
|  3   |     Ambitious      |      Being admired      |        Being failure        |
|  4   | Self-introspective |      Being unique       |       Being ordinary        |
|  5   |  Knowledge-driven  |     Having autonomy     |      Being interfered       |
|  6   |      Cautious      |       Being safe        |        Being unsafe         |
|  7   |     Optimistic     | Having good experiences | Facing negative experiences |
|  8   |     Dominating     |     Expand control      |       Being powerless       |
|  9   |      Relaxed       |      Having peace       |     Disruption in peace     |


### 1.2 <u>Linear Definitions</u>:

1. People with clear principles about what's good and what's bad, driven by desire to hold up their values and fear being unethical.
2. Warm and pleasing people, driven by desire to give and take love, but fear being disconnected from others.
3. People who are very ambitious with their goals, want to be socially admired, but also fear to be tagged as a failure.
4. Very self-aware people who want to clearly distinguish themselves from the crowd on any grounds, and fear being part of it.
5. Individuals fueled by thirst of knowledge and knowing more, fueled by having autonomy on their work, and fear worldly demands that may stop them from learning or their work.
6. Highly cautious people known for being careful, fueled by desire to be physically and mentally safe, and fear becoming target of worldly chaos.
7. Optimistic people with energy to have all the good experiences, but fear dealing with negative experiences.
8. Highly assertive individuals who are driven by a desire to control as much as of their environment they gain, and fear having lack of control.
9. Laid-back individuals who are fueled by desire to have harmony and peace in their life, but fear facing chaotic demands or mess that disrupts their peace.



## 2. Tendency Scores Meaning


- $1$ - Strongly disagree
- $2$ - Somewhat disagree
- $3$ - Maybe / Unsure
- $4$ - Somewhat agree
- $5$ - Strongly agree



## 3. Method (v1.0.0)


1. Read out the table from **section 1**.
2. Write subject's opinion on relation of each trait, motivation, and fear with them.
3. For each types core trait, motivation, and fear, ask 3 AIs (***Grok***, ***ChatGPT***, ***Gemini***) to score them on range of $[1,5]$.
4. Ask it to normalize each score on scale of $[0,1]$ with $s'=\frac{s-1}{4}$
5. Then find composite for each type with $C=0.40T'+0,50M'+0.10F'$
6. Arrange the scores in descending order.
7. For same scores, compare as per $M>T>F$.
8. Choose the **main enneagram**, its **wing**, and the **tri-type** as per the most common result.

>**<u>NOTE</u>:**
>1. $T$, $M$, and $F$ represent **trait**, **motivation**, and **fear** respectively.
>2. Trait & motivation are weighed higher than fear for being reliable & stable.
>3. Fear is more reactive & volatile, might also distort result.
>4. The particular 3 AIs noted above for objective scoring are there for a reason.



## 4. Example Calculation


1. User reads the table given in **section 1**.
2. Subject's opinion on the traits:

| Type |                                                                                                                                   Core Trait                                                                                                                                   |                                                                                                       Core Motivation                                                                                                        |                                                                                                                       Core Fear                                                                                                                       |
| :--: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  1   |                                                   I don't have a sense of moral absolution within me, because I know that things are on spectrum, not binary. And people taking everything for absolution seem close-minded.                                                   |              Being moral is a great motivator for me, when considering the fact that others don't consider it, but me. And in a cruel world like this, someone with both mastery and principles is great pride.              |                                                   I do fear being immoral sometimes because I am aware about the fact that ego and status blinds the morality. I might become something I despised.                                                   |
|  2   |                                                      I try to be warm, specially with children. I have patience for innocent people who try to do things right. But for stupid and careless adults, I am very very rude.                                                       |           Love is optional and primal. I don't try to gain love of others. I am not against a sense of connection among people, but its never my first priority. It is more of a burden and dependency on others.            |                                                                     I never ever feared, for not being loved. In fact this thing never came to my mind. That's all I have to say.                                                                     |
|  3   |                                               I could be very ambitious, but only thing that stops me from it is the fact that I deep within know, it won't make one forever satisfied. And thanks to the corrupt politics also.                                               |                                     Yeah I within myself want to be admired, but what's the point when people admire those who shouldn't be. And I prefer not to be one of those pricks.                                     |                                                              Fear of failure in itself doesn't scares me. But it could be the consequences of failing, which is in my opinion different.                                                              |
|  4   |                          I have been very self-introspective and filled with all philosophical questions which others never even think of, being NPCs. But its strange that this fire seems to have extinguished when living in noise of this world.                           |                       Being unique is like being a character of a movie. The primary purpose behind my college projects are even to increase self-esteem, choosing difficult niches that others fear.                        |                            I don't have any problem with a healthy society where I am its part. But on a realistic grounds, its a shame to be a sheep in this modern world of corporate slavery and avoidable sufferings.                             |
|  5   |                                               Yes I just love learning. I want to learn about everything, whether its playing difficult games, flying jets, or reading malwares. I am personally mastering systems programming.                                                |                            I work best when I have full autonomy of what I am doing. I have a history of feuds with authorities I feel they don't act efficiently. I prefer doing things my way.                             |                              I fear being forced out of my shelter. And being in environment where your university authorities could harass you by giving pointless classes and penalty otherwise, its almost traumatic.                              |
|  6   |                           I do consider my choices. I use objective facts and metrics instead of how I feel for the moment to decide something. And if using proper engineering procedures even in your personal work is cautious, then count me in.                           |                   I am not exactly driven by a desire to be safe, but its a good propulsion system if we consider it as a strategy game, but sooner growing bored despite the real-world stakes it takes.                    | It's a big fear, specially in modern society. Being a person with ordinary social status means the elites could crush you. And rising cases of fake files by women ruining your life? I decided years ago to not marry or have kids, minimalism life. |
|  7   | At some random points of life I may have a burst of dopamine and good feeling about opportunities in world, which I know within to be a lie. They are just temporary neurological imbalance which are self-diagnosed in upcoming hours. I am more pessimistic than optimistic. |         I don't think about good experiences other than seeing my projects getting popular worldwide. Its my routine to spend time with friends to regulate primal social needs. But I don't actively seek out fun.          |                          That highly depends on what negative experiences here mean. I fear facing situations where I am boxed, but otherwise I have become too used to face situations which others label as bad or scary.                           |
|  8   |                                          I have zero interest in real life domination. In games and sports, its fine, as its fun. But if it leads to harassing people to get your work done or take immoral steps, sorry but I'm out.                                          |                            I seek to expand power in a way, but its more of a strategic gamification of life. And in real-world? Maybe, but I am not mad about it, or its not my first priority.                             |                                    If being powerless means boxed into a helpless situation, yeah its a fear. But in general having less control over the environment, it was never my desire at the first place.                                     |
|  9   |                 I many a times tend to be relaxed. Because I have seen enough of life in my 21 years of breathing to know that we get a choice to be miserable or be carefree. Now I choose the latter to not regret in old age, though I am default serious.                  | Not exactly I seek out peace itself. I seek structure and predictability with logical settings. But absolute peace sounds boring and less challenging, though I have no problem with people who seek it, its understandable. | Life is unpredictable. Anytime any demand could be raised. If it is in my control, I have no problem with it. I fear sudden demands popping up, like how college authorities dragging you mid of your personal work which you can't focus on anymore. |
3. Most generic/central scores is as given below:

| Type | Core Trait | Core Motivation | Core Fear |
| :--: | :--------: | :-------------: | :-------: |
|  1   |     3      |        4        |     3     |
|  2   |     3      |        1        |     1     |
|  3   |     3      |        2        |     2     |
|  4   |     5      |        5        |     4     |
|  5   |     5      |        5        |     5     |
|  6   |     4      |        3        |     5     |
|  7   |     2      |        2        |     3     |
|  8   |     2      |        3        |     3     |
|  9   |     4      |        2        |     4     |
4. Scoring is done as below:

| Type  |  T'  |  M'  |  F'  | **R = 4:5:1** |
| :---: | :--: | :--: | :--: | :-----------: |
| **1** | 0.25 | 0.75 | 0.50 |   **6.25**    |
| **2** | 0.50 | 0.00 | 0.00 |   **2.00**    |
| **3** | 0.50 | 0.25 | 0.25 |   **4.00**    |
| **4** | 1.00 | 1.00 | 0.75 |   **9.75**    |
| **5** | 1.00 | 1.00 | 1.00 |   **10.00**   |
| **6** | 0.75 | 0.50 | 1.00 |   **7.25**    |
| **7** | 0.25 | 0.25 | 0.50 |   **3.25**    |
| **8** | 0.25 | 0.50 | 0.50 |   **4.75**    |
| **9** | 0.75 | 0.25 | 0.75 |   **5.00**    |
5. Composites are calculated as below:

| Type | Composite |
| :--: | :-------: |
|  5   |   0.900   |
|  4   |   0.750   |
|  6   |   0.700   |
|  3   |   0.550   |
|  9   |   0.425   |
|  1   |   0.375   |
|  8   |   0.300   |
|  7   |   0.250   |
|  2   |   0.100   |
6. $5>4>6>9>1>8>3>7>2$
7. Already managed the same scores in previous step.
8. **Type:** 5w4, **Tri-type:** 549

---
