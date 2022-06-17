 python -m pytest  -v -s   -m "sanity" --html=Reports\report.html testCases/ --browser Chrome
REM python -m pytest  -v -s   -m "regression" --html=Reports\report.html testCases/ --browser Chrome
REM python -m pytest  -v -s   -m "sanity and regression" --html=Reports\report.html testCases/ --browser Chrome
REM python -m pytest  -v -s   -m "sanit or regression" --html=Reports\report.html testCases/ --browser Chrome

