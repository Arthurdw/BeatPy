def repl(var):
    return var.replace('A', '1.5-').replace('B', '2.5-').replace('C', '3.5-').replace('D', '4.5-').replace('E', '5.5-')\
        .replace('F', '6.5-').replace('G', '7.5-').replace('H', '8.5').replace('I', '9.5-').replace('J', '10.5-')\
        .replace('K', '11.5-').replace('L', '12.5-').replace('M', '13.5-').replace('N', '14.5-').replace('O', '15.5-')\
        .replace('P', '16.5-').replace('Q', '17.5-').replace('R', '18.5-').replace('S', '19.5-').replace('T', '20.5-')\
        .replace('U', '21.5-').replace('V', '22.5-').replace('W', '23.5-').replace('X', '24.5-').replace('Y', '25.5-')\
        .replace('Z', '26.5-')


def ltn(text, first: bool = False):
    if first is True:
        prevent_errors = text.replace('1', '&').replace('2', 'é').replace('3', '#').replace('4', '@').replace('5', '(')\
            .replace('6', '§').replace('7', 'è').replace('8', '!').replace('9', 'ç').replace('0', 'à')
        higher_convert = repl(prevent_errors)
    else:
        higher_convert = repl(text)
    lower_convert = higher_convert.replace('a', '1-').replace('b', '2-').replace('c', '3-').replace('d', '4-')\
        .replace('e', '5-').replace('f', '6-').replace('g', '7-').replace('h', '8').replace('i', '9-')\
        .replace('j', '10-').replace('k', '11-').replace('l', '12-').replace('m', '13-').replace('n', '14-')\
        .replace('o', '15-').replace('p', '16-').replace('q', '17-').replace('r', '18-').replace('s', '19-')\
        .replace('t', '20-').replace('u', '21-').replace('v', '22-').replace('w', '23-').replace('x', '24-')\
        .replace('y', '25-').replace('z', '26-')
    return lower_convert


def ntl(text):
    prevent_errors = text.replace('&', '1').replace('é', '2').replace('#', '3').replace('@', '4').replace('(', '5')\
        .replace('§', '6').replace('è', '7').replace('!', '8').replace('ç', '9').replace('à', '0')
    higher_convert = prevent_errors.replace('26.5-', 'Z').replace('25.5-', 'Y').replace('24.5-', 'X')\
        .replace('23.5-', 'W').replace('22.5-', 'V').replace('21.5-', 'U').replace('20.5-', 'T').replace('19.5-', 'S')\
        .replace('18.5-', 'R').replace('17.5-', 'Q').replace('16.5-', 'P').replace('15.5-', 'O').replace('14.5-', 'N')\
        .replace('13.5-', 'M').replace('12.5-', 'L').replace('11.5-', 'K').replace('10.5-', 'J').replace('9.5-', 'I')\
        .replace('8.5', 'H').replace('7.5-', 'G').replace('6.5-', 'F').replace('5.5-', 'E').replace('4.5-', 'D')\
        .replace('3.5-', 'C').replace('2.5-', 'B').replace('1.5-', 'A')
    lower_convert = higher_convert.replace('26-', 'z').replace('25-', 'y').replace('24-', 'x').replace('23-', 'w')\
        .replace('22-', 'v').replace('21-', 'u').replace('20-', 't').replace('19-', 's').replace('18-', 'r')\
        .replace('17-', 'q').replace('16-', 'p').replace('15-', 'o').replace('14-', 'n').replace('13-', 'm')\
        .replace('12-', 'l').replace('11-', 'k').replace('10-', 'j').replace('9-', 'i').replace('8', 'h')\
        .replace('7-', 'g').replace('6-', 'f').replace('5-', 'e').replace('4-', 'd').replace('3-', 'c')\
        .replace('2-', 'b').replace('1-', 'a')
    return lower_convert


def ltb(text: str):
    emotes = [("#", "#️⃣"), ("0", "0️⃣"), ("1", "1️⃣"), ("2", "2️⃣"), ("3", "3️⃣"), ("4", "4️⃣"), ("5", "5️⃣"), ("6", "6️⃣"),
              ("7", "7️⃣"), ("8", "8️⃣"), ("9", "9️⃣"), ("10", "10️⃣"), ("z", ":regional_indicator_z:"),
              ("y", ":regional_indicator_y:"), ("x", ":regional_indicator_x:"), ("w", ":regional_indicator_w:"),
              ("v", ":regional_indicator_v:"), ("u", ":regional_indicator_u:"), ("u", ":regional_indicator_u:"),
              ("t", ":regional_indicator_t:"), ("s", ":regional_indicator_s:"), ("r", ":regional_indicator_r:"),
              ("q", ":regional_indicator_q:"), ("p", ":regional_indicator_p:"), ("o", ":regional_indicator_o:"),
              ("n", ":regional_indicator_n:"), ("m", ":regional_indicator_m:"), ("l", ":regional_indicator_l:"),
              ("k", ":regional_indicator_k:"), ("j", ":regional_indicator_j:"), ("i", ":regional_indicator_i:"),
              ("h", ":regional_indicator_h:"), ("g", ":regional_indicator_g:"), ("f", ":regional_indicator_f:"),
              ("e", ":regional_indicator_e:"), ("d", ":regional_indicator_d:"), ("c", ":regional_indicator_c:"),
              ("b", ":regional_indicator_b:"), ("a", ":regional_indicator_a:")]
    new_text = ""
    for letter in text.lower():
        for emoji in emotes:
            if letter == emoji[0]:
                new_text += text.replace(letter, emoji[1])
    return new_text
