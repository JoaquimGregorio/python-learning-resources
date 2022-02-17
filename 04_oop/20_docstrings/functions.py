"""Quicly and simple description

Pellentesque dapibus suscipit ligula.  Donec posuere augue in quam.
Etiam vel tortor sodales tellus ultricies commodo.  Suspendisse
potenti.  Aenean in sem ac leo mollis blandit.  Donec neque quam,
dignissim in, mollis nec, sagittis eu, wisi.  Phasellus lacus.  Etiam
laoreet quam sed arcu.  Phasellus at dui in ligula mollis ultricies.
Integer placerat tristique nisl.

Praesent augue.  Fusce commodo. Vestibulum convallis, lorem a tempus
semper, dui dui euismod elit, vitae placerat urna tortor vitae lacus.
Nullam libero mauris, consequat quis, varius et, dictum id, arcu.  Mauris
mollis tincidunt felis.  Aliquam feugiat tellus ut neque.  Nulla facilisis, risus a
rhoncus fermentum, tellus tellus lacinia purus, et dictum nunc justo
sit amet elit.
"""

var1 = "value 1"


def sum_values(x, y):
    """Sum x plus y"""
    return x + y


def multiply(x, y, z=None):
    """Multiply x, y and z

    Multiply x, y and z. The developer can ommit the variable z if
    he does not need it.
    """
    if z:
        return x * y * z

    return x * y


var2 = "value 2"
var3 = "value 3"
var4 = "value 4"
