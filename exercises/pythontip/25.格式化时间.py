t = {"year": "2013", "month": "9", "day": "30", "hour": "16", "minute": "45", "second": "2"}
#输出：2013-09-30 16:45:02
print("%s-%s-%s %s:%s:%s" %tuple(t[i] if len(t[i])!=1 else "0"+t[i] for i in t))