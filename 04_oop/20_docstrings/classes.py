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


class MyClass:
    """Normal documentatiion

    As another documentation you have used before. It can be a big block
    of documentation like in module documentation.
    """

    arrt1 = 1
    attr2 = "Value"

    def __init__(self, text: str):
        """Initializes the data

        :param text: the text of the class
        :type text: str
        """
        self.text = text

    @staticmethod
    def show_text(text: str):
        """Method that shows a 100 characters text

        :param text: a text of 100 characters
        :type text: str

        :return: The text of 100 characters
        :rtype: str

        :raises ValueError: If the text has more than 100 characters
        :raises TypeError: If the text is not a string
        """
        if not isinstance(text, str):
            raise TypeError("The text must be a string.")

        if len(text) > 100:
            raise ValueError("The text must have 100 characters or less.")

        return text
