# Sessions

A better HTTPS session manager in python.
Based on the python requests session. 

## Usage

```python
>>> from Sessions import Sessions
>>> s = Sessions()
>>> s.get(url="https://google.com")
<Response [200]>
>>> s.parsed_response
<Element html at 0x7efbf8192908>
>>> s.parsed_response.xpath("//*[@id='hplogo']/@alt")
["Elena Cornaro Piscopia's 373rd Birthday"]

```