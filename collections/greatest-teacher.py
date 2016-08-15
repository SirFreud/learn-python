teachers = {
'Jason Seifer': 
['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 
'Kenneth Love': 
['Python Basics', 'Python Collections', 'Django Basics', 'Django Forms'], 
'Michael Valdez': 
['All the cool stuff', 'Making cool shit'], 
'Bob Jones': 
['Bob cant teach for shit']
}


def most_classes(teachers):
    highest_classes = ""
    temp = 0
    for value in teachers:
        if len(teachers[value]) > temp:
            temp = len(teachers[value])
            highest_classes = value
    return highest_classes


def num_teachers(teachers):
    total_num = len(teachers)
    return total_num


def stats(teachers):
    teacher_list = []
    for key in teachers:
        new_string = [key, len(teachers[key])]
        teacher_list.append(new_string)
    return teacher_list


def courses(teachers):
    course_list = []
    for courses in teachers:
        course_list.extend(teachers[courses])
    return course_list

print(courses(teachers))
# print(stats(teachers))
# print(most_classes(teachers))
# print (num_teachers(teachers))
