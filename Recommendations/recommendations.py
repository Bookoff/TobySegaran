# -*- coding: utf-8 -*- 


# Словарь кинокритиков и выставленных ими оценок для небольшого набора данных о фильмах

critics={
'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5}, 
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}
}

from math import sqrt


# Возвращает оценку подобия person1 и person2 на основе расстояния

def sim_distance(prefs, person1, person2):
	# Получить список предметов, оцененных обоими
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1

	# Если нет ни одной общей оценки, вернуть 0
	if len(si)==0: return 0

	# Сложить квадраты разностей
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])

	return 1/(1+sum_of_squares)


#  Возвращает коэффициент корреляции Пирсона между p1 и p2
def sim_pearson(prefs,p1,p2):
	# Получить список предметов, оцененных обоими
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1
	# Найти число элементов
	n=len(si)

	# Если нет ни одной общей оценки, вернуть 0
	if n==0: return 0

	# Вычислить сумму всех предпочтений
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])

	# Вычислить сумму квадратов
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

	# Вычислить сумму произведений
	pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])

	# Вычислить коэффициент Пирсона
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))

	if den==0: return 0

	r=num/den

	return r


# Возвращает список наилучших соответствий для человека из словаря prefs
# Количество результатов в списке и функция подобия - необязательные параметры.

def topMatches(prefs, person, n=5, similarity=sim_pearson):
	scores=[(similarity(prefs,person,other), other) for other in prefs if other!=person]
	
	# Отсортировать список по убыванию оценок
	scores.sort()
	scores.reverse()
	return scores[0:n]