#!/usr/bin/python3
print(''.join(f'{chr(122-i) if i % 2 == 0 else chr(90 - ((i//2)*2 + 1))}' for i in range(26)), end='')

