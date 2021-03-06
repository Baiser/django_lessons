#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


# Views Students

def students_list(request):
    students = ({'id':1,
                 'first_name':u'Олександр',
                 'last_name':u'Шимель',
                 'ticket':'1705',
                 'image':'img/shim.jpg'},
                {'id':2,
                 'first_name':u'Ірина',
                 'last_name':u'Любімова',
                 'ticket':'2205',
                 'image':'img/lyu.jpg'},
                {'id':3,
                 'first_name':u'Ярослав',
                 'last_name':u'Каднічанський',
                 'ticket':'2305',
                 'image':'img/yar.jpg'}
                )
    return render(request, 'students/students_list.html', {'students':students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups
def groups_list(request):
    groups = ({'id':1,
              'name':u'HH-1',
              'leader':'Leader',},
             {'id': 2,
              'name': u'HH-2',
              'leader': 'Leader', },
             {'id': 3,
              'name': u'HH-3',
              'leader': 'Leader', }
                )
    return render(request, 'students/groups_list.html', {'groups':groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
