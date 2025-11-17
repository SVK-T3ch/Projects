print("Welcome to the Mini Quiz!")
while True:
 Difficulty = input("Choose your difficulty [E/m/h]: ").lower()
 if Difficulty == 'e':
  while True:
   Theme = input("What theme would you like to use? \na)History \nb)Geography \nc)English \nd)GK \ne)Science (Biology,Chemistry and Physics):  ").lower()
   if Theme == 'a':
     print("=== HISTORY QUIZ ===")
     print("Answer the following 10 MCQ questions!\n")

     score = 0


     q1 = input('1) Who is known as the "Father of History"?\n'
                'a) Plato\nb) Herodotus\nc) Socrates\nd) Aristotle\nYour answer: ').lower()
     if q1 == 'b':
         score += 1


     q2 = input('2) The Great Wall is located in which country?\n'
                'a) Japan\nb) China\nc) Korea\nd) Mongolia\nYour answer: ').lower()
     if q2 == 'b':
         score += 1


     q3 = input("3) Who discovered America?\n"
                "a) Vasco da Gama\nb) Columbus\nc) Magellan\nd) Cook\nYour answer: ").lower()
     if q3 == 'b':
         score += 1


     q4 = input("4) The Pyramids were built by the people of which ancient civilization?\n"
                "a) Greece\nb) Rome\nc) Egypt\nd) China\nYour answer: ").lower()
     if q4 == 'c':
         score += 1


     q5 = input("5) Who was the first President of the United States?\n"
                "a) Abraham Lincoln\nb) George Washington\nc) Thomas Jefferson\nd) John Adams\nYour answer: ").lower()
     if q5 == 'b':
         score += 1


     q6 = input("6) In which country did the Industrial Revolution begin?\n"
                "a) USA\nb) Germany\nc) France\nd) Britain\nYour answer: ").lower()
     if q6 == 'd':
         score += 1


     q7 = input("7) Who discovered the sea route to India?\n"
                "a) Columbus\nb) Zheng He\nc) Vasco da Gama\nd) Magellan\nYour answer: ").lower()
     if q7 == 'c':
         score += 1


     q8 = input("8) The Roman Empire was centered in which modern country?\n"
                "a) Spain\nb) Italy\nc) Greece\nd) Turkey\nYour answer: ").lower()
     if q8 == 'b':
         score += 1


     q9 = input("9) What was the name of the famous ship on which the Pilgrims came to America?\n"
                "a) Mayflower\nb) Titanic\nc) Santa Maria\nd) Queen Mary\nYour answer: ").lower()
     if q9 == 'a':
         score += 1


     q10 = input("10) Which ruler built the Taj Mahal?\n"
                 "a) Akbar\nb) Aurangzeb\nc) Shah Jahan\nd) Babar\nYour answer: ").lower()
     if q10 == 'c':
         score += 1


     print("\n=== QUIZ FINISHED ===")
     print("Your Score:", score, "/ 10")

     if score == 10:
         print("Outstanding! Perfect score!")
     elif score >= 7:
         print("Great job! You know your history well.")
     elif score >= 4:
         print("Not bad, but you can improve.")
     else:
         print("You need to study a bit more.")
     break
   elif Theme == 'b':
     print("=== GEOGRAPHY QUIZ ===")
     print("Answer the following 10 MCQ questions!\n")

     score = 0

     # Q1
     q1 = input("1) Which is the largest continent?\n"
                "a) Africa\nb) Asia\nc) Europe\nd) Antarctica\nYour answer: ").lower()
     if q1 == 'b':
         score += 1

     # Q2
     q2 = input("2) Which country has the longest coastline in the world?\n"
                "a) Australia\nb) Russia\nc) Canada\nd) USA\nYour answer: ").lower()
     if q2 == 'c':
         score += 1

     # Q3
     q3 = input("3) The Sahara Desert is located on which continent?\n"
                "a) Africa\nb) Asia\nc) South America\nd) Australia\nYour answer: ").lower()
     if q3 == 'a':
         score += 1

     # Q4
     q4 = input("4) What is the longest river in the world?\n"
                "a) Amazon\nb) Yellow River\nc) Nile\nd) Congo\nYour answer: ").lower()
     if q4 == 'c':
         score += 1

     # Q5
     q5 = input("5) Mount Everest lies in which mountain range?\n"
                "a) Alps\nb) Andes\nc) Himalayas\nd) Rockies\nYour answer: ").lower()
     if q5 == 'c':
         score += 1

     # Q6
     q6 = input("6) Which is the smallest country in the world?\n"
                "a) Monaco\nb) Malta\nc) Vatican City\nd) Liechtenstein\nYour answer: ").lower()
     if q6 == 'c':
         score += 1

     # Q7
     q7 = input("7) Which ocean is the deepest?\n"
                "a) Atlantic\nb) Pacific\nc) Indian\nd) Arctic\nYour answer: ").lower()
     if q7 == 'b':
         score += 1

     # Q8
     q8 = input("8) Which country is called the Land of the Rising Sun?\n"
                "a) China\nb) Japan\nc) Thailand\nd) South Korea\nYour answer: ").lower()
     if q8 == 'b':
         score += 1

     # Q9
     q9 = input("9) Which is the largest island in the world?\n"
                "a) Greenland\nb) Madagascar\nc) Borneo\nd) New Guinea\nYour answer: ").lower()
     if q9 == 'a':
         score += 1

     # Q10
     q10 = input("10) The equator passes through which of these countries?\n"
                 "a) India\nb) Mexico\nc) Brazil\nd) Spain\nYour answer: ").lower()
     if q10 == 'c':
         score += 1

     # FINAL SCORE
     print("\n=== QUIZ FINISHED ===")
     print("Your Score:", score, "/ 10")

     if score == 10:
         print("Perfect! Geography master!")
     elif score >= 7:
         print("Great job! Strong geography knowledge.")
     elif score >= 4:
         print("Decent. Keep improving.")
     else:
         print("Needs more practice.")
     break
   elif Theme == 'c':
     print("=== ENGLISH QUIZ ===")
     print("Answer the following 10 MCQ questions!\n")

     score = 0

     # Q1
     q1 = input("1) Choose the correctly spelled word:\n"
                "a) Accomodate\nb) Acommodate\nc) Accommodate\nd) Acommadate\nYour answer: ").lower()
     if q1 == 'c':
         score += 1

     # Q2
     q2 = input("2) What is the plural of 'Child'?\n"
                "a) Childs\nb) Children\nc) Childes\nd) Childrens\nYour answer: ").lower()
     if q2 == 'b':
         score += 1

     # Q3
     q3 = input("3) Choose the synonym of 'Happy':\n"
                "a) Sad\nb) Joyful\nc) Angry\nd) Silent\nYour answer: ").lower()
     if q3 == 'b':
         score += 1

     # Q4
     q4 = input("4) Identify the noun in this sentence: 'The dog barked loudly.'\n"
                "a) barked\nb) loudly\nc) dog\nd) the\nYour answer: ").lower()
     if q4 == 'c':
         score += 1

     # Q5
     q5 = input("5) Which sentence is grammatically correct?\n"
                "a) He don't like tea.\n"
                "b) He doesn't likes tea.\n"
                "c) He doesn't like tea.\n"
                "d) He not likes tea.\nYour answer: ").lower()
     if q5 == 'c':
         score += 1

     # Q6
     q6 = input("6) What is the opposite of 'Brave'?\n"
                "a) Fearless\nb) Cowardly\nc) Strong\nd) Bold\nYour answer: ").lower()
     if q6 == 'b':
         score += 1

     # Q7
     q7 = input("7) Which of these is an adjective?\n"
                "a) Quickly\nb) Happiness\nc) Beautiful\nd) Running\nYour answer: ").lower()
     if q7 == 'c':
         score += 1

     # Q8
     q8 = input("8) Choose the correct article: '___ apple a day keeps the doctor away.'\n"
                "a) A\nb) An\nc) The\nd) No article needed\nYour answer: ").lower()
     if q8 == 'b':
         score += 1

     # Q9
     q9 = input("9) Which word is a verb?\n"
                "a) Jump\nb) Chair\nc) Red\nd) Quickly\nYour answer: ").lower()
     if q9 == 'a':
         score += 1

     # Q10
     q10 = input("10) Convert to past tense: 'She writes a letter.'\n"
                 "a) She wrote a letter.\n"
                 "b) She writed a letter.\n"
                 "c) She writing a letter.\n"
                 "d) She write a letter.\nYour answer: ").lower()
     if q10 == 'a':
         score += 1

     # FINAL SCORE
     print("\n=== QUIZ FINISHED ===")
     print("Your Score:", score, "/ 10")

     if score == 10:
         print("Excellent! Perfect English!")
     elif score >= 7:
         print("Very good! Strong English skills.")
     elif score >= 4:
         print("Not bad. Keep practicing.")
     else:
         print("You need more work on basics.")
     break
   elif Theme == 'd':
     print("=== GENERAL KNOWLEDGE QUIZ ===")
     print("Answer the following 10 MCQ questions!\n")

     score = 0

     # Q1
     q1 = input("1) Who is known as the 'Father of Computers'?\n"
                "a) Alan Turing\nb) Charles Babbage\nc) Bill Gates\nd) Steve Jobs\nYour answer: ").lower()
     if q1 == 'b':
         score += 1

     # Q2
     q2 = input("2) What is the capital of Japan?\n"
                "a) Osaka\nb) Kyoto\nc) Tokyo\nd) Hiroshima\nYour answer: ").lower()
     if q2 == 'c':
         score += 1

     # Q3
     q3 = input("3) Which animal is the largest on Earth?\n"
                "a) Elephant\nb) Blue Whale\nc) Giraffe\nd) Shark\nYour answer: ").lower()
     if q3 == 'b':
         score += 1

     # Q4
     q4 = input("4) How many sides does a hexagon have?\n"
                "a) 5\nb) 6\nc) 7\nd) 8\nYour answer: ").lower()
     if q4 == 'b':
         score += 1

     # Q5
     q5 = input("5) Which country invented pizza?\n"
                "a) France\nb) Italy\nc) Greece\nd) USA\nYour answer: ").lower()
     if q5 == 'b':
         score += 1

     # Q6
     q6 = input("6) How many planets are in our Solar System?\n"
                "a) 7\nb) 8\nc) 9\nd) 10\nYour answer: ").lower()
     if q6 == 'b':
         score += 1

     # Q7
     q7 = input("7) Which gas do plants absorb from the air?\n"
                "a) Oxygen\nb) Hydrogen\nc) Carbon Dioxide\nd) Nitrogen\nYour answer: ").lower()
     if q7 == 'c':
         score += 1

     # Q8
     q8 = input("8) Which day is celebrated as World Environment Day?\n"
                "a) June 5\nb) July 5\nc) April 22\nd) March 3\nYour answer: ").lower()
     if q8 == 'a':
         score += 1

     # Q9
     q9 = input("9) Which is the fastest land animal?\n"
                "a) Cheetah\nb) Lion\nc) Horse\nd) Gazelle\nYour answer: ").lower()
     if q9 == 'a':
         score += 1

     # Q10
     q10 = input("10) How many colors are in a rainbow?\n"
                 "a) 5\nb) 6\nc) 7\nd) 8\nYour answer: ").lower()
     if q10 == 'c':
         score += 1

     # FINAL SCORE
     print("\n=== QUIZ FINISHED ===")
     print("Your Score:", score, "/ 10")

     if score == 10:
         print("Legend! Perfect GK score!")
     elif score >= 7:
         print("Great job! You’re pretty smart.")
     elif score >= 4:
         print("Decent. You can do better!")
     else:
         print("This was rough — time to level up.")
     break

   elif Theme == 'e':
     print("=== SCIENCE QUIZ (EASY MODE) ===")
     print("Answer the following 10 MCQ questions!\n")

     score = 0

     # Q1
     q1 = input("1) What is the closest star to Earth?\n"
                "a) Sirius\nb) Sun\nc) Polaris\nd) Alpha Centauri\nYour answer: ").lower()
     if q1 == 'b':
         score += 1

     # Q2
     q2 = input("2) Which gas do humans need to survive?\n"
                "a) Oxygen\nb) Nitrogen\nc) Carbon Dioxide\nd) Helium\nYour answer: ").lower()
     if q2 == 'a':
         score += 1

     # Q3
     q3 = input("3) Water boils at what temperature (at sea level)?\n"
                "a) 80°C\nb) 100°C\nc) 120°C\nd) 60°C\nYour answer: ").lower()
     if q3 == 'b':
         score += 1

     # Q4
     q4 = input("4) What is the largest organ of the human body?\n"
                "a) Heart\nb) Skin\nc) Liver\nd) Brain\nYour answer: ").lower()
     if q4 == 'b':
         score += 1

     # Q5
     q5 = input("5) Plants make food by which process?\n"
                "a) Photosynthesis\nb) Transpiration\nc) Respiration\nd) Germination\nYour answer: ").lower()
     if q5 == 'a':
         score += 1

     # Q6
     q6 = input("6) Bees collect what from flowers?\n"
                "a) Water\nb) Soil\nc) Nectar\nd) Sand\nYour answer: ").lower()
     if q6 == 'c':
         score += 1

     # Q7
     q7 = input("7) Which planet is known as the Red Planet?\n"
                "a) Mercury\nb) Venus\nc) Mars\nd) Jupiter\nYour answer: ").lower()
     if q7 == 'c':
         score += 1

     # Q8
     q8 = input("8) The main source of energy for Earth is?\n"
                "a) Moon\nb) Sun\nc) Stars\nd) Oceans\nYour answer: ").lower()
     if q8 == 'b':
         score += 1

     # Q9
     q9 = input("9) Which part of a plant absorbs water?\n"
                "a) Leaves\nb) Flower\nc) Stem\nd) Roots\nYour answer: ").lower()
     if q9 == 'd':
         score += 1

     # Q10
     q10 = input("10) Which of these is a solid?\n"
                 "a) Oxygen\nb) Steam\nc) Ice\nd) Carbon dioxide\nYour answer: ").lower()
     if q10 == 'c':
         score += 1

     # FINAL SCORE
     print("\n=== QUIZ FINISHED ===")
     print("Your Score:", score, "/ 10")

     if score == 10:
         print("Legend! Perfect Science score!")
     elif score >= 7:
         print("Great job! You're pretty sharp!")
     elif score >= 4:
         print("Not bad. Keep learning!")
     else:
         print("Tough round — revise your basics.")
     break
   else:
     print('Please enter a valid input')
 elif Difficulty == "m":
   while True:
    Theme = input("What theme would you like to use? \na)History \nb)Geography \nc)English \nd)GK \ne)Science (Biology, Chemistry, Physics):  ").lower()

    # -------------------------------------------------------------
    # ======================= HISTORY (MEDIUM) =====================
    # -------------------------------------------------------------
    if Theme == 'a':
        print("=== HISTORY QUIZ (MEDIUM MODE) ===")
        print("Answer the following 10 MCQ questions!\n")

        score = 0

        q1 = input("1) In which year did World War II begin?\n"
                   "a) 1935\nb) 1939\nc) 1941\nd) 1945\nYour answer: ").lower()
        if q1 == 'b':
            score += 1

        q2 = input("2) Who was the first Mughal Emperor?\n"
                   "a) Akbar\nb) Babur\nc) Humayun\nd) Jahangir\nYour answer: ").lower()
        if q2 == 'b':
            score += 1

        q3 = input("3) The French Revolution began in which year?\n"
                   "a) 1776\nb) 1789\nc) 1804\nd) 1815\nYour answer: ").lower()
        if q3 == 'b':
            score += 1

        q4 = input("4) Who wrote the book 'Arthashastra'?\n"
                   "a) Chanakya\nb) Kalidasa\nc) Banabhatta\nd) Aryabhata\nYour answer: ").lower()
        if q4 == 'a':
            score += 1

        q5 = input("5) Which empire built Machu Picchu?\n"
                   "a) Aztec\nb) Roman\nc) Inca\nd) Maya\nYour answer: ").lower()
        if q5 == 'c':
            score += 1

        q6 = input("6) Who led the Salt March in 1930?\n"
                   "a) Sardar Patel\nb) Mahatma Gandhi\nc) Nehru\nd) Subhash Bose\nYour answer: ").lower()
        if q6 == 'b':
            score += 1

        q7 = input("7) Which treaty ended World War I?\n"
                   "a) Treaty of Vienna\nb) Treaty of Paris\nc) Treaty of Versailles\nd) Treaty of Ghent\nYour answer: ").lower()
        if q7 == 'c':
            score += 1

        q8 = input("8) What was the capital of the Maurya Empire?\n"
                   "a) Pataliputra\nb) Taxila\nc) Ujjain\nd) Kannauj\nYour answer: ").lower()
        if q8 == 'a':
            score += 1

        q9 = input("9) Who discovered the sea route to India?\n"
                   "a) Columbus\nb) Vasco da Gama\nc) Magellan\nd) Cook\nYour answer: ").lower()
        if q9 == 'b':
            score += 1

        q10 = input("10) The Renaissance began in which country?\n"
                    "a) France\nb) England\nc) Italy\nd) Germany\nYour answer: ").lower()
        if q10 == 'c':
            score += 1

        # FINAL SCORE
        print("\n=== QUIZ FINISHED ===")
        print("Your Score:", score, "/ 10")

        if score == 10:
            print("Outstanding! Strong historical mastery!")
        elif score >= 7:
            print("Great job! Solid knowledge.")
        elif score >= 4:
            print("Decent. Keep learning more!")
        else:
            print("You need more practice on history.")
        break



    # -------------------------------------------------------------
    # ===================== GEOGRAPHY (MEDIUM) =====================
    # -------------------------------------------------------------
    elif Theme == 'b':
        print("=== GEOGRAPHY QUIZ (MEDIUM MODE) ===")
        print("Answer the following 10 MCQ questions!\n")

        score = 0

        q1 = input("1) Which river is the longest in Asia?\n"
                   "a) Yangtze\nb) Yellow River\nc) Indus\nd) Mekong\nYour answer: ").lower()
        if q1 == 'a':
            score += 1

        q2 = input("2) What is the deepest point in the Earth's oceans?\n"
                   "a) Tonga Trench\nb) Mariana Trench\nc) Java Trench\nd) Philippine Trench\nYour answer: ").lower()
        if q2 == 'b':
            score += 1

        q3 = input("3) Which country has the most natural lakes?\n"
                   "a) USA\nb) Russia\nc) Canada\nd) Finland\nYour answer: ").lower()
        if q3 == 'c':
            score += 1

        q4 = input("4) Which desert is the largest hot desert in the world?\n"
                   "a) Arabian\nb) Gobi\nc) Sahara\nd) Kalahari\nYour answer: ").lower()
        if q4 == 'c':
            score += 1

        q5 = input("5) What is the largest peninsula in the world?\n"
                   "a) Indo-China\nb) Arabian Peninsula\nc) Alaska\n"
                   "d) Scandinavian Peninsula\nYour answer: ").lower()
        if q5 == 'b':
            score += 1

        q6 = input("6) Which line divides Earth into the Northern and Southern Hemispheres?\n"
                   "a) Tropic of Cancer\nb) Equator\nc) Prime Meridian\nd) Tropic of Capricorn\nYour answer: ").lower()
        if q6 == 'b':
            score += 1

        q7 = input("7) Which country has the highest population density?\n"
                   "a) Bangladesh\nb) India\nc) Japan\nd) South Korea\nYour answer: ").lower()
        if q7 == 'a':
            score += 1

        q8 = input("8) Which African river is the main tributary of the Nile?\n"
                   "a) Congo\nb) Niger\nc) Blue Nile\nd) Limpopo\nYour answer: ").lower()
        if q8 == 'c':
            score += 1

        q9 = input("9) The Great Barrier Reef is located in which country?\n"
                   "a) Australia\nb) Mexico\nc) South Africa\nd) Indonesia\nYour answer: ").lower()
        if q9 == 'a':
            score += 1

        q10 = input("10) Which country is the largest producer of coffee?\n"
                    "a) Vietnam\nb) Brazil\nc) Colombia\nd) Ethiopia\nYour answer: ").lower()
        if q10 == 'b':
            score += 1

        # FINAL SCORE
        print("\n=== QUIZ FINISHED ===")
        print("Your Score:", score, "/ 10")

        if score == 10:
            print("Excellent! Geography expert.")
        elif score >= 7:
            print("Very good performance!")
        elif score >= 4:
            print("Not bad. Keep improving.")
        else:
            print("Needs more practice.")
        break



    # -------------------------------------------------------------
    # ======================== ENGLISH (MEDIUM) ====================
    # -------------------------------------------------------------
    elif Theme == 'c':
        print("=== ENGLISH QUIZ (MEDIUM MODE) ===")
        print("Answer the following 10 MCQ questions!\n")

        score = 0

        q1 = input("1) Identify the figure of speech: 'He is a shining star.'\n"
                   "a) Metaphor\nb) Simile\nc) Personification\nd) Irony\nYour answer: ").lower()
        if q1 == 'a':
            score += 1

        q2 = input("2) Choose the correct indirect speech:\n"
                   "'He said, \"I am tired.\"'\n"
                   "a) He said he is tired.\n"
                   "b) He said that he was tired.\n"
                   "c) He told that he is tired.\n"
                   "d) He says he was tired.\nYour answer: ").lower()
        if q2 == 'b':
            score += 1

        q3 = input("3) Which sentence uses correct punctuation?\n"
                   "a) Its raining, lets go inside.\n"
                   "b) It's raining, let's go inside.\n"
                   "c) It's raining lets go inside.\n"
                   "d) Its raining let's go inside.\nYour answer: ").lower()
        if q3 == 'b':
            score += 1

        q4 = input("4) Choose the synonym of 'Reluctant':\n"
                   "a) Eager\nb) Unwilling\nc) Certain\nd) Strong\nYour answer: ").lower()
        if q4 == 'b':
            score += 1

        q5 = input("5) Identify the tense: 'She had been studying for hours.'\n"
                   "a) Past Perfect\nb) Present Perfect\nc) Past Perfect Continuous\n"
                   "d) Present Continuous\nYour answer: ").lower()
        if q5 == 'c':
            score += 1

        q6 = input("6) Choose the correct spelling:\n"
                   "a) Embarrassment\nb) Embarasment\nc) Embarrasment\nd) Embarassment\nYour answer: ").lower()
        if q6 == 'a':
            score += 1

        q7 = input("7) Which is a compound sentence?\n"
                   "a) I came, I saw, I conquered.\n"
                   "b) She ran quickly.\n"
                   "c) Although he tried, he failed.\n"
                   "d) I wanted to play but it was raining.\nYour answer: ").lower()
        if q7 == 'd':
            score += 1

        q8 = input("8) Choose the antonym of 'Scarce':\n"
                   "a) Rare\nb) Plenty\nc) Limited\nd) Few\nYour answer: ").lower()
        if q8 == 'b':
            score += 1

        q9 = input("9) Identify the noun form of 'Decide':\n"
                   "a) Decisive\nb) Decider\nc) Decision\nd) Deciding\nYour answer: ").lower()
        if q9 == 'c':
            score += 1

        q10 = input("10) Which sentence is in active voice?\n"
                    "a) The ball was thrown by John.\n"
                    "b) John threw the ball.\n"
                    "c) The ball is being thrown.\n"
                    "d) The ball will be thrown.\nYour answer: ").lower()
        if q10 == 'b':
            score += 1

        # FINAL SCORE
        print("\n=== QUIZ FINISHED ===")
        print("Your Score:", score, "/ 10")

        if score == 10:
            print("Outstanding! Perfect English skills.")
        elif score >= 7:
            print("Great performance!")
        elif score >= 4:
            print("Decent. Keep practicing.")
        else:
            print("Needs more study.")
        break



    # -------------------------------------------------------------
    # ===================== GENERAL KNOWLEDGE (MEDIUM) =============
    # -------------------------------------------------------------
    elif Theme == 'd':
        print("=== GENERAL KNOWLEDGE QUIZ (MEDIUM MODE) ===")
        print("Answer the following 10 MCQ questions!\n")

        score = 0

        q1 = input("1) Who invented the World Wide Web?\n"
                   "a) Tim Berners-Lee\nb) Bill Gates\nc) Vint Cerf\nd) Dennis Ritchie\nYour answer: ").lower()
        if q1 == 'a':
            score += 1

        q2 = input("2) Which country hosted the 2020 Summer Olympics?\n"
                   "a) China\nb) Japan\nc) Brazil\nd) UK\nYour answer: ").lower()
        if q2 == 'b':
            score += 1

        q3 = input("3) Which element has the symbol 'Fe'?\n"
                   "a) Lead\nb) Iron\nc) Fluorine\nd) Tin\nYour answer: ").lower()
        if q3 == 'b':
            score += 1

        q4 = input("4) Which continent has the most countries?\n"
                   "a) Europe\nb) South America\nc) Africa\nd) Asia\nYour answer: ").lower()
        if q4 == 'c':
            score += 1

        q5 = input("5) Who painted the Mona Lisa?\n"
                   "a) Picasso\nb) Michelangelo\nc) Leonardo da Vinci\nd) Raphael\nYour answer: ").lower()
        if q5 == 'c':
            score += 1

        q6 = input("6) What is the currency of Russia?\n"
                   "a) Yen\nb) Rupee\nc) Ruble\nd) Peso\nYour answer: ").lower()
        if q6 == 'c':
            score += 1

        q7 = input("7) Which country developed the first nuclear bomb?\n"
                   "a) Germany\nb) USA\nc) Russia\nd) UK\nYour answer: ").lower()
        if q7 == 'b':
            score += 1

        q8 = input("8) Where is the headquarters of the UN located?\n"
                   "a) Geneva\nb) New York\nc) Paris\nd) London\nYour answer: ").lower()
        if q8 == 'b':
            score += 1

        q9 = input("9) Which planet has the most moons?\n"
                   "a) Earth\nb) Jupiter\nc) Saturn\nd) Neptune\nYour answer: ").lower()
        if q9 == 'c':
            score += 1

        q10 = input("10) Who is known as the Missile Man of India?\n"
                    "a) C.V. Raman\nb) APJ Abdul Kalam\nc) Homi Bhabha\nd) Vikram Sarabhai\nYour answer: ").lower()
        if q10 == 'b':
            score += 1

        # FINAL SCORE
        print("\n=== QUIZ FINISHED ===")
        print("Your Score:", score, "/ 10")

        if score == 10:
            print("Legend! Outstanding performance!")
        elif score >= 7:
            print("Great job! Solid GK.")
        elif score >= 4:
            print("Decent attempt.")
        else:
            print("Needs improvement! Keep learning.")
        break



    # -------------------------------------------------------------
    # ===================== SCIENCE (MEDIUM MODE) =================
    # -------------------------------------------------------------
    elif Theme == 'e':
        print("=== SCIENCE QUIZ (MEDIUM MODE) ===")
        print("Answer the following 10 MCQ questions!\n")

        score = 0

        q1 = input("1) What is the chemical formula of washing soda?\n"
                   "a) NaHCO₃\nb) Na₂CO₃·10H₂O\nc) CaCO₃\nd) NaOH\nYour answer: ").lower()
        if q1 == 'b':
            score += 1

        q2 = input("2) Which part of the brain controls balance?\n"
                   "a) Cerebrum\nb) Cerebellum\nc) Medulla\nd) Pons\nYour answer: ").lower()
        if q2 == 'b':
            score += 1

        q3 = input("3) What is the SI unit of force?\n"
                   "a) Pascal\nb) Joule\nc) Newton\nd) Watt\nYour answer: ").lower()
        if q3 == 'c':
            score += 1

        q4 = input("4) Which gas is used in the Haber process?\n"
                   "a) Oxygen\nb) Nitrogen\nc) Helium\nd) Chlorine\nYour answer: ").lower()
        if q4 == 'b':
            score += 1

        q5 = input("5) Which mirror is used in rear-view mirrors of vehicles?\n"
                   "a) Concave\nb) Convex\nc) Plane\nd) Parabolic\nYour answer: ").lower()
        if q5 == 'b':
            score += 1

        q6 = input("6) Which organelle is known as the powerhouse of the cell?\n"
                   "a) Nucleus\nb) Mitochondria\nc) Ribosome\nd) Golgi apparatus\nYour answer: ").lower()
        if q6 == 'b':
            score += 1

        q7 = input("7) The rate of change of velocity is called?\n"
                   "a) Speed\nb) Momentum\nc) Acceleration\nd) Power\nYour answer: ").lower()
        if q7 == 'c':
            score += 1

        q8 = input("8) What is the pH of pure water?\n"
                   "a) 5\nb) 6\nc) 7\nd) 8\nYour answer: ").lower()
        if q8 == 'c':
            score += 1

        q9 = input("9) Which disease is caused by vitamin D deficiency?\n"
                   "a) Scurvy\nb) Rickets\nc) Goitre\nd) Anaemia\nYour answer: ").lower()
        if q9 == 'b':
            score += 1

        q10 = input("10) What type of bond is formed by sharing of electrons?\n"
                    "a) Ionic\nb) Metallic\nc) Covalent\nd) Hydrogen\nYour answer: ").lower()
        if q10 == 'c':
            score += 1

        # FINAL SCORE
        print("\n=== QUIZ FINISHED ===")
        print("Your Score:", score, "/ 10")

        if score == 10:
            print("Brilliant! Strong scientific understanding!")
        elif score >= 7:
            print("Great job! Good concepts.")
        elif score >= 4:
            print("Decent, but revise a bit more.")
        else:
            print("Weak attempt — brush up your basics.")
        break

    else:
        print("Please enter a valid input.")
 elif Difficulty == "h":
  while True:
   Theme = input("Choose theme for HARD MODE: \na)History \nb)Geography \nc)English \nd)GK \ne)Science: ").lower()
   if Theme == 'a':
    print("=== HISTORY QUIZ (HARD / COLLEGE LEVEL) ===")
    print("Answer the following 10 MCQ questions!\n")

    score = 0

    q1 = input("1) The Treaty of Westphalia (1648) ended which war?\n"
               "a) Hundred Years' War\nb) Thirty Years' War\nc) War of Roses\nd) Napoleonic Wars\nYour answer: ").lower()
    if q1 == 'b':
        score += 1

    q2 = input("2) Who wrote the historical text 'The Muqaddimah'?\n"
               "a) Ibn Battuta\nb) Al-Tabari\nc) Ibn Khaldun\nd) Al-Biruni\nYour answer: ").lower()
    if q2 == 'c':
        score += 1

    q3 = input("3) Which empire used the administrative system known as 'Satrapies'?\n"
               "a) Roman Empire\nb) Persian Achaemenid Empire\nc) Ottoman Empire\nd) Byzantine Empire\nYour answer: ").lower()
    if q3 == 'b':
        score += 1

    q4 = input("4) The Meiji Restoration (1868) transformed which country?\n"
               "a) Korea\nb) China\nc) Japan\nd) Vietnam\nYour answer: ").lower()
    if q4 == 'c':
        score += 1

    q5 = input("5) Who discovered the Indus Valley Civilization?\n"
               "a) Alexander Cunningham\nb) John Marshall\nc) Mortimer Wheeler\nd) Rakhaldas Banerjee\nYour answer: ").lower()
    if q5 == 'd':
        score += 1

    q6 = input("6) The Battle of Hastings (1066) established which ruler on the English throne?\n"
               "a) Richard I\nb) William the Conqueror\nc) Henry II\nd) Alfred the Great\nYour answer: ").lower()
    if q6 == 'b':
        score += 1

    q7 = input("7) 'Pax Romana' refers to:\n"
               "a) Rome’s civil war period\nb) A 200-year peace period in Rome\nc) Rome’s expansion into Asia\nd) Decline of the Roman Senate\nYour answer: ").lower()
    if q7 == 'b':
        score += 1

    q8 = input("8) Who was the founder of the Maurya Empire?\n"
               "a) Bindusara\nb) Ashoka\nc) Chandragupta Maurya\nd) Chanakya\nYour answer: ").lower()
    if q8 == 'c':
        score += 1

    q9 = input("9) The Renaissance began in which Italian city-state?\n"
               "a) Venice\nb) Florence\nc) Rome\nd) Milan\nYour answer: ").lower()
    if q9 == 'b':
        score += 1

    q10 = input("10) The 'Domesday Book' was commissioned by whom?\n"
                "a) Edward I\nb) Henry VIII\nc) William the Conqueror\nd) King John\nYour answer: ").lower()
    if q10 == 'c':
        score += 1

    print("\n=== QUIZ FINISHED ===")
    print("Your Score:", score, "/ 10")

    if score == 10:
        print("Exceptional! You absolutely dominate history.")
    elif score >= 7:
        print("Strong performance! Excellent historical understanding.")
    elif score >= 4:
        print("Decent, but deeper study will help.")
    else:
        print("This level is tough — keep learning!")
    break
   elif Theme == 'b':
      print("=== GEOGRAPHY QUIZ (HARD / COLLEGE LEVEL) ===")
      print("Answer the following 10 MCQ questions!\n")

      score = 0

      q1 = input("1) What is the deepest point in the Earth's oceans?\n"
                 "a) Tonga Trench\nb) Puerto Rico Trench\nc) Mariana Trench\nd) Java Trench\nYour answer: ").lower()
      if q1 == 'c':
          score += 1

      q2 = input("2) Which river has the largest drainage basin in the world?\n"
                 "a) Congo\nb) Nile\nc) Amazon\nd) Mississippi\nYour answer: ").lower()
      if q2 == 'c':
          score += 1

      q3 = input("3) The concept of 'Continental Drift' was proposed by:\n"
                 "a) James Hutton\nb) Alfred Wegener\nc) Charles Lyell\nd) Harry Hess\nYour answer: ").lower()
      if q3 == 'b':
          score += 1

      q4 = input("4) What type of plate boundary forms the Himalayas?\n"
                 "a) Divergent\nb) Convergent (Continental-Continental)\n"
                 "c) Transform\nd) Convergent (Oceanic-Continental)\nYour answer: ").lower()
      if q4 == 'b':
          score += 1

      q5 = input("5) Which country has the highest number of active volcanoes?\n"
                 "a) Japan\nb) Indonesia\nc) Chile\nd) USA\nYour answer: ").lower()
      if q5 == 'b':
          score += 1

      q6 = input("6) What is the largest hot desert in the world?\n"
                 "a) Gobi\nb) Sahara\nc) Arabian Desert\nd) Kalahari\nYour answer: ").lower()
      if q6 == 'b':
          score += 1

      q7 = input("7) The 'Ring of Fire' is located around which ocean?\n"
                 "a) Atlantic\nb) Indian\nc) Pacific\nd) Arctic\nYour answer: ").lower()
      if q7 == 'c':
          score += 1

      q8 = input("8) Which climate classification system is most widely used?\n"
                 "a) Köppen\nb) Thornthwaite\nc) Bergeron\nd) Strahler\nYour answer: ").lower()
      if q8 == 'a':
          score += 1

      q9 = input("9) The longest mountain range in the world is:\n"
                 "a) Rockies\nb) Andes\nc) Himalayas\nd) Alps\nYour answer: ").lower()
      if q9 == 'b':
          score += 1

      q10 = input("10) Which country has the highest Human Development Index (HDI)?\n"
                  "a) Switzerland\nb) Norway\nc) Iceland\nd) Denmark\nYour answer: ").lower()
      if q10 == 'b':
          score += 1

      print("\n=== QUIZ FINISHED ===")
      print("Your Score:", score, "/ 10")

      if score == 10:
          print("Outstanding! You understand advanced geography concepts.")
      elif score >= 7:
          print("Very strong — great job at this difficulty.")
      elif score >= 4:
          print("Decent attempt. Hard mode is challenging.")
      else:
          print("Study deeper — this level is unforgiving.")
      break
   elif Theme == 'c':
      print("=== ENGLISH QUIZ (HARD / COLLEGE LEVEL) ===")
      print("Answer the following 10 MCQ questions!\n")

      score = 0

      q1 = input("1) Identify the figure of speech: 'The silence was deafening.'\n"
                 "a) Oxymoron\nb) Hyperbole\nc) Metaphor\nd) Paradox\nYour answer: ").lower()
      if q1 == 'b':
          score += 1

      q2 = input("2) Choose the grammatically correct sentence:\n"
                 "a) Neither of the answers are correct.\n"
                 "b) Neither of the answers is correct.\n"
                 "c) Neither the answers is correct.\n"
                 "d) Neither answers is correct.\nYour answer: ").lower()
      if q2 == 'b':
          score += 1

      q3 = input("3) What is the meaning of the word 'Ubiquitous'?\n"
                 "a) Rare\nb) Found everywhere\nc) Hidden\nd) Dangerous\nYour answer: ").lower()
      if q3 == 'b':
          score += 1

      q4 = input("4) Identify the clause type: 'Although he was tired, he continued working.'\n"
                 "a) Noun clause\nb) Relative clause\nc) Adverbial clause\nd) Independent clause\nYour answer: ").lower()
      if q4 == 'c':
          score += 1

      q5 = input("5) Which of the following is an example of a gerund?\n"
                 "a) Running is fun.\n"
                 "b) I will run tomorrow.\n"
                 "c) He ran quickly.\n"
                 "d) She is run.\nYour answer: ").lower()
      if q5 == 'a':
          score += 1

      q6 = input("6) Who wrote the epic poem 'Paradise Lost'?\n"
                 "a) John Milton\nb) Alexander Pope\nc) Geoffrey Chaucer\nd) William Wordsworth\nYour answer: ").lower()
      if q6 == 'a':
          score += 1

      q7 = input("7) A word that is similar in meaning to another word is called:\n"
                 "a) Antonym\nb) Homonym\nc) Synonym\nd) Pseudonym\nYour answer: ").lower()
      if q7 == 'c':
          score += 1

      q8 = input("8) Identify the sentence type: 'How beautiful the night is!'\n"
                 "a) Interrogative\nb) Exclamatory\nc) Imperative\nd) Declarative\nYour answer: ").lower()
      if q8 == 'b':
          score += 1

      q9 = input("9) Choose the correct passive voice:\n"
                 "'The committee approved the proposal.'\n"
                 "a) The proposal is approved by the committee.\n"
                 "b) The proposal was approved by the committee.\n"
                 "c) The proposal has been approved by the committee.\n"
                 "d) The proposal had been approved by the committee.\nYour answer: ").lower()
      if q9 == 'b':
          score += 1

      q10 = input("10) The term 'iambic pentameter' refers to:\n"
                  "a) 5 stressed syllables per line\n"
                  "b) 10 unstressed syllables per line\n"
                  "c) 5 iambs per line\nd) 10 iambs per line\nYour answer: ").lower()
      if q10 == 'c':
          score += 1

      print("\n=== QUIZ FINISHED ===")
      print("Your Score:", score, "/ 10")

      if score == 10:
          print("Amazing! You’ve mastered advanced English.")
      elif score >= 7:
          print("Strong work — excellent English knowledge.")
      elif score >= 4:
          print("Not bad, but this level demands more depth.")
      else:
          print("Tough set — study advanced grammar and literature.")
      break
   elif Theme == 'd':
      print("=== GENERAL KNOWLEDGE QUIZ (HARD / COLLEGE LEVEL) ===")
      print("Answer the following 10 MCQ questions!\n")

      score = 0

      q1 = input("1) Which element has the highest electrical conductivity?\n"
                 "a) Gold\nb) Copper\nc) Silver\nd) Aluminum\nYour answer: ").lower()
      if q1 == 'c':
          score += 1

      q2 = input("2) In which year was the United Nations founded?\n"
                 "a) 1919\nb) 1945\nc) 1950\nd) 1939\nYour answer: ").lower()
      if q2 == 'b':
          score += 1

      q3 = input("3) Who invented the World Wide Web?\n"
                 "a) Bill Gates\nb) Vint Cerf\nc) Tim Berners-Lee\nd) Dennis Ritchie\nYour answer: ").lower()
      if q3 == 'c':
          score += 1

      q4 = input("4) What is the full form of GDP?\n"
                 "a) Gross Domestic Product\nb) General Domestic Price\nc) Global Demand Price\nd) Gross Demand Product\nYour answer: ").lower()
      if q4 == 'a':
          score += 1

      q5 = input("5) Nobel Prizes are awarded in how many categories?\n"
                 "a) 5\nb) 6\nc) 7\nd) 8\nYour answer: ").lower()
      if q5 == 'b':
          score += 1

      q6 = input("6) Which country has the largest proven oil reserves?\n"
                 "a) Saudi Arabia\nb) Venezuela\nc) Iran\nd) Iraq\nYour answer: ").lower()
      if q6 == 'b':
          score += 1

      q7 = input("7) The currency of South Korea is:\n"
                 "a) Yen\nb) Won\nc) Yuan\nd) Ringgit\nYour answer: ").lower()
      if q7 == 'b':
          score += 1

      q8 = input("8) Which is the largest airline in the world by fleet size?\n"
                 "a) Emirates\nb) Delta Airlines\nc) American Airlines\nd) Lufthansa\nYour answer: ").lower()
      if q8 == 'c':
          score += 1

      q9 = input("9) The ‘Brexit’ referendum took place in:\n"
                 "a) 2014\nb) 2016\nc) 2018\nd) 2020\nYour answer: ").lower()
      if q9 == 'b':
          score += 1

      q10 = input("10) Who is the first woman to win a Nobel Prize?\n"
                  "a) Mother Teresa\nb) Rosalind Franklin\nc) Marie Curie\nd) Ada Lovelace\nYour answer: ").lower()
      if q10 == 'c':
          score += 1

      print("\n=== QUIZ FINISHED ===")
      print("Your Score:", score, "/ 10")

      if score == 10:
          print("Brilliant! Outstanding GK knowledge!")
      elif score >= 7:
          print("Great job! Strong general awareness.")
      elif score >= 4:
          print("Not bad, but there’s room for improvement.")
      else:
          print("Hard mode hits hard — expand your GK base.")
      break
   elif Theme == 'e':
      print("=== SCIENCE QUIZ (HARD / COLLEGE LEVEL) ===")
      print("Answer the following 10 MCQ questions!\n")

      score = 0

      q1 = input("1) Which law states that entropy of an isolated system always increases?\n"
                 "a) First law of thermodynamics\nb) Second law\nc) Third law\nd) Zeroth law\nYour answer: ").lower()
      if q1 == 'b':
          score += 1

      q2 = input("2) The pH of human blood is approximately:\n"
                 "a) 5.5\nb) 6.2\nc) 7.4\nd) 8.1\nYour answer: ").lower()
      if q2 == 'c':
          score += 1

      q3 = input("3) In genetics, the term 'epistasis' refers to:\n"
                 "a) One gene masking the effect of another\nb) Multiple alleles in a locus\nc) Crossing over\nd) Mutation in sex chromosomes\nYour answer: ").lower()
      if q3 == 'a':
          score += 1

      q4 = input("4) Which particle is responsible for the strong nuclear force?\n"
                 "a) Photon\nb) Gluon\nc) Boson\nd) Neutrino\nYour answer: ").lower()
      if q4 == 'b':
          score += 1

      q5 = input("5) The chemical formula of bleaching powder is:\n"
                 "a) CaOCl₂\nb) CaCl₂\nc) Ca(OH)₂\nd) CaCO₃\nYour answer: ").lower()
      if q5 == 'a':
          score += 1

      q6 = input("6) Which organelle is responsible for protein synthesis?\n"
                 "a) Lysosome\nb) Ribosome\nc) Golgi apparatus\nd) Mitochondria\nYour answer: ").lower()
      if q6 == 'b':
          score += 1

      q7 = input("7) The Heisenberg Uncertainty Principle applies to:\n"
                 "a) Position and velocity\nb) Mass and charge\nc) Temperature and pressure\nd) Energy and colour\nYour answer: ").lower()
      if q7 == 'a':
          score += 1

      q8 = input("8) Which of the following is NOT a greenhouse gas?\n"
                 "a) Methane\nb) Nitrous oxide\nc) Ozone\nd) Helium\nYour answer: ").lower()
      if q8 == 'd':
          score += 1

      q9 = input("9) What is the SI unit of electric capacitance?\n"
                 "a) Weber\nb) Henry\nc) Farad\nd) Tesla\nYour answer: ").lower()
      if q9 == 'c':
          score += 1

      q10 = input("10) Which process produces the most ATP in cellular respiration?\n"
                  "a) Glycolysis\nb) Fermentation\nc) Electron transport chain\nd) Krebs cycle\nYour answer: ").lower()
      if q10 == 'c':
          score += 1

      print("\n=== QUIZ FINISHED ===")
      print("Your Score:", score, "/ 10")

      if score == 10:
          print("Incredible! You mastered college-level science.")
      elif score >= 7:
          print("Excellent performance — impressive knowledge.")
      elif score >= 4:
          print("Decent, but strengthen your fundamentals.")
      else:
          print("Hard mode is brutal — keep studying!")
      break
 while True:
  WTA = input("Do you wanna try again? [Y/n]").lower()
  if WTA == 'y':
      break
  elif WTA == 'n':
      print("Thanks for using the program!")
      exit()
  else:
      print("Please enter a valid input")
