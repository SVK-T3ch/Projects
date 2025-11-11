while True:
 q1 = input('Welcome to Palindrome Checker!\nThis app checks whether a set of characters are palindrome.please type ? to know the definition of palindrome.\nWould you like to continue? [y/n/?]: ')
 if q1 == 'y':
  q2 = input('Please type the characters you would like to check: ')
  if q2 != q2[::-1]:
      print('The above is not a palindrome')
  else:
      print('The above is a palindrome')
 elif q1 == 'n':
    print('Thamks for using the program!')
    exit()
 elif q1 == '?':
    print('A palindrome (/ˈpæl. ɪn. droʊm/) is a word, number, phrase, or other sequence of symbols \nthat reads the same backwards as forwards, such as madam or racecar, the date "22/02/2022" and \nthe sentence: "A man, a plan, a canal – Panama".')
 else:
    print('Please enter a valid input')
 while True:
  q2 = input('Would you like to try it again? [y/n]: ').lower()
  if q2 == 'y':
    break
  elif q2 == 'n':
    print('Thamks for using the program!')
    exit()
  else:
    print('Please enter a valid input')
