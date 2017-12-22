# geographic quiz
# store game questions and answers in dict
game_data = {
   'easy': {
        'quiz': ("China has _1_ provinces (including municipalities). The capital of China is _2_, "
                 "where the 2008 Olympic Games is held. The nearest province to _2_ is _3_ Province. "
                 "The province capital of _3_ is _4_, which develops rapidly from a small village to big city "
                 "with the advantage of traffic location. "
                 "In addition, the 2022 Olympic Winter Games will be held in _3_ Province too, but in another city _5_. "
                 "This city is famous for its snow-covered landscape."),
        'answers': ['34', 'beijing', 'hebei', 'shijiazhuang', 'zhangjiakou']
    },
   'medium': {
        'quiz': ("Earth's global ocean makes up approximately 70% of the planet's surface. "
                 "In order to categorize this vast amount, we have chosen to break this body of water into 5 major oceans: "
                 "_1_ Ocean, Atlantic Ocean, Indian Ocean, Arctic Ocean and Southern Ocean. "
                 "_1_ is the largest of these oceans and _2_ Ocean is the second largest, while _3_ Ocean is the smallest. "
                 "In addition, there are 7 continents: North America, South America, Europe, Antarctica, Asia, Africa and _4_. "
                 "_5_ covers nearly 9% of the earth's surface, making it the largest of the continents."),
        'answers': ['pacific','atlantic','arctic','australia','asia']
    },
   'hard': {
        'quiz': ("Please enter the abbreviation (Pinyin) of below Chinese provinces. "
                "Heilongjiang Provicen: _1_, Shandong Province: _2_, Shanghai: _3_, "
                "Hunan Province: _4_, Guangdong Province: _5_"),
        'answers': ['hei','lu','hu','xiang','yue']
    }
}
blanks = ['_1_', '_2_', '_3_', '_4_', '_5_']


def level_check(game_level):
    """check users' input
    Args:
        game_level: the level user enters
    Returns:
        'easy', 'medium' or 'hard'
    """ 
    while True:
        game_level = game_level.strip()  # trim whitespace if user inputs place/tab on both sides 
        if game_level == 'easy' or game_level == 'medium' or game_level == 'hard':
            print 'You have chosen {} game level! You will get 5 guesses per problem.'.format(game_level)
            return game_level
        else:
            game_level = raw_input('Note that please enter your game level from below choices (easy, medium or hard): \n')


def get_test_answer(game_level, game_data):
    """retrieve test and answers corresponding to the game level the user enters"""
    level = level_check(game_level)
    test = game_data[level]['quiz']
    answer = game_data[level]['answers']
    return test, answer


def check_answer(answer, user_ans, order):
    """check if the user's answer is correct
    Args:
        answer: correct answer
        user_ans: user's answer
        order: the question order
    Returns:
        True for correct, False otherwise.
    """
    user_ans = user_ans.lower()   # transfer to lowercase
    user_ans = user_ans.strip()  # trim whitespace if user inputs place/tab on both sides 
    return user_ans == answer[order] 


def fill_blank(test, blanks, order, user_ans):
    """to fill the blank with the correct answer"""
    filled_test = test.replace(blanks[order], user_ans)
    return filled_test


def play_game(game_data, blanks, question_num, choice_num):
    """the main function to play the game
    Args:
        game_data: data for quiz
        blanks: blanks need to be filled
        question_num: question number
        choice_num: answer choice for each question 
    Returns:
        True for correct, False otherwise.
    """
    game_level = raw_input('Welcome to geographical quiz! Please type in a game level you preferred (easy, medium or hard): \n')
    test, answer = get_test_answer(game_level, game_data)
    print 'The current paragraph reads as such:\n{}'.format(test)
    for order in range(question_num):
        user_ans = raw_input('What should be substitude in for {} ?'.format(blanks[order]))
        choice = 1
        while choice < choice_num:
            if check_answer(answer, user_ans, order):
                test = fill_blank(test, blanks, order, user_ans)
                print 'Correct! The current paragraph reads as such: \n{}'.format(test)
                break
            else:
                print 'Incorrect... Let us try again. You have {} choices left. The current paragraph reads as such:\n{}'.format(5-choice, test)
                user_ans = raw_input('What should be substitude in for {} ?'.format(blanks[order]))
                choice += 1 
        if choice == choice_num: 
            print 'Sorry, Game over.' 
            return
    print 'Congratulations! You finished the test!'


question_num = 5
choice_num = 5
play_game(game_data, blanks, question_num, choice_num)