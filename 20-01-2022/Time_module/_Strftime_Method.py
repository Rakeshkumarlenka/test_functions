'''
FORMAT CODE OF STRFTIME=====
-----------------------------------

%a    ==> Weekdays as an abbreviated name (Sun, Mon..........)
%A    ==> Weekdays as fullname (Sunday, monday.................)
%w    ==> Weekdays as decimal no, where Sunday as 0 and saturday as 6(0, 1, 2, 3,......)
%d    ==> Day of month as Zero-padded decimal no(01, 02, 03 ........)
%b    ==> Month as abbreviated name( Jan, Feb, ........)
%B    ==> Month as full name (January, February,......)
%m    ==> Month as zero-padded decimal no (01,02,03......12)
%-m	  ==> Month as a decimal number.	1, 2, ..., 12
%y	  ==> Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	  ==> Year without century as a decimal number.	0, 1, ..., 99
%Y	 ==> Year with century as a decimal number.	2013, 2019 etc.
%H	==> Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	==> Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	==> Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	==> Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	==> Locale’s AM or PM.	AM, PM
%M	==> Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	==> Minute as a decimal number.	0, 1, ..., 59
%S	==> Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	==> Second as a decimal number.	0, 1, ..., 59
%f	==> Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	==> UTC offset in the form +HHMM or -HHMM.
%Z	==> Time zone name.
%j	==> Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%-j	==> Day of the year as a decimal number.	1, 2, ..., 366
%U	==> Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%W	==> Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	==> Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	==> Locale’s appropriate date representation.	09/30/13
%X	==> Locale’s appropriate time representation.	07:06:05
%%	==> A literal '%' character.	%
'''