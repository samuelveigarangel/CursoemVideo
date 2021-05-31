def notas(*n, status=False):
    """
        Calculates highest, lowest and average grades.
    :param n: Grades of student
    :param status: Show the student's situation
    :return: Dict with information of student
    """
    a = dict()
    a['total'] = len(n)
    a['highest'] = max(n)
    a['lowest'] = min(n)
    a['average'] = sum(n) / len(n)
    if status:
        if a['average'] >= 7:
            a['status'] = 'Great'
        elif 5 < a['average'] < 7:
            a['status'] = 'Medium'
        elif a['average'] < 5:
            a['status'] = 'Bad'
    return a


resp = notas(10, 8, 5.5, status=True)
print(resp)
