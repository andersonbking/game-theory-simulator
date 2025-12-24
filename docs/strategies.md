Here is a list of the implemented strategies you can choose to run in the simulation:

1. Cooperate

   ALWAYS cooperate

2. Defect
   
   ALWAYS defect

3. Grim (aka. Permanent Retaliation)
   
   Starts by cooperating and continues to cooperate as long as the opponent does the same. If the opponent defects, the      agent will permanently defect for the remainder of the rounds.

4. Tit-for-Tat (aka. Copycat)
   
   Cooperates in the first round and then copies the opponent's previous moves in the next rounds. (Tit-for-Tat              cooperates, other agent defects. Next round -> Tit-for-Tat defects)

5. Suspicious Tit-for-Tat (aka. stft)
   
   Defects in the first round, and then follows the rules of regular Tit-for-Tat.

6. Cooperate For Defect

   First, the agent defects, but will start cooperating if both agents defect.

7. Random
    
   Randomly chooses to defect or cooperate.

8. Two Tits for Tat (aka. 2tft)

   It defects twice after being defected against, otherwise cooperating.

9. Gradual

   Increasingly adds to a string of defections if the opponent continues to defect, then will cooperate once the string      is finished.
