import io
import os

def is_id_invalid(id):
    if str(id) and str(id)[0] == '0':
        return False
    # consider only digits and check whether the digit-string is two repeats of a non-empty substring
    string = ''.join(ch for ch in str(id) if ch.isdigit())
    n = len(string)
    if n >= 2 and n % 2 == 0:
        half = n // 2
        if string[:half] == string[half:]:
            print(f"{id} is invalid")
            return True
    #print(f"{id} is valid")
    return False


def is_id_invalid_part2(id):
    # treat id as string and reject leading-zero IDs
    if str(id) and str(id)[0] == '0':
        return False
    # consider only digits and check whether the digit-string is k repeats of a non-empty substring (k >= 2)
    string = ''.join(ch for ch in str(id) if ch.isdigit())
    n = len(string)
    if n >= 2:
        # chop it up to 2 to floor(n)/2 + 1 times
        for sub_len in range(2, n // 2 + 1):
            if n % sub_len == 0:
                # if I can rebuild the string by apending the part I chopped..
                if string == string[:sub_len] * (n // sub_len):
                    print(f"{id} is invalid")
                    return True
    return False

if __name__ == "__main__":
    invaid_count = 0
    #print(is_id_invalid_part2(38593859))
    #print(is_id_invalid_part2(2121212121))
    with open("day2.txt", 'r') as fh:
        buf = []
        size = os.fstat(fh.fileno()).st_size
        while fh.tell() < size:
            while fh.tell() < size:
                ch = fh.read(1)
                if not ch or ch == ',':
                    break
                buf.append(ch)
            string = ''.join(buf)
            buf.clear()

            start, end = [int(s.strip()) for s in string.split('-', 1)]
            for i in range(start, end + 1):
                if is_id_invalid_part2(str(i)):
                    invaid_count += i
    print(invaid_count)