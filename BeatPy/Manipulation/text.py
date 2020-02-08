def triangle(text: str, separator: str = "\n"):
    """Receives a `string triangle`!
    Usage:
        Base:
            ->> Manipulation.triangle("text")
            <<- 't\nte\ntex\ntext\ntext\ntex\nte\nt'
        or with a custom separator.
            ->> Manipulation.triangle("text", "\nsep\n")
            <<- 't\nsep\nte\nsep\ntex\nsep\ntext\nsep\ntext\nsep\ntex\nsep\nte\nsep\nt'
        """
    previous_letters, cool_string = "", []

    for letter in text:
        cool_string.append(previous_letters + letter)
        previous_letters += letter

    return separator.join(cool_string) + separator + separator.join(cool_string[::-1])
