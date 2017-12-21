# -*- coding: utf8 -*-
import sys

# geographic quiz
# store game questions and answers in dict
game_data = {
   'easy': {
        'quiz': ('中国有_1_个省份（含直辖市和自治区），首都为_2_市，2008年奥运会在此举办。距离_2_市最近的省份是_3_省，'
                '该省的省会为_4_市, 依靠其便捷的地理交通位置迅速发展。2022年冬奥会将在_3_省_5_市举办。'),
        'answers': ['34', '北京', '河北', '石家庄', '张家口']
    },
   'medium': {
        'quiz': ('海洋占地球表面积的70%左右，我们通常将大洋分为五大洋：_1_，大西洋，印度洋，北冰洋和南冰洋。面积最大的大洋为'
        '_1_，面积第二的大洋为_2_， 面积最小的大洋为_3_。除了五大洋，通常将陆地分为七大洲，包括：北美洲，南美洲，欧洲，亚洲，'
        '非洲，_4_和南极洲。其中，面积最大的洲为_5_，约占地球表面积的9%。'),
        'answers': ['太平洋','大西洋','北冰洋','大洋洲','亚洲']
    },
   'hard': {
        'quiz': '请输入以下省份的简称。黑龙江省：_1_，山东省：_2_， 上海省：_3_，湖南省：_4_，广东省：_5_',
        'answers': ['黑','鲁','沪','湘','粤']
    }
}
blanks = ['_1_', '_2_', '_3_', '_4_', '_5_']

# game level input
game_level = raw_input(u'欢迎来到地理知识大闯关！请从下列三个选项中输入游戏等级：初级，中级，高级\n'.encode('gbk')).decode(sys.stdin.encoding)                          

def user_level(game_level):
    """check users' input
    Args:
        game_level: the level user enters
    Returns:
        'easy', 'medium' or 'hard'
    """ 
    while True:
        game_level = game_level.strip()  # trim whitespace if user inputs place/tab on both sides 
        if game_level != u'初级' and game_level != u'中级' and game_level != u'高级':
            game_level = raw_input(u'输入有误，请输入下列选项中的任意一个：初级，中级，高级\n'.encode('gbk')).decode(sys.stdin.encoding)
        else:
            print u'游戏开始，你选择的关卡为{}！每道题目你有5次作答机会哦'.format(game_level)
            if game_level == u'初级':
                return 'easy'
            elif game_level == u'中级':
                return 'medium'
            else:
                return 'hard'


def get_test_answer(game_level, game_data):
    """retrieve test and answers corresponding to the game level the user enters"""
    level = user_level(game_level)
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
    return user_ans == answer[order] 


def fill_blank(test, blanks, order, user_ans):
    """to fill the blank with the correct answer"""
    filled_test = test
    filled_test.replace(blanks[order], user_ans)
    return filled_test


def play_game(game_level, game_data, blanks):
    """to play the game"""
    test, answer = get_test_answer(game_level, game_data)
    print 'The current paragraph reads as such:\n{}'.format(test)
    question_num = 5
    choice_num = 5
    for order in range(question_num):
        user_ans = raw_input('What should be substitude in for {} ?'.format(blanks[order])).decode(sys.stdin.encoding)
        choice = 1
        while choice < choice_num:
            if check_answer(answer, user_ans, order):
                test = fill_blank(test, blanks, order, user_ans)
                print 'Correct! The current paragraph reads as such:\n'.format(test)
                break
            else:
                print 'Incorrect... Let us try again. You have {} choices left. The current paragraph reads as such:\n{}'.format(5-choice, test)
                user_ans = raw_input('What should be substitude in for {} ?'.format(blanks[order])).decode(sys.stdin.encoding)
                choice += 1 
        if choice == choice_num: 
            print 'Sorry, Game over.' 
            return
    print 'Congratulations! You finished the test!'


play_game(game_level, game_data, blanks)