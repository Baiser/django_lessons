[1mdiff --git a/css/main.css b/css/main.css[m
[1mindex 4866efa..15c273b 100644[m
[1m--- a/css/main.css[m
[1m+++ b/css/main.css[m
[36m@@ -49,7 +49,7 @@[m [mh1, h2, h3, h4, h5, h6 {[m
 }[m
 [m
 .btn-primary{[m
[31m-    margin-left:-35px;[m
[32m+[m[32m    margin-left:0;[m
 }[m
 [m
 #form-footer{[m
[1mdiff --git a/students/views.py b/students/views.py[m
[1mindex 17bd84e..6016827 100644[m
[1m--- a/students/views.py[m
[1m+++ b/students/views.py[m
[36m@@ -1,3 +1,4 @@[m
[32m+[m[32m#-*- coding:utf-8 -*-[m
 from django.shortcuts import render[m
 from django.http import HttpResponse[m
 [m
[36m@@ -5,7 +6,23 @@[m [mfrom django.http import HttpResponse[m
 # Views Students[m
 [m
 def students_list(request):[m
[31m-    return render(request, 'students/students_list.html', {})[m
[32m+[m[32m    students = ({'id':1,[m
[32m+[m[32m                 'first_name':u'Олександр',[m
[32m+[m[32m                 'last_name':u'Шимель',[m
[32m+[m[32m                 'ticket':'1705',[m
[32m+[m[32m                 'image':'img/shim.jpg'},[m
[32m+[m[32m                {'id':2,[m
[32m+[m[32m                 'first_name':u'Ірина',[m
[32m+[m[32m                 'last_name':u'Любімова',[m
[32m+[m[32m                 'ticket':'2205',[m
[32m+[m[32m                 'image':'img/lyu.jpg'},[m
[32m+[m[32m                {'id':3,[m
[32m+[m[32m                 'first_name':u'Ярослав',[m
[32m+[m[32m                 'last_name':u'Каднічанський',[m
[32m+[m[32m                 'ticket':'2305',[m
[32m+[m[32m                 'image':'img/yar.jpg'}[m
[32m+[m[32m                )[m
[32m+[m[32m    return render(request, 'students/students_list.html', {'students':students})[m
 [m
 [m
 def students_add(request):[m
