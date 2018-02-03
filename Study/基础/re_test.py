"""
 Created by Victor Wu on 2017/12/22.
 
"""
import re
text = "是是是http://www.cos.sssss搜索"
pattern = '([hH][tT]{2}[pP]:/*|[hH][tT]{2}[pP][sS]:/*|[fF][tT][pP]:/*|www.)(([A-Za-z0-9-~]+).)+([A-Za-z0-9-~\\/])+(\\?(([A-Za-z0-9-~]+\\={0,1})([A-Za-z0-9-~]*)\\&{0,1})*)'
# pattern = '(http[s]?://|ftp://|file://)[a-zA-Z0-9\\.\\-]+\\.([a-zA-Z]+)(:\\d+)?(/[a-zA-Z0-9\\.\\-~!@#$%^&*+?:_/=<>]*)?'
print(re.match(pattern, text, flags=2))
