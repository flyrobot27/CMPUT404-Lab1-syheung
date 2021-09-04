import requests

## LICENSE ##
"""
MIT License

Copyright (c) 2021 Steven Heung

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

print("requests version: " + requests.__version__)

result = requests.get("http://google.com/")
result_text = result.text
print("=" * 10 + " Google Page request result " + "=" * 10)
print(result.text)
print("=" * 14 + " Google result ends " + "=" * 14)

python_script = requests.get("https://raw.githubusercontent.com/flyrobot27/CMPUT404-Lab1-syheung/master/lab1.py")
print("=" * 10 + " Raw Python script " + "=" * 10)
print(python_script.text)
print("=" * 14 + " Ends " + "=" * 14)


