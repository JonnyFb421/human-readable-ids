# Human Readable ID
> Python library to generate a random human readable ID in the format of `<adjective> <noun> <number 1-100>`.


## Common Usage
This can be used any time you need a unique value that should be legible by humans (unlike a UUID).  
Currently this library only contains a single method: `get_new_id()`

```python
In [1]: import human_readable_ids                                                                                                                                                                                                       

In [2]: human_readable_ids.get_new_id()                                                                                                                                                                                                 
Out[2]: 'Short-term Painting 30'

```
